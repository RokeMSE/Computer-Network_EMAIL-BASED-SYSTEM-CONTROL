from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('', views.home),
    path('logout', views.logout_view)
]