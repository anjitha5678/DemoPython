from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages,auth
import json

from .models import Person, get_s_strings, get_c_strings,get_e_strings,get_p_strings,get_b_strings
from .forms import PersonForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('new')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    return render(request, 'login.html')

def new(request):
    return render(request,'new.html')





def register(request):
    if request.method =='POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        # email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return  redirect('register')
            # elif User.objects.filter(email=email).exists():
            #     messages.info(request, 'email Taken')
            #     return redirect('register')
            else:


                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name)

                user.save();


                return redirect('login')


        else:
            messages.info(request, 'password not matched')
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')

def personal_info(request):
    context = {}

    personform = PersonForm()
    context['personform'] = personform

    s_strings = get_s_strings()
    c_strings = get_c_strings()
    e_strings = get_e_strings()
    p_strings = get_p_strings()
    b_strings = get_b_strings()

    json_s_strings = json.dumps(s_strings)
    json_c_strings = json.dumps(c_strings)
    json_e_strings = json.dumps(e_strings)
    json_p_strings = json.dumps(p_strings)
    json_b_strings = json.dumps(b_strings)

    context['json_s_strings'] = json_s_strings
    context['json_c_strings'] = json_c_strings
    context['json_e_strings'] = json_e_strings
    context['json_p_strings'] = json_p_strings
    context['json_b_strings'] = json_b_strings

    return render(request, 'personal_info.html', context)
def form(request):
    return render(request,'form.html')
