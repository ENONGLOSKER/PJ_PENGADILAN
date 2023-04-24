from django.contrib import admin
from django.urls import path
from .import views
# static
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/',views.LoginPage,name='login'),
    path('register/',views.SignupPage,name='register'),
    path('logout/',views.LogoutPage,name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

