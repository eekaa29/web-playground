from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile
# Create your tests here.

class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user("test", "test@gmail.com", "test1234")

    def test_profile_exists(self):
        exist = Profile.objects.filter(user__username = "test").exists()#Esto devuelve un booleano, si el usuario existe devuelve True, si no existe devulve false
        self.assertEqual(exist, True)#Comprobar que exist == True, en cuyo caso pasará el test.