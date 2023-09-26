from django.shortcuts import render, get_object_or_404

from .models import Article, Introduction


def home_view(request):

    try:
        introduction = Introduction.objects.get(template_tag="home_introduction")
    except Introduction.DoesNotExist:
        introduction = None

    articles = Article.objects.all()

    context = {
        'introduction': introduction,
        'articles': articles
    }

    return render(request, 'home.html', context=context)


def article_view(request, article_id):

    introduction = Introduction.objects.all()
    intro_context = {'introduction': introduction}

    article = get_object_or_404(Article, id=article_id)
    article_context = {'article': article}

    combined_context = {**intro_context, **article_context}

    return render(request, 'article.html', context=combined_context)
