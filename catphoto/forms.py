from django import forms
from PIL import Image
from .models import *

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', )