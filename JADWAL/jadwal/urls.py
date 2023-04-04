from django.urls import path
from . import views
app_name='jadwal'
urlpatterns = [
    path('', views.Jadwal, name='sidang'),
] 