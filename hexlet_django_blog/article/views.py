from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

from hexlet_django_blog.article.models import Article


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'article/index.html', context={
            'articles': articles,
        })


def article(request, tags, article_id):
    return HttpResponse(f'Статья номер {article_id}. Тег {tags}.')