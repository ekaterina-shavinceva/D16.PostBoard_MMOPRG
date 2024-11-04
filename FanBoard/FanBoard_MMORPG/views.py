from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .forms import ArticleForm
from .models import Article
from datetime import datetime
from .filters import ArticleFilter

class ArticleList(ListView):
    model = Article
    ordering = 'article_time'
    template_name = 'articles.html'
    context_object_name = 'articles'
    paginate_by = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ArticleFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context


class ArticleDetail(DetailView):
    model = Article
    template_name = 'article.html'
    context_object_name = 'article'


def create_article(request):
    form = ArticleForm()

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/articles/')

    return render(request, 'article_edit.html', {'form': form})
