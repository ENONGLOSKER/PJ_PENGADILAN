from django.shortcuts import render
from . models import jadwal

# Create your views here.

def Jadwal(request):
    data = jadwal.objects.all()
    context = {
        'datas':data,
    }
    return render(request,'jadwal.html', context)