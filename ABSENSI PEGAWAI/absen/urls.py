from django.contrib import admin
from django.urls import path,include
from . import views

# gambar/static
from django.conf import settings
from django.conf.urls.static import static

#url/alamat per halaman 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('print/absen/', views.print_absen_data, name='print_absen_data'),
    path('',views.index, name='home'),
    path('akun',views.akun, name='akun'),
    path('absen/',include('absenapp.urls', namespace='absen'  ) ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

