from django.shortcuts import render,redirect
from suratapp . models import SuratMasuk, SuratKeluar
from django.contrib.auth import authenticate
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt

def print_surat_masuk_data(request):
    if 'ids' in request.GET:
        ids = request.GET['ids'].split(',')
        # Mengambil data SuratMasuk sesuai dengan id yang dipilih
        surat_masuk_data = SuratMasuk.objects.filter(id__in=ids)
        # Render template untuk halaman pencetakan data SuratMasuk
        context = {'surat_masuk_data': surat_masuk_data}
        return render(request, 'print_surat_masuk.html', context)

def print_surat_keluar_data(request):
    if 'ids' in request.GET:
        ids = request.GET['ids'].split(',')
        # Mengambil data SuratMasuk sesuai dengan id yang dipilih
        surat_keluar_data = SuratKeluar.objects.filter(id__in=ids)
        # Render template untuk halaman pencetakan data SuratMasuk
        context = {'surat_keluar_data': surat_keluar_data}
        return render(request, 'print_surat_keluar.html', context)

def index(request):
    return render(request, 'index.html')