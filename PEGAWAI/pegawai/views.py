from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from daftar . models import Pegawaai_PNS,Pegawaai_HONORER


def index(request):
    return render(request,'index.html')
