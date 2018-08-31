from django.shortcuts import render, get_object_or_404
from box.models import Articles, Tags


def articles_list(request):
    articles = Articles.objects.all()
    return render(request, 'box/articles_list.html', {'articles': articles})


def article_singl(request, id_article):
    article = get_object_or_404(Articles, id=id_article)
    return render(request, 'box/article_singl.html', {'article': article})


def articles_tag(request, id_tag):
    articles = Articles.objects.all().filter(tag=id_tag)
    tag_name = Tags.objects.get(id=id_tag)
    context = {
        'articles': articles,
        'tag_name':tag_name,
    }
    return render(request, 'box/articles_tags.html', context)
    

def tags_list(request):
    tags = Tags.objects.all()
    return render(request, 'box/tags_list.html', {'tags': tags})
    
def contacts(request):
    return render(request, 'box/contacts.html', {})
