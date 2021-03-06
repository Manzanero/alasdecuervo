from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import News


def news_list(request):
    news = News.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/news_list.html', {'news': news})


def news_detail(request, pk):
    piece = get_object_or_404(News, pk=pk)
    return render(request, 'blog/news_detail.html', {'piece': piece})
