from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse


class IndexView(View):

    def get(self, request):
        return redirect('article', tags='python', article_id=42)


def article(request, tags, article_id):
    return HttpResponse(f'Статья номер {article_id}. Тег {tags}.')