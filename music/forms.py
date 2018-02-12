from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Song, Profile

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'genre', 'singer', 'rating']

class SignUpForm(UserCreationForm):
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    birth_date = forms.DateField(label='Birth Date')
    gender = forms.ChoiceField(widget=forms.Select, choices=gender_choices)
    address = forms.CharField(max_length=50, widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birth_date', 'gender', 'address', 'email', 'username', 'password1', 'password2' ]