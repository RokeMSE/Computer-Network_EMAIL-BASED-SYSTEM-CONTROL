from django.shortcuts import render

import os
import threading

# Create your views here.
def index(request):
    return render(request, 'server/home.html')

def run_EmailServer():
    os.system("python ./server/main/main.py")

def loadServer(request):
    try:
        threading.Timer(1, run_EmailServer).start()
    except:
        pass
    return render(request, 'server/server.html')

def loadClient(request):
    return render(request, 'server/client.html')