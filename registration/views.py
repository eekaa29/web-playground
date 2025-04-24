from .forms import RequiredEmailForm, ProfileForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from django import forms
from .models import Profile



# Create your views here.

class SignUpView(CreateView):
    form_class=RequiredEmailForm
    template_name = "registration/signup.html"
    def get_success_url(self):
        return reverse_lazy("login") + "?registration"
    
    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        #Moificar el formulario:
        form.fields["username"].widget = forms.TextInput(attrs={"class":"form-control mb-2", "placeholder":"Nombre de Usuario"})
        form.fields["email"].widget = forms.EmailInput(attrs={"class":"form-control mb-2", "placeholder":"Email"})
        form.fields["password1"].widget = forms.PasswordInput(attrs={"class":"form-control mb-2", "placeholder":"Contraseña"})
        form.fields["password2"].widget = forms.PasswordInput(attrs={"class":"form-control mb-2", "placeholder":"Repite la contraseña"})

        return form
    

@method_decorator(staff_member_required, name="dispatch")
class ProfileUpdate(UpdateView):
    form_class=ProfileForm
    success_url=reverse_lazy("profile")
    template_name = "registration/profile_form.html"

    def get_object(self):
        #Recuperar el objeto(usuario) que se va a editar. 
        #El objetivo es averiguar el user que está accediendo al perfil, para crearle uno en caso de que este no exista.
        #Recordar que es una realción OneToOne, un solo perfil para un solo user
        profile, created = Profile.objects.get_or_create(user=self.request.user)#Esot devuelve 2 tuplas,por un lado el user, por otro un Booleano para saber si se ha creado o no el perfil
        return profile
    
