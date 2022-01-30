from datetime import datetime

from django import forms

from .models import Recipe, Image


class RecipeForm(forms.ModelForm):
    created = forms.DateTimeField(initial=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), required=False)
    class Meta:
        model = Recipe
        fields = '__all__'


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', )