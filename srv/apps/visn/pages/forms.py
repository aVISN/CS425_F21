# docs forms: https://docs.djangoproject.com/en/3.2/topics/forms/ 

from django import forms

from .models import Upload
from django.core.mail import send_mail

# ModelForm: https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/
class UploadForm(forms.ModelForm):
    class Meta: 
        model = Upload
        fields = ('description', 'comments', 'filename')

class EmailChangeForm(forms.Form):
    new_email = forms.EmailField()

class CreateClientLoginForm(forms.Form):
    client_email = forms.EmailField()