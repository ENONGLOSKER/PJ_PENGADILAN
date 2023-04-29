from django.contrib import admin
from . models import absenModel,profil
from django.contrib import admin
from .models import profil, absenModel
from django.http import HttpResponse, HttpResponseRedirect 
from django.utils.html import format_html


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
    readonly_fields = ['tgl','waktu'] # menambahkan field image_tag sebagai read-only field
    list_display = ('pegawai','status','ket','waktu','tgl','foto_preview') 
    list_filter = ['pegawai','status','tgl','waktu']

    def foto_preview(self, obj):
        return format_html('<img src="{}" height="50" />'.format(obj.foto.url))

    foto_preview.short_description = 'Foto Preview'

admin.site.register(absenModel, AbsenModelAdmin)
admin.site.register(profil, ProfilAdmin)


# untuk merubah/edit nama header/judul panel admin
admin.site.site_header= 'Absensi Online'

