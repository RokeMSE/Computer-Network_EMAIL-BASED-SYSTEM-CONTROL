from django.urls import path
from . import views

urlpatterns = [
    path("", views.load_home, name='home'),
    path('server/', views.server_login, name='server'),
    path('client/', views.client_login, name='client'),
]