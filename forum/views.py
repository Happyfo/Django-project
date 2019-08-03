from django.shortcuts import render
from .models import Post


def forum(request):
    data = Post.objects.all()
    context = {
        'object': data
    }
    return render(request, 'forum/forum.html', context)
