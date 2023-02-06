from . import views
from django.urls import path

app_name='teapp'
urlpatterns = [

    path('', views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat,name='courses_by_department'),
    path('<slug:c_slug>/<slug:course_slug>/', views.proDetail,name='courDeptdetail')


]