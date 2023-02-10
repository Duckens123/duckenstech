from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from articles.models import Article,Contact
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def Index(request):
    lastarticle=Article.objects.all().order_by("-id")[0]
    most_read=Article.objects.all().order_by("-nb_views")[0]
    articles=Article.objects.all().order_by("-id")
    page_num=request.GET.get('page,1')
    paginator=Paginator(articles,6)
    try:
        page_obj=paginator.page(page_num)
    except PageNotAnInteger:
        page_obj=paginator.page(1)
    except EmptyPage:
        page_obj=paginator.page(paginator.num_pages)
    context={'lastarticle': lastarticle,'most_read': most_read,'articles': articles,'page_obj': page_obj}
    message=Contact()
    if request.method == 'POST':
        message.name=request.POST['name']
        message.email=request.POST['email']
        message.message=request.POST['message']
        message.save()
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'articles/index.html',context)


def DisplayArticle(request,id):
    article=Article.objects.get(pk=id)
    article.nb_views+=1
    article.save()
    return render(request,'articles/display_article.html',{'article' : article})


def About(request):
    return render(request,'articles/display_about.html')

