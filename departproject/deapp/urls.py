from . import views
from django.urls import path

app_name='deapp'
urlpatterns = [


    path('', views.allProdCat,name='allProdCat'),
    path('register/',views.register,name='register'),
    path('new/', views.new, name='new'),
    # path('click/',views.forms,name='click'),
    path('forms/',views.forms,name='forms'),

    path('personal_info/',views.personal_info,name='personal_info'),
    path('<slug:c_slug>/', views.allProdCat,name='courses_by_department'),
    path('<slug:c_slug>/<slug:course_slug>/', views.proDetail,name='courDeptdetail'),
    path('login', views.login, name='login')




]