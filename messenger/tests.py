from django.test import TestCase
from .models import Message, Thread
from django.contrib.auth.models import User

# Create your tests here.

class MessengerTestCase(TestCase):
    def setUp(self):
        self.user_1= User.objects.create_user("user_1", None, "ekaitz-2003")
        self.user_2= User.objects.create_user("user_2", None, "ekaitz-2003")
        self.user_3= User.objects.create_user("user_3", None, "ekaitz-2003")
        

        self.thread = Thread.objects.create()

    def test_add_user_to_thread(self):
        self.thread.users.add(self.user_1, self.user_2)
        self.assertEqual(len(self.thread.users.all()), 2)

    def test_get_thread_by_user(self):
        self.thread.users.add(self.user_1, self.user_2)
        thread = Thread.objects.filter(users=self.user_1). filter(users=self.user_2)#Obtener todos los threads donde participe el user_1 y el user_2
        self.assertEqual(thread[0], self.thread)

    def test_get_thread_non_user(self):
        threads = Thread.objects.filter(users=self.user_1).filter(users=self.user_2)
        self.assertNotEqual(threads, self.thread)
        self.assertEqual(len(threads),0)

    def test_add_message_to_thread(self):
        self.thread.users.add(self.user_1, self.user_2)
        message_1 = Message.objects.create(user=self.user_1, content="Hola, muy buenas")
        message_2 = Message.objects.create(user=self.user_2, content="Que hay!")
        self.thread.messages.add(message_1, message_2)
        self.assertEqual(len(self.thread.messages.all()), 2)

        for message in self.thread.messages.all():
            print(f"({message.user}):{message.content}")

    def test_filter_message_from_user_not_in_thread(self):
        self.thread.users.add(self.user_1, self.user_2)
        message_1 = Message.objects.create(user=self.user_1, content="Hola que tal?")
        message_2 = Message.objects.create(user=self.user_2, content="Bien, y tu?")
        message_3 = Message.objects.create(user=self.user_3, content="Soy un espía?")
        self.thread.messages.add(message_1, message_2, message_3)
        self.assertEqual(len(self.thread.messages.all()), 2)

    
    def test_find_thread_with_custom_manager(self):
        self.thread.users.add(self.user_1, self.user_2)
        thread = Thread.objects.find(self.user_1, self.user_2)
        self.assertEqual(self.thread, thread)

    def test_find_or_create_thread_with_custom_manager(self):
        self.thread.users.add(self.user_1, self.user_2)
        thread = Thread.objects.find_or_create(self.user_1, self.user_2)
        self.assertEqual(self.thread, thread)
        thread_2 = Thread.objects.find_or_create(self.user_1, self.user_3)
        self.assertIsNotNone(thread_2)

