from django import forms
from .models import Questions
from ckeditor.widgets import CKEditorWidget

class LoginForm(forms.Form):
    kulad = forms.CharField()
    parola = forms.CharField(widget=forms.PasswordInput)


class NewQuestion(forms.ModelForm):
    class Meta:
        model = Questions
        exclude = ['user_id']


class AnswerForm(forms.Form):
    context = forms.CharField(widget=CKEditorWidget)