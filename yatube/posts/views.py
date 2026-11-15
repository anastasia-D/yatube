from django.shortcuts import render

from .models import Post


def index(request):
    posts = Post.objects.select_related('author').order_by('-pub_date', '-pk')
    return render(request, 'posts/index.html', {'posts': posts})


def group_posts(request, slug):
    return render(request, 'posts/group_list.html', {'slug': slug})
