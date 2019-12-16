from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index(requset):
    return render(requset,'blog/index.html',context={
        'title':'我的微博首页',
        'welcome':'欢迎来到我的微博首页'
    })