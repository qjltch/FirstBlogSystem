from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
# Create your views here.
def index(requset):
    post_list=Post.objects.all().order_by('-create_time')

    return render(requset,'blog/index.html',context={
        'post_list':post_list,
    })