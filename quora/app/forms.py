from django import forms
from .models import Questions, Tags
from ckeditor.widgets import CKEditorWidget

class LoginForm(forms.Form):
    kulad = forms.CharField()
    parola = forms.CharField(widget=forms.PasswordInput)


class NewQuestion(forms.ModelForm):
    class Meta:
        model = Questions
        exclude = ['user_id', 'tags']


class AnswerForm(forms.Form):
    context = forms.CharField(widget=CKEditorWidget)


class SignForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()    
    mail = forms.CharField(widget=forms.EmailInput)

    