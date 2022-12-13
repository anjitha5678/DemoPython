from django.http import HttpResponse
from django.shortcuts import render
from . models import place,traveller
# Create your views here.
def demo(request):
    obj=place.objects.all()
    dis=traveller.objects.all()

    return render(request,'index.html',{'result':obj,'result1':dis})

