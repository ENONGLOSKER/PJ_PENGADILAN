from django.db import models
from django.contrib.auth.models import User


class Katagori(models.Model):
    Kode_kategori    = models.CharField(max_length=50, editable=False)
    Nama_kategori    = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.Kode_kategori)
    
    def save(self, *args, **kwargs):
        if not self.id:  # hanya berlaku untuk objek baru
            total_kategori = Katagori.objects.count()
            self.Kode_kategori = 'KT{:03d}'.format(total_kategori + 1)
        super(Katagori, self).save(*args, **kwargs)

class Suplier(models.Model):
    Kode_suplier   = models.CharField(max_length=50, unique=True, editable=False)
    Nama_suplier   = models.CharField(max_length=50)
    Alamat_suplier = models.TextField()
    Tlpn_suplier   = models.CharField(max_length=50)
    
    def __str__(self):
         return "{}".format(self.Nama_suplier)
    
    def save(self, *args, **kwargs):
        if not self.Kode_suplier:
            last_suplier = Suplier.objects.last()
            if last_suplier:
                last_suplier_number = int(last_suplier.Kode_suplier[2:]) + 1
            else:
                last_suplier_number = 1
            self.Kode_suplier = 'SP{:03d}'.format(last_suplier_number)
        super(Suplier, self).save(*args, **kwargs)

class Barang(models.Model):
    Kode_barang = models.CharField(max_length=5, unique=True, primary_key=True, editable=False)
    Nama_barang = models.CharField(max_length=50)
    stok_barang = models.CharField(max_length=50)
    Kode_kategori = models.ManyToManyField(Katagori)
    Kode_suplier = models.ManyToManyField(Suplier)

    def __str__(self):
        return "{},{}".format(self.Kode_barang, self.Nama_barang)

    def get_kode_kategori(self):
        return ", ".join([str(kategori) for kategori in self.Kode_kategori.all()])

    get_kode_kategori.short_description = "Kategori"
    
    def get_kode_suplier(self):
        return ", ".join([str(suplier) for suplier in self.Kode_suplier.all()])

    get_kode_suplier.short_description = "Suplier"

    def save(self, *args, **kwargs):
        if not self.Kode_barang:
            last_Kode_barang = Barang.objects.all().order_by('Kode_barang').last()
            if last_Kode_barang:
                Kode_barang = int(last_Kode_barang.Kode_barang[2:]) + 1
            else:
                Kode_barang = 1
            self.Kode_barang = 'BR{:03d}'.format(Kode_barang)
        super(Barang, self).save(*args, **kwargs)
    
class Transaksi(models.Model):  
    id_transaksi    = models.AutoField(primary_key=True)#auto increment
    tgl_transaksi   = models.DateField(auto_now_add=True) 
    waktu_transaksi = models.TimeField(auto_now_add=True) 
    Kode_barang     = models.ForeignKey(Barang, on_delete=models.DO_NOTHING, default='1')
    ambil_transaksi = models.CharField(max_length=50)
    nama_admin      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Transaksi')

    def __str__(self):
        return "{}".format(self.id_transaksi)
  
    def save(self, *args, **kwargs):
        barang = self.Kode_barang
        barang.stok_barang = str(int(barang.stok_barang) - int(self.ambil_transaksi))
        barang.save()
        super(Transaksi, self).save(*args, **kwargs)