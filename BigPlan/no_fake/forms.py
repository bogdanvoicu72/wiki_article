from django import forms
from .models import Document
class HashCode(forms.Form):
    hash_code = forms.SlugField(label='ObjectID')


class ImageForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('desc', 'document')



