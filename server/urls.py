from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='loadHome'),
    path('server/', views.loadServer, name='loadServer'),
    path('client/', views.loadClient, name='loadClient'),
    path('get-key-logger/', views.get_key_logger, name='get_key_logger'),
]
