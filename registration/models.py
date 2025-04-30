from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return "profiles/" + filename

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null =True, blank = True)
    link = models.URLField(null=True, blank=True, max_length=200)

#Los perfiles de usuario se crean al iniciar sesion, pero ¿Qué pasa si un usuario se registra por primera vez, pero no inicia sesión?
#Para prevenir que a un usuario recién registrado pero que no haya iniciado sesión no se le cree el perfil, creare una señal
#De esta manera se crea una señal, que se ejecutará cada vez que se guarde la instancia del usuario.
@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get("created", False):#De esta manera comprobamos que es la primera vez que se guarda la instancia de ese usuario, ya que existirá el campo "created", de lo contrario será False. Así me aseguro de que la señal solo se ejecute la primera vez que se guarde un user, y no cada vez que se guarde después de actualizar un usuario existente.
        Profile.objects.get_or_create(user=instance)
        #print("Perfil creado correctamente")