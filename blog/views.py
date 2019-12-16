from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.
def index(requset):
    post_list=Post.objects.all().order_by('-create_time')

    return render(requset,'blog/index.html',context={
        'post_list':post_list,
    })
def detail(requset,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(requset,'blog/detail.html',context={'post':post})