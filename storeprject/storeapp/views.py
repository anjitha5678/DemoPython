from django.http import HttpResponse
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from . models import School,Store

# Create your views here.
def index(request):
    obj=School.objects.all()
    obj1=Store.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})
def forms(request):
    return render(request,'forms.html')
def new(request):
    return render(request,'new.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        # if user is not None:
        #     auth.login(request,user)
        #     return redirect('/')
        # else:
        #     messages.info(request,'invalid credentials')
        #     return redirect('login')

    return render(request, 'login.html')






def register(request):
    if request.method =='POST':
        username = request.POST['username']

        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return  redirect('login')
            # elif User.objects.filter(email=email).exists():
            #     messages.info(request, 'email Taken')
                return redirect('register')
            else:


              user=User.objects.create_user(username=username,password=password)

              user.save();
              return redirect('login')


        else:
            messages.info(request,'password not matched')
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')
def personal_info(request):
    if request.method =='POST':
        full_name = request.POST['Full Name']
        Mobile = request.POST['Mobile']
        Department = request.POST['Department']
        Other_Department = request.POST['Other Department']


        Course = request.POST['Course']
        Other_Course = request.POST['Other Course']
        Address = request.POST['Address']

        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=full_name).exists():
                messages.info(request,'Username Taken')
                return  redirect('login')
            # elif User.objects.filter(email=email).exists():
            #     messages.info(request, 'email Taken')
                return redirect('personal_info')
            else:


              user=User.objects.create_user(username=full_name,password=password,Mobile=Mobile,Department=Department,Other_Department=Other_Department,Course=Course,Other_Course=Other_Course,Address=Address)

              user.save();
              return redirect('login')


        else:
            messages.info(request,'password not matched')
            return redirect('register')
        return redirect('/')
    return render(request,'personal_info.html')