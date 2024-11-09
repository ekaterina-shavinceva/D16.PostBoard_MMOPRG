from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from allauth.account.forms import SignupForm
from django.core.mail import send_mail
from .models import Article
from string import hexdigits
import random



class ArticleForm(forms.ModelForm):
    title = forms.CharField(min_length=1)
    text = forms.CharField(min_length=1)
    class Meta:
        model = Article
        fields = ['title', 'text', 'category', 'upload']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')
        if title == text:
            raise ValidationError({
                'title': 'Название не может совпадать с текстом'
            })
        return cleaned_data


class CommonSignupForm(SignupForm):
    def save(self, request):
        user = super(CommonSignupForm, self).save(request)
        user.is_active = False
        code = ''.join(random.sample(hexdigits, 5))
        user.code = code
        user.save()
        send_mail(
            subject=f'Код активации',
            message=f'Код активации аккаунта: {code}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
        )
        return user



