from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse
from django.views.generic import ListView

from .models import Article


def index(request):
    a = Article.objects.all()
    paginator = Paginator(a, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/test.html', {'page_obj': page_obj})


def main_page(request):
    return render(request, 'blog/index.html')


def article_detail(request, article_id):
    a = Article.objects.get(id=article_id)
    comments = a.comment_set.order_by('-pub_date')
    return render(request, 'blog/article_detail.html', {'article': a, 'comments': comments})


def leave_comment(request, article_id):
    a = Article.objects.get(id=article_id)
    a.comment_set.create(name=request.POST['name'], content=request.POST['content'])
    return HttpResponseRedirect(reverse('articles:article_detail', args=(a.id,)))


def about(request):
    return render(request, 'blog/about.html')


# def search_results(request):
#     search = request.POST['search']
#     a = Article.objects.filter(title__icontains=search)
#     paginator = Paginator(a, 3)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'blog/search.html', {'page_obj': page_obj})


class Search(ListView):
    paginate_by = 3
    template_name = 'blog/search.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(title__icontains=self.request.GET.get('search'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = self.request.GET.get('search')
        return context
