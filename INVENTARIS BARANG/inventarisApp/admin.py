from django.contrib import admin
from . models import Katagori,Suplier,Barang,Transaksi

# Register your models here.
class TransaksiAdmin(admin.ModelAdmin):
    list_display = ('id_transaksi','tgl_transaksi','waktu_transaksi','Kode_barang','ambil_transaksi','nama_admin')
    list_filter = ['Kode_barang','tgl_transaksi','waktu_transaksi']

class SuplierAdmin(admin.ModelAdmin):
    list_display = ('Kode_suplier','Nama_suplier','Alamat_suplier','Tlpn_suplier')
    list_filter = ['Kode_suplier','Nama_suplier','Alamat_suplier']

class BarangAdmin(admin.ModelAdmin):
    list_display = ('Kode_barang', 'Nama_barang', 'stok_barang', 'get_kode_kategori','get_kode_suplier')
    list_filter = ['Kode_barang','Nama_barang']

class KatagoriAdmin(admin.ModelAdmin):
    list_display = ('Kode_kategori','Nama_kategori')
    list_filter = ['Kode_kategori','Nama_kategori']

admin.site.register(Katagori,KatagoriAdmin)
admin.site.register(Suplier,SuplierAdmin)
admin.site.register(Barang,BarangAdmin)
admin.site.register(Transaksi,TransaksiAdmin)