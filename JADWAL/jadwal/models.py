from django.db import models
from django.contrib.auth.models import User


class jadwal(models.Model):
    tgl             = models.DateTimeField(auto_now_add=False) 
    noPerkara       = models.CharField(max_length=50, default="0001/Pdt.G/2023/PA.Sel" )
    jenisPerkara    = models.CharField(max_length=50)
    penggugat       = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pengguna')
    tergugat        = models.CharField(max_length=50,default='tergugat')
    sdk = (
        ('Ya','Ya'),
        ('Tidak','Tidak')
    )
    sidangKeliling  = models.CharField(choices=sdk, max_length=50)
    rng = (
        ('Ruang Sidang Utama','Ruang Sidang Utama'),
        ('Ruang Sidang Dua','Ruang Sidang Dua'),
    )
    ruangan  = models.CharField(choices=rng, max_length=50)
    agenda   = models.TextField()
    created  = models.DateTimeField(auto_now_add=True) 
    updated  = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return "{}".format(self.penggugat)

