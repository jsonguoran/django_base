from django.urls import path, include
from .views import index
from .views import postman
urlpatterns = [
    path('index/', index),
    path('postman/', postman),
]
