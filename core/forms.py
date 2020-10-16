from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
# from django.forms import formset_factory
from .models import GaleryPhoto


class UploadImageForm(forms.ModelForm):
    '''This class references a form before to post in the body,
    when send a new image.'''
    name = forms.CharField(max_length=150)
    description = forms.CharField(widget=forms.Textarea )
    image = forms.FileInput()

    class Meta:
        model = GaleryPhoto
        fields = ['name', 'description', 'image']


class UpdateImageForm(forms.ModelForm):
    '''This class references a action when user want left free a image'''   
    approved = forms.BooleanField(label="", initial=False, required=False)

    class Meta:
        model = GaleryPhoto
        fields = ['approved',]
