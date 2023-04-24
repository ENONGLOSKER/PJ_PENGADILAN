from django.contrib import admin
from django.urls import path,include
from . import views

# static
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('detail/',views.detail,name='detail'),
    path('jadwal/',include('jadwal.urls', namespace='jadwal') ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
