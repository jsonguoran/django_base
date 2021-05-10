from django.shortcuts import render

# Create your views here.
# 导入HTTPResponse模块
from django.http import HttpResponse
# 导入redner模块
from django.shortcuts import render
# 定义试图函数


def index(request):
    # 准备上下文：定义在字典中（测试数据）
    context = {'title': '测试模板处理数据'}
    # 将上下文交给模板中进行处理，处理后视图响应给客户端
    return render(request, 'book/index.html', context)

