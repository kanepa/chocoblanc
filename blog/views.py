from django.shortcuts import render
from django.utils import timezone
from.models import Post
from django.shortcuts import render, get_object_or_404


# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, "postdetail.html", {'post': post})

def profile(request):
    return render(request, 'profile.html')