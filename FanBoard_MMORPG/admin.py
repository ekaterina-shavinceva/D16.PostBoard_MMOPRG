from django.contrib import admin
from .models import Article, UserResponse, Subscription, Category


admin.site.register(Article)
admin.site.register(UserResponse)
admin.site.register(Subscription)
admin.site.register(Category)
