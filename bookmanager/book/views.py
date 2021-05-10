from django.shortcuts import render

# Create your views here.
# 导入HTTPResponse模块
from django.http import HttpResponse

# 定义试图函数


def index(request):
    return HttpResponse('OK')

