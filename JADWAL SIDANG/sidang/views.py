from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from jadwal . models import jadwal
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import authenticate

def home(request):
    
    return render(request,'index.html')

def detail(request):
    if request.user.is_active:
        data1 = User.objects.get(username=request.user)
        data =jadwal.objects.filter(penggugat=data1)
    else:
        return redirect('login')

    context = {
        'datas':data,
    }

    print(request.user.is_active)
    return render(request,'detail.html',context)

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            messages.error(request," Password tidak sama!")  
            return redirect('signup')
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            messages.success(request,"Selamat, Register Berhasil!")  
            return redirect('login')

    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)

            if user.is_superuser:
                return redirect('/admin/')
            else:
                messages.success(request,"Selamat, Login Berhasil!")  
                return redirect('home')
        else:
            messages.error(request,"Username atau Password tidak valid!!")
            return redirect('login')

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')
    return render(request,'login.html')