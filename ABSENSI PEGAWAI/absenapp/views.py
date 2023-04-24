from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from absenapp . models import absenModel,profil
from .forms import profilForm,absenForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# @login_required() #fungsi ini bisa diakses setelah login berhasil
@csrf_exempt
def absen(request):

    if request.user.is_active:
        data = absenModel.objects.all() #ambil semua data di tabel absenmodel
        ab = absenForm() 

        pgaw = profil.objects.get(nama=request.user)

        if request.method == 'POST':
            absenModel.objects.create(
                pegawai = pgaw,
                status  = request.POST.get('status'),
                ket     = request.POST.get('ket'),
            )
            messages.success(request,"Selamat Absen Berhasil")
            return redirect('akun')
    else:
        return redirect('absen:login')

    #lempar data yang sudah didapat ke templates
  
    context = { 
        'profile':ab,
        'datas':data,
    }
    return render(request, 'absen.html',context)
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

# AKUN
@csrf_exempt
def register(request):
    if request.method=='POST':
        username=request.POST.get('username') #megambil data dari form username
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2: #jika password/password 1 tidak sama dengan confirm password atau password ke 2
            messages.warning(request, 'Password tidak sama!')
            return redirect('absen:register') #ke halaman register
        else: #jika sama password 1 dengan ke 2
            my_user=User.objects.create_user(username,email,pass1) #buat user baru dengan data username,email dan password
            my_user.save()
            messages.success(request,"Selamat Register Berhasil")
            return redirect('absen:profile') #ke halaman login

    return render(request,'register.html')
@csrf_exempt
def loginAkun(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('passw')

        user=authenticate(request,username=username,password=pass1) #cek username dan password
        if user is not None: #jika username dan password ada di database maka
            login(request, user) 
            
            if user.is_superuser: #jika user adalah admin maka tampilkan halaman ad  min
                return redirect('/admin/')
            else: #jika user bukan admin maka tampilkan halaman absen
                messages.success(request,"Selamat, Login Berhasil!")  
                return redirect('akun')

        else:# jika username dan password  tidak ada
            messages.warning(request,'Username dan Password tidak Valid!!')
            return redirect('absen:login') 
    return render(request,'login.html')

def logoutAkun(request):
    logout(request) 
    return redirect('absen:login')


