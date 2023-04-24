from django.contrib import admin
from . models import jadwal

# Register your models here.
class jadwalAdmin(admin.ModelAdmin):
    list_display = ('tgl','noPerkara','jenisPerkara','penggugat','tergugat','sidangKeliling','ruangan','agenda','created','updated')
    list_filter = ['tgl','noPerkara','jenisPerkara','penggugat','tergugat','ruangan']

admin.site.register(jadwal,jadwalAdmin)


admin.site.site_header= 'JADWAL SIDANG'