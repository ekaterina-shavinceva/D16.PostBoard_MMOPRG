from django.urls import path
from .views import ArticleList, ArticleDetail, ArticleCreate, ArticleUpdate, ArticleDelete
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', ArticleList.as_view(), name='article'),
    path('<int:pk>', ArticleDetail.as_view(), name='article'),
    path('create/', ArticleCreate.as_view(), name='article_create'),
    path('<int:pk>/update/', ArticleUpdate.as_view(), name='article_update'),
    path('<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]