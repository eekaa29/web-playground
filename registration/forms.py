from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class RequiredEmailForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 carácteres como máximo.")

    class Meta():
        model = User
        fields = ("username", "email", "password1","password2")
        
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email existente, introduzca un email nuevo por favor")
        return email
    
class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ["avatar", "bio", "link"]
        widgets = {
            "avatar": forms.ClearableFileInput(attrs= {"class":"form-control-file mt-3"}),
            "bio" : forms.Textarea(attrs={"class":"form-control-file mt-3","rows": 3, "placeholder":"Biografía"}),
            "link" : forms.URLInput(attrs={"class":"form-control-file mt-3","placeholder":"Link"})
        }

class UpdateEmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 carácteres como máximo.")
    class Meta:
        model = User
        fields = ["email"]
        #No debo de cometer el error de configurar aquí los widgets, ya que el modelo User ya tiene sus propias 
        #configs sobre autenticación, sus propioswidgets... Entonces si lo hago aquí me cargaría todo eso.
        #Para evitarlo, es mejor configurar los widgets de este form en views.py(en tiempo de ejecución)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if "email" in self.changed_data:#change_data es una lista interna de django donde se almacenan todos los campos que han sido modificados
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("Email existente, introduzca un email nuevo por favor")
        return email
        