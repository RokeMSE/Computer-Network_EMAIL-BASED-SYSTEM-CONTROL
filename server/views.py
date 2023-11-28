from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

import os
import threading

def load_home(request):
    return render(request, 'home.html')

def run_Emailserver():
    os.system("python .\\server\\main\\main.py")

def server_login(request):
    try:
        threading.Timer(1, run_Emailserver).start()
    except:
        pass
    return render(request, 'server.html')


def client_login(request):

    return render(request, 'client.html')






# Create your views here.
