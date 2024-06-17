from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


import django.forms.utils
import django.forms.widgets


class RegisterForm(forms.ModelForm):
    username = forms.CharField(label="Kullanıcı Adı" , max_length=40)
    email = forms.CharField(label="E-Posta Adresiniz" , max_length=150 , widget=forms.EmailInput)
    password1 = forms.CharField(label="Şifre" , widget=forms.PasswordInput ,  max_length=20)
    password2 = forms.CharField(label="Yeniden Şifre",widget=forms.PasswordInput , max_length= 20)

    class Meta:
        model = User
        fields=[
        'username',
        'email',
        'password1',
        'password2',
        ]

    def clean_password(self):
        password1= self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError("Parolalar Eşleşmiyor")
        return password2


class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı" , max_length=40)

    password = forms.CharField(label="Şifre", widget=forms.PasswordInput,max_length=20)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username = username, password = password)
            if not(user):
                raise forms.ValidationError("Hafıza Hücrelerine Bi Baktır İstersen")
        return super(LoginForm,self).clean()
