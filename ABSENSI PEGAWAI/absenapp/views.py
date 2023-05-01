from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from absenapp . models import absenModel,profil
from .forms import profilForm,absenForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
# def absen(request):

    # if request.user.is_active:
        
    #     ab = absenForm(request.POST or None) 

    #     if request.method == 'POST':
    #         pgaw = profil.objects.get(nama=request.user)
    #         absenModel.objects.create(
    #             pegawai = pgaw,
    #             status  = request.POST.get('status'),
    #             ket     = request.POST.get('ket'),
    #             foto    = request.POST.get('foto'),
    #         )
    #         messages.success(request,"Selamat Absen Berhasil")
    #         return redirect('akun')
    # else:
    #     return redirect('absen:login')
    
    # data = absenModel.objects.all() #ambil semua data di tabel absenmodel

    # #lempar data yang sudah didapat ke templates
  
    # context = { 
    #     'profile':ab,
    #     'datas':data,
    # }
    # return render(request, 'absen.html',context)

def absen(request):
    if not request.user.is_authenticated:
        return redirect('absen:login')
    ab = absenForm() 
    if request.method == 'POST':
        ab = absenForm(request.POST, request.FILES)
        if ab.is_valid():
            pgaw = profil.objects.get(nama=request.user)
            absen = ab.save(commit=False)
            absen.pegawai = pgaw
            absen.save()
            messages.success(request, 'Selamat Absen Berhasil')
            return redirect('akun')
            
    data = absenModel.objects.all() 
    context = { 
        'profile': ab,
        'datas': data,
    }
    return render(request, 'absen.html', context)

@csrf_exempt
def profile(request):

    karyawan=profilForm(request.POST or None)
    if request.method == 'POST':
        if karyawan.is_valid():
            karyawan.save()
        return redirect('absen:login')

    context = {
        'karyawan':karyawan,
    }
    return render(request,'profile.html', context)

@csrf_exempt
def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2: 
            messages.warning(request, 'Password tidak sama!')
            return redirect('absen:register')
        else: 
            my_user=User.objects.create_user(username,email,pass1)
            my_user.save()
            messages.success(request,"Selamat Register Berhasil")
            return redirect('absen:profile') 

    return render(request,'register.html')
@csrf_exempt
def loginAkun(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('passw')

        user=authenticate(request,username=username,password=pass1) 
        if user is not None: 
            login(request, user) 
            
            if user.is_superuser: 
                return redirect('/admin/')
            else: 
                messages.success(request,"Selamat, Login Berhasil!")  
                return redirect('akun')

        else:
            messages.warning(request,'Username dan Password tidak Valid!!')
            return redirect('absen:login') 
    return render(request,'login.html')

def logoutAkun(request):
    logout(request) 
    return redirect('absen:login')


