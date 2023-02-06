from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from . models import Department,Course
from  django.core.paginator import Paginator,EmptyPage,InvalidPage


# Create your views here.

def allProdCat(request,c_slug=None):
    c_page=None
    courses_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Department,slug=c_slug)
        courses_list=Course.objects.all().filter(department=c_page,available=True)
    else:
        courses_list=Course.objects.all().filter(available=True)
    paginator = Paginator(courses_list, 6)
    try:
         page = int(request.GET.get('page', '1'))
    except:
         page = 1
    try:
         courses = paginator.page(page)
    except (EmptyPage, InvalidPage):
         courses = paginator.page(paginator.num_pages)


    return render(request,'department.html',{'department' :c_page,'courses':courses})
def proDetail(request,c_slug,course_slug):
    try:
        course=Course.objects.get(department__slug=c_slug,slug=course_slug)
    except Exception as e:
        raise e
    return render(request,'course.html',{'course':course})