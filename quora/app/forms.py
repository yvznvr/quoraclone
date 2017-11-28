from django import forms
from .models import Questions

class LoginForm(forms.Form):
    kulad = forms.CharField()
    parola = forms.CharField(widget=forms.PasswordInput)

class NewQuestion(forms.ModelForm):
    class Meta:
        model = Questions
        exclude = ['user_id']