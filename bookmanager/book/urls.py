from django.urls import path, include
from .views import index
from .views import postman
from .views import goods
from .views import get_best_book
from .views import register
urlpatterns = [
    path('index/', index),
    path('postman/', postman),
    path('<year>/<month>/<day>/', goods),
    path('book/', get_best_book),
    path('register/', register),
]
