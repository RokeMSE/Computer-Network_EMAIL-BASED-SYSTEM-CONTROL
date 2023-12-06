from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='loadHome'),
    path('server/', views.loadServer, name='loadServer'),
    path('client/', views.loadClient, name='loadClient'),
    path('about/', views.loadAbout, name='loadAbout'),
    path('get-key-logger/', views.get_key_logger, name='get_key_logger'),
    path('get-list-apps/', views.get_list_apps, name='get_list_apps'),
    path('get-list-processes/', views.get_list_processes, name='get_list_processes'),
]
