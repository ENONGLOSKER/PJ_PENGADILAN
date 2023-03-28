from django.contrib import admin
from . models import jadwal

# Register your models here.
class jadwalAdmin(admin.ModelAdmin):
    list_display = ('tgl','noPerkara','jenisPerkara','pihak','sidangKeliling','ruangan','agenda','created','updated')
    list_filter = ['tgl','noPerkara','jenisPerkara','pihak','ruangan']

admin.site.register(jadwal,jadwalAdmin)


admin.site.site_header= 'JADWAL SIDANG'