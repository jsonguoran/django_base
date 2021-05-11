from django.shortcuts import render

# Create your views here.
# 导入HTTPResponse模块
from django.http import HttpResponse
# 导入redner模块
from django.shortcuts import render

# 导入模型类
from .models import BookInfo, PeopleInfo
# 定义试图函数


def index(request):
    # 准备上下文：定义在字典中（测试数据）
    context = {'title': '测试模板处理数据'}
    # 将上下文交给模板中进行处理，处理后视图响应给客户端
    return render(request, 'book/index.html', context)


def postman(request):
    context = {
        'content':'来自Django这种用于postman测试的内容'
    }
    return render(request, 'book/postman.html', context)


def goods(request, year, month, day):
    pub_date = str(year) + '-' + str(month) + '-' + str(day)
    book = BookInfo.objects.filter(pub_date=pub_date)
    books = []
    for book_name in book:
        books.append(book_name)
    return HttpResponse(books)