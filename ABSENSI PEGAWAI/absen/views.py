from django.shortcuts import render,redirect
from absenapp . models import absenModel,profil
from django.contrib.auth import authenticate
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt

def print_absen_data(request):
    if 'ids' in request.GET:
        ids = request.GET['ids'].split(',')
        # Mengambil data absenModel sesuai dengan id yang dipilih
        absen_data = absenModel.objects.filter(id__in=ids)
        # Render template untuk halaman pencetakan data absenModel
        context = {'absen_data': absen_data}
        return render(request, 'print_absen.html', context)

@csrf_exempt
def akun(request):
    if request.user.is_active:
        # ambil nama berdasarkan user yang aktif dari tabel profil -> (1 jenis data yaitu nama)
        profile=profil.objects.get(nama=request.user)

        # ambil data pegawai berdasarkan user yang aktif (profil) dari tabel absenmodel ->(semua data)
        datas= absenModel.objects.filter(pegawai=profile)

        # inisialiasi jumlah status: hadir,izin dan pulang serta cuti
        jh=0
        ji=0
        jp=0
        jc=0
        # untuk mendaptkan jumlah sesuai status maka setiap kali melakukan absen akan di jumlahkan sesuai dengan statusnya
        for jlh in datas:
            if jlh.status == 'HADIR': #jika status absennya hadir maka variabel inisialisasi kita jumlahkan
                jh += 1
            elif jlh.status == 'IZIN':
                ji += 1
            elif jlh.status == 'PULANG':
                jp += 1
            elif jlh.status == 'CUTI':
                jc += 1
            else:
                pass

        #paginator
        data = datas.order_by('-tgl')
        hal = Paginator(data,5)
        hal_list = request.GET.get('page')
        datas = hal.get_page(hal_list)
    else:
        return redirect('absen:login')

    context = {
        'datas':datas,
        'jlh_hadir':jh,
        'jlh_izin':ji,
        'jlh_pulang':jp,
        'jlh_cuti':jc,
    }

    return render(request,'akun.html',context)

def index(request):

    return render(request, 'index.html')


