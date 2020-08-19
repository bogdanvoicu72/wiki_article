from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('setcookie', views.setcookie),
    path('getcookie', views.showcookie),
]