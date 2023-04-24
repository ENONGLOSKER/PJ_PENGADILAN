from django.contrib import admin
from . models import absenModel,profil
from django.contrib import admin
from .models import profil, absenModel
from django.http import HttpResponse, HttpResponseRedirect 

# Tambahkan action untuk mencetak data absenModel
def print_absen_data(modeladmin, request, queryset):
    # Mengambil data absenModel yang dipilih
    selected = queryset.values_list('id', flat=True)
    # Redirect ke halaman pencetakan data absenModel
    return HttpResponseRedirect('/print/absen/?ids={}'.format(','.join(map(str, selected))))
print_absen_data.short_description = "Cetak data absen"

# Tambahkan action untuk mencetak data profil
def print_profil_data(modeladmin, request, queryset):
    # Mengambil data profil yang dipilih
    selected = queryset.values_list('id', flat=True)
    # Redirect ke halaman pencetakan data profil
    return HttpResponseRedirect('/print/profil/?ids={}'.format(','.join(map(str, selected))))
print_profil_data.short_description = "Cetak data profil"

class ProfilAdmin(admin.ModelAdmin):
    actions = [print_profil_data]
    list_display = ('nama','nip','jenisK','jabatan','alamat')
    list_filter = ['nama','nip','jenisK','jabatan','alamat']

class AbsenModelAdmin(admin.ModelAdmin):
    actions = [print_absen_data]
    readonly_fields = ['tgl','waktu'] #untuk menmpilkan kolom yang tersembunyi
    list_display = ('pegawai','status','ket','waktu','tgl') #untuk menu pencarian berdasarkan kategori
    list_filter = ['pegawai','status','tgl','waktu'] #untuk membuat tampilkan tabel pada admin

admin.site.register(profil, ProfilAdmin)
admin.site.register(absenModel, AbsenModelAdmin)



# class absenAdmin(admin.ModelAdmin):
#     readonly_fields = ['tgl','waktu'] #untuk menmpilkan kolom yang tersembunyi
#     list_display = ('pegawai','status','ket','waktu','tgl') #untuk menu pencarian berdasarkan kategori
#     list_filter = ['pegawai','status','tgl','waktu'] #untuk membuat tampilkan tabel pada admin

# class profilAdmin(admin.ModelAdmin):
#     list_display = ('nama','nip','jenisK','jabatan','alamat')
#     list_filter = ['nama','nip','jenisK','jabatan','alamat']

# #untuk mendaptarkan tabel ke admin
# admin.site.register(absenModel,absenAdmin)
# admin.site.register(profil,profilAdmin)

# untuk merubah/edit nama header/judul panel admin
admin.site.site_header= 'Absensi Online'

