from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='loadHome'),
    path('server/', views.loadServer, name='loadServer'),
    path('client/', views.loadClient, name='loadClient'),
]
