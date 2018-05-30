from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser



class UserRegistration(UserCreationForm):


    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'date_of_birth', 'sex')
        labels = {'first_name': 'Imię', 'last_name': 'Nazwisko', 'date_of_birth': 'Data urodzenia', 'sex': 'Płeć'}


class UserEditForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'first_name', 'last_name', 'date_of_birth', 'sex')
        labels = {'date_of_birth': 'Data urodzenia', 'sex': 'Płeć'}

