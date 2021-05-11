from django.urls import path, include
from .views import index
from .views import postman
from .views import goods
urlpatterns = [
    path('index/', index),
    path('postman/', postman),
    path('<year>/<month>/<day>/', goods),
]
