from django.urls import path
from . import views

# utntuk menyambungkan/include url pada menu/app dengan project
app_name='absenapp'

#url/alamat per halaman 
urlpatterns =[
    path('',views.absen, name='absen'),
    path('profile/',views.profile, name='profile'),
    path('register/',views.register, name='register'),
    path('login/',views.loginAkun, name='login'),
    path('logoutAkun/',views.logoutAkun, name='logout'),
]
