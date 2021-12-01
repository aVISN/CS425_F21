# docs forms: https://docs.djangoproject.com/en/3.2/topics/forms/ 

from django import forms

from .models import Upload

# ModelForm: https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/
class UploadForm(forms.ModelForm):
    class Meta: 
        model = Upload
        fields = ('description', 'comments', 'filename')
