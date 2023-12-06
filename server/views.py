from django.shortcuts import render

import os
import threading
from django.http import JsonResponse

def read_from_file(fileName):
    with open(fileName, 'r', encoding='utf-8') as file:
        return file.read().strip()



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
    return render(request, template_name='server/client.html')
        # 'list_processes': list_processes()

def loadAbout(request):
    return render(request, 'server/about.html')


def get_key_logger(request):
    key_string_global =  read_from_file("variable.txt")
    # Consider importing this variable from its source
    return JsonResponse({'key_logger': key_string_global})

def get_list_apps(request):
    list_apps = read_from_file("list_apps.json")
    return JsonResponse({'list_apps': list_apps})

def get_list_processes(request):
    list_processes = read_from_file("list_processes.json")
    return JsonResponse({'list_processes': list_processes})