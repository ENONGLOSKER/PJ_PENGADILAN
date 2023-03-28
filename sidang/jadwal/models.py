from django.db import models
from django.contrib.auth.models import User


class jadwal(models.Model):
    tgl             = models.DateTimeField(auto_now_add=False) 
    noPerkara       = models.CharField(max_length=50, default="3125/Pdt.G" )
    jenisPerkara    = models.CharField(max_length=50)
    pihak           = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pengguna')
    sdk = (
        ('Ya','Ya'),
        ('Tidak','Tidak')
    )
    sidangKeliling  = models.CharField(choices=sdk, max_length=50)
    rng = (
        ('Ruang Sidang 1','Ruang Sidang 1'),
        ('Ruang Sidang 2','Ruang Sidang 2'),
        ('Ruang Sidang 3','Ruang Sidang 3'),
        ('Ruang Sidang 4','Ruang Sidang 4'),
        ('Ruang Sidang 5','Ruang Sidang 5'),
    )
    ruangan  = models.CharField(choices=rng, max_length=50)
    agenda   = models.TextField()
    created  = models.DateTimeField(auto_now_add=True) 
    updated  = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return "{}".format(self.pihak)

