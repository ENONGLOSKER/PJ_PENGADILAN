from django.contrib import admin
from django.urls import path
from . import views
# static
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('print/masuk/', views.print_surat_masuk_data, name='print_surat_masuk_data'),
    path('print/keluar/', views.print_surat_keluar_data, name='print_surat_keluar_data'),
    path('admin/', admin.site.urls),
    path('',views.index, name='home'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
