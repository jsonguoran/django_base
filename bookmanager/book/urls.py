from django.urls import path, include
from .views import index
from .views import postman
from .views import goods
from .views import get_best_book
from .views import register
from .views import parse_json
from .views import phone_register
from .views import response
from .views import redirect_test
from .views import web_main
from .views import set_cookie
from .views import get_cookie
from .views import use_session


urlpatterns = [
    path('index/', index),
    path('postman/', postman),
    path('<year>/<month>/<day>/', goods),
    path('book/', get_best_book),
    path('register/', register),
    path('parse_json/', parse_json),
    path('<mobile:phone>/', phone_register),
    path('response_test/', response),
    path('redirect_test/', redirect_test),
    path('main/', web_main),
    path('set_cookie/', set_cookie),
    path('get_cookie/', get_cookie),
    path('use_session/', use_session)
]
