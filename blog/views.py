from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/carousel.html', {})

def signup(request):
    return render(request, 'blog/signup.html', {})

def class_details(request):
    return render(request, 'blog/class_details.html', {})

def instructor_details(request):
    return render(request, 'blog/instructor_details.html', {})

def hotclass_details(request):
    return render(request, 'blog/hotclass_details.html', {})

def yoga_details(request):
    return render(request, 'blog/yoga_details.html', {})

def oneday_class_details(request):
    return render(request, 'blog/oneday_class_details.html', {})

def pilates_details(request):
    return render(request, 'blog/pilates_details.html', {})

def view_on_map(request):
    return render(request, 'blog/view_on_map.html', {})
