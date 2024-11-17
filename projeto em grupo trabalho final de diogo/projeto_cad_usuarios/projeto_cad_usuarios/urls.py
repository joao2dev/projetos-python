
from django.contrib import admin
from django.urls import path
from app_cad_usuario import views
urlpatterns = [
    path('', views.home, name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuario'),
    path('delete/', views.delete_database, name='delete_database')
]