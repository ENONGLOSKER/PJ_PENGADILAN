from django.db import models

class SuratMasuk(models.Model):
    Kode            = models.CharField(max_length=100, default='0001/HM.00')
    sft = (('Biasa','Biasa'),
        ('Penting','Penting'),
        ('Segera','Segera'),
        ('Sangat Segera','Sangat Segera'),
    )
    Sifat           = models.CharField(choices=sft, max_length=100, default='Biasa')
    Asal            = models.CharField(max_length=100)
    Nomor           = models.CharField(max_length=100, default='01/KM.1/KNL.0001/2023')
    Isi_Ringkasan   = models.TextField()
    Tujuan          = models.CharField(max_length=100)
    Tanggal         = models.DateField()
    File            = models.FileField(upload_to='dokumen/')
    Keterangan      = models.TextField(default='')

    def __str__(self):
        return self.Kode
        
class SuratKeluar(models.Model):
    Agenda          = models.CharField(max_length=100,default='5001')
    sft = (('Biasa','Biasa'),
        ('Penting','Penting'),
        ('Segera','Segera'),
        ('Sangat Segera','Sangat Segera'),
    )
    Sifat           = models.CharField(choices=sft, max_length=100)
    Tujuan          = models.CharField(max_length=100)
    Nomor           = models.CharField(max_length=100,default='01/KM.1/KNL.0001/2023')
    Isi_Ringkasan   = models.TextField()
    Tanggal         = models.DateField()
    File            = models.FileField(upload_to='dokumen/')
    Keterangan      = models.TextField()

    def __str__(self):
        return self.Agenda
        