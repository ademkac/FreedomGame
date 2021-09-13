from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^sendstate$', views.sendstate, name='sendstate'),
    re_path(r'^sendstate1$', views.sendstate1, name='sendstate1'),
    re_path(r'^sendstate2$', views.sendstate2, name='sendstate2'),

]
