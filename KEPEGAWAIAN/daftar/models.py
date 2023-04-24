from django.db import models

# Create your models here.
class Pegawaai_PNS(models.Model):
    id          = models.CharField(max_length=50, primary_key=True)
    nama        = models.CharField(max_length=50)
    NIP         = models.CharField(max_length=50)
    alamat      = models.TextField()
    tgl_lahir   = models.DateField(auto_now_add=False)
    pendidikan  = models.CharField(max_length=50)
    jabatan     = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.nama)

class Pegawaai_HONORER(models.Model):
    id          = models.CharField(max_length=50, primary_key=True)
    nama        = models.CharField(max_length=50)
    alamat      = models.TextField()
    tgl_lahir   = models.DateField(auto_now_add=False)
    pendidikan  = models.CharField(max_length=50)
    jabatan     = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.nama)
