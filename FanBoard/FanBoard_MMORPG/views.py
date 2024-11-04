from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Article
from datetime import datetime

class ArticleList(ListView):
    model = Article
    ordering = 'article_time'
    template_name = 'articles.html'
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class ArticleDetail(DetailView):
    model = Article
    template_name = 'article.html'
    context_object_name = 'article'

#
# class ArticleCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
#     raise_exception = True
#     permission_required = ('article.add_post',)
#     form_class = ArticleForm
#     model = Article
#     template_name = 'post_edit.html'
#
#     def form_valid(self, form):
#         post = form.save(commit=False)
#         if self.request.path == '/news/articles/create/':
#             post.post_type = article
#         post.save()
#         return super().form_valid(form)
