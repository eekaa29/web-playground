from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

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
