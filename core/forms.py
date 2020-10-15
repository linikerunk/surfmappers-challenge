from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import GaleryPhoto

CHOICES=[('Aceitar', True),
         ('Negar', False)]

class UploadImageForm(forms.ModelForm):
    '''This class references a form before to post in the body,
    when send a new image.'''
    name = forms.CharField(max_length=150)
    description = forms.CharField(widget=forms.Textarea )
    image = forms.FileInput()

    class Meta:
        model = GaleryPhoto
        fields = ['name', 'description', 'image']


class UploadImageManageForm(forms.ModelForm):
    '''This class references a action when user want left free a image'''
    approved = forms.CharField(widget=forms.RadioSelect(
        choices=CHOICES))
    

    class Meta:
        model = GaleryPhoto
        fields = ['approved',]