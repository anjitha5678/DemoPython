from . import views
from django.urls import path

urlpatterns = [

    path('',views.index,name='index'),
    path('login', views.login, name='login'),
    path('register/',views.register,name='register'),
    path('personal_info/',views.personal_info,name='personal_info'),
    path('forms/',views.forms,name='forms'),
    path('new/',views.new,name='new')






]
