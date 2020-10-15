from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import GaleryPhoto


# Here bellow we have the forms about our models...
class UploadImageForm(forms.ModelForm):
    '''This class references a form before to post in the body.'''
    name = forms.CharField(max_length=150)
    description = forms.CharField(widget=forms.Textarea )
    approved = forms.BooleanField(label="New Geeks Field")

    class Meta:
        model = GaleryPhoto
        fields = ['name', 'description', 'image', 'approved']