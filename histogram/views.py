from django.shortcuts import render
from .models import *
# Create your views here.

def Home(request):
    if 'q' in request.GET:
        q = request.GET['q']
        posts = Post.objects.filter(title__icontains=q)
        # posts = Post.objects.filter(topic__icontains=q)
        # posts = Post.objects.filter(date__icontains=q)
    else:    
        posts = Post.objects.all()
    return render (request, 'home.htm',{'posts':posts})