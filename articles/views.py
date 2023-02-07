from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from articles.models import Article

# Create your views here.
def Index(request):
    lastarticle=Article.objects.all().order_by("-id")[0]
    most_read=Article.objects.all().order_by("-nb_views")[0]
    context={'lastarticle': lastarticle,'most_read': most_read}
    return render(request, 'articles/index.html',context)


def DisplayArticle(request,id):
    article=Article.objects.get(pk=id)
    article.nb_views+=1
    article.save()
    return render(request,'articles/display_article.html',{'article' : article})
