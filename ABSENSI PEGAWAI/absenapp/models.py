from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# tabel untuk profile karyawan
class profil(models.Model):
    nama        =models.OneToOneField(User, on_delete=models.CASCADE, related_name='profil')
    nip         =models.CharField(max_length=50, default='-')
    jk =(
        ('Laki-Laki','L'),
        ('Perempuan','P'),
    )
    jenisK      =models.CharField(choices=jk, max_length=10)
    jabatan     =models.CharField(max_length=50,null=True)
    alamat      =models.TextField()
    

    def __str__(self):
        return "{}".format(self.nama)

# tabel utnuk absen karyawan
class absenModel(models.Model):
    # data karyawan    
    pegawai     =models.ForeignKey(profil, on_delete=models.DO_NOTHING)
    tgl         =models.DateField(auto_now_add=True)
    waktu       =models.TimeField(auto_now_add=True)
    absen=(
        ('HADIR','HADIR'),
        ('IZIN','IZIN'),
        ('PULANG','PULANG'),
        ('CUTI','CUTI'),
    )
    status      =models.CharField(choices=absen, max_length=50, default='HADIR')
    ket         =models.TextField(null=True, blank=True) 

    def __str__(self):
        return "{}".format(self.pegawai)