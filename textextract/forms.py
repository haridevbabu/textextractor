from django import forms
from textextract.models import ExtractText

class UrlForm(forms.ModelForm):

    class Meta:
        model = ExtractText
        fields = [
            'blog_url'

            ]