from django.shortcuts import render
from .models import Usuario
def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('Idade')
    novo_usuario.save()

    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request,'usuarios/usuarios.html',usuarios)

from django.db import connection

def delete_database(request):
    Usuario.objects.all().delete()
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='app_cad_usuario_usuario'")
    return render(request,'usuarios/usuarios.html')