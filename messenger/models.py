from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import m2m_changed
# Create your models here.

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created"]

class ThreadsManager(models.Manager):
    def find(self, user1, user2):
        queryset = self.filter(users=user1).filter(users=user2)#Dentro de un object manager, la palabra "self" hace referencia a todas las instancias del modelo; Es decir que es lo mismo que hacer=> Thread.objects.all()
        if len(queryset) > 0:
            return queryset[0]#Asumiendo que no va a haber más de un hilo con los mismos users
        return None
    
    def find_or_create(self, user1, user2):
        thread = self.find(user1, user2)
        if thread is None:
            thread = Thread.objects.create()
            thread.users.add(user1, user2)
        return thread 

class Thread(models.Model):
    users = models.ManyToManyField(User, related_name="threads")
    messages = models.ManyToManyField(Message)
    updated = models.DateTimeField(auto_now=True)
    objects = ThreadsManager()#De esta manera añado los nuevos ModelManagers al modelo que yo quiera

    class Meta:
        ordering = ["-updated"]

def messages_changed(sender, **kwargs):
    instance = kwargs.pop("instance", None)
    action = kwargs.pop("action", None)
    pk_set = kwargs.pop("pk_set", None)
    print(instance, action, pk_set)

    false_msg = set()
    if action == "pre_add":
        for msg_pk in pk_set:
            msg = Message.objects.get(pk=msg_pk)
            if msg.user not in instance.users.all():
                print(f"El usuario {msg.user} no forma parte del hilo")
                false_msg.add(msg_pk)

    pk_set.difference_update(false_msg)
    #Forzar la actualización haciendo save(para que el campo updated se actualize y aparezcan los hilos más recientes arriba del todo)
    instance.save()


m2m_changed.connect(messages_changed, sender=Thread.messages.through)

