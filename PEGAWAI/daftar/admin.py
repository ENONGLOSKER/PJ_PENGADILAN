from django.contrib import admin
from . models import Pegawaai_PNS, Pegawaai_HONORER

# Register your models here.
class PNSAdmin(admin.ModelAdmin):
    list_display = ('id','nama','NIP','alamat','tgl_lahir','pendidikan','jabatan')
    list_filter = ['nama','NIP','alamat','jabatan']
class HNRAdmin(admin.ModelAdmin):
    list_display = ('id','nama','alamat','tgl_lahir','pendidikan','jabatan')
    list_filter = ['nama','alamat','jabatan']


admin.site.register(Pegawaai_PNS,PNSAdmin)
admin.site.register(Pegawaai_HONORER,HNRAdmin)
