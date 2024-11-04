from django import forms
from .models import Article
from django.core.exceptions import ValidationError

class ArticleForm(forms.ModelForm):
    title = forms.CharField(min_length=1)
    text = forms.CharField(min_length=1)
    class Mets:
        model = Article
        fields = ['author', 'title', 'text', 'category']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')
        if title == text:
            raise ValidationError({
                'title': 'Название не может совпадать с текстом'
            })
        return cleaned_data
