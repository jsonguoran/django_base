import json

from django.shortcuts import render, redirect

# Create your views here.
# 导入HTTPResponse模块
from django.http import HttpResponse

from django.http import JsonResponse

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


def get_best_book(request):
    # 如果请求的url中没有对应的key，则value为0并赋值给变量
    readcount = request.GET.getlist('readcount', 0)
    commentcount = request.GET.getlist('commentcount', 0)
    print(readcount, commentcount)
    if len(commentcount) == 2 and len(readcount) == 1:
        min_commentcount = commentcount[0]
        max_commentcount = commentcount[-1]
        books = BookInfo.objects.filter(readcount__gt=readcount[0], commentcount__gt=min_commentcount,commentcount__lt=max_commentcount)
    if len(readcount) == 1 and len(commentcount) == 1:
        books = BookInfo.objects.filter(readcount__gt=readcount[0], commentcount__gt=commentcount[0])
    books_list = []
    for book_name in books:
        books_list.append(book_name)
    return HttpResponse(books_list)


def register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username, password)
    return HttpResponse('用户注册成功!')

def parse_json(request):
    json_data = request.body
    req_data = json.loads(json_data)
    print(req_data['username'], req_data['password'])
    return HttpResponse('body中json格式数据解析成功!')


def phone_register(request, phone):
    return HttpResponse(phone)


def response(request):
    content = {
        'name': 'pinginglab',
        'pass': 'password',
    }
    return JsonResponse(content)


def redirect_test(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username, password)
    return redirect('/main')

def web_main(request):
    return HttpResponse('这是注册成功后的网站主页!')


def set_cookie(request):
    response = HttpResponse('set_cookie')
    response.set_cookie('username', 'pinginglab')
    return response


def get_cookie(request):
    if 'username' in request.COOKIES:
        return HttpResponse('Your username is {0}'.format(request.COOKIES['username']))
    else:
        return HttpResponse('No Cookies.')


def use_session(request):
    if 'username' in request.session:
        username = request.session['username']
        response = HttpResponse('Your username is {}'.format(username))
        # del request.session['username']
        return response
    else:
        request.session['username'] = 'pinginglab'
        return HttpResponse('no session.')


def set_session(request):
    if 'username' in request.session:
        username = request.session['username']
        response = HttpResponse('Your username is {}'.format(username))
        return response
    else:
        request.session['username'] = 'pinginglab'
        return HttpResponse('login successed.')


def get_session(request):
    username = request.session['username']
    response = HttpResponse('Your username is {}'.format(username))
    return response

from django.contrib.sessions.models import Session
def session_test(request):
    # sid = request.COOKIES['sessionid']
    sid = request.session.session_key
    s = Session.objects.get(pk=sid)
    s_info = 'Session ID:{} <br>Expire_date:{} <br>Data:{}'.format(sid,s.expire_date,s.get_decoded())
    return HttpResponse(s_info)


def book_list(request):
    books = BookInfo.objects.all()
    print(books)
    request.session['books'] = books
    return render(request, 'book/books.html', locals())
