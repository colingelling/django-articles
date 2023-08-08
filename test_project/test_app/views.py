from django.shortcuts import render

from . models import Article


def home_view(request):

    articles = Article.objects.all()
    context = {'articles': articles}

    return render(request, 'home.html', context=context)
