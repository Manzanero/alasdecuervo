from django.shortcuts import render


def news_list(request):
    return render(request, 'blog/news_list.html', {})
