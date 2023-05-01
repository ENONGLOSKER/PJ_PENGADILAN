from django.contrib import admin
from suratapp .models import SuratMasuk,SuratKeluar
from django.http import HttpResponse, HttpResponseRedirect 

# Register your models here.
def print_surat_masuk_data(modeladmin, request, queryset):
    # Mengambil data absenModel yang dipilih
    selected = queryset.values_list('id', flat=True)
    # Redirect ke halaman pencetakan data absenModel
    return HttpResponseRedirect('/print/masuk/?ids={}'.format(','.join(map(str, selected))))
print_surat_masuk_data.short_description = "Cetak Surat Masuk"

class masukAdmin(admin.ModelAdmin):
    actions = [print_surat_masuk_data]
    list_display = ('Kode','Sifat','Asal','Nomor','Isi_Ringkasan','Tujuan','Tanggal','File','Keterangan') #untuk menu pencarian berdasarkan kategori
    list_filter = ['Kode','Tanggal','Nomor'] #untuk membuat tampilkan tabel pada admin

def print_surat_masuk_data(modeladmin, request, queryset):
    # Mengambil data absenModel yang dipilih
    selected = queryset.values_list('id', flat=True)
    # Redirect ke halaman pencetakan data absenModel
    return HttpResponseRedirect('/print/keluar/?ids={}'.format(','.join(map(str, selected))))
print_surat_masuk_data.short_description = "Cetak Surat Keluar"


class keluarAdmin(admin.ModelAdmin):
    actions = [print_surat_masuk_data]
    list_display = ('Agenda','Sifat','Isi_Ringkasan','File','Nomor','Tanggal','Keterangan','Tujuan') #untuk menu pencarian berdasarkan kategori
    list_filter = ['Sifat','Tanggal','Nomor'] #untuk membuat tampilkan tabel pada admin


admin.site.register(SuratMasuk, masukAdmin)
admin.site.register(SuratKeluar, keluarAdmin)