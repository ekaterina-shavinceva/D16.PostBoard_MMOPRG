from django.db import models
from django.contrib.auth.models import User
# from django.urls import reverse
#
# from .resources import TYPE


class Category(models.Model):
    TYPE = (
        ('tank', 'Танки'),
        ('heal', 'Хилы'),
        ('dd', 'ДД'),
        ('buyers', 'Торговцы'),
        ('gildemaster', 'Гилдмастеры'),
        ('quest', 'Квестгиверы'),
        ('smith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('potion', 'Зельевары'),
        ('spellmaster', 'Мастера заклинаний'),
    )
    name = models.CharField(max_length=25, choices=TYPE, default='Tanks')

    def __str__(self):
        return self.name

#
# class Author(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     #
#     # def __str__(self):
#     #     return self.user.username


class Article(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    article_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=120)
    text = models.TextField()
    category = models.ManyToManyField(Category, default='Tanks')
    # upload = models.FileField(upload_to='uploads/')

    def __str__(self):
        return f'Заголовок: {self.title}. Содержание: {self.text}. {self.article_time}. Категория: {self.category}'
    #
    # def get_absolute_url(self):
    #     return reverse('article_list')


class UserResponse(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.article.title


class Subscription(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='subscriptions')
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='subscriptions')
