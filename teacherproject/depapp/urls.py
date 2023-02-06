from . import views
from django.urls import path


urlpatterns = [

    path('register', views.register,name='register'),
    path('login',views.login,name='login'),
    path('new',views.new,name='new'),
    path('personal_info',views.personal_info,name='personal_info'),
    path('form',views.form,name='form'),



]