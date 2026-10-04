from django.shortcuts import render
from .models import Livro
# Create your views here.

def listar_livros(request):
    livros = Livro.objects.all()
    contexto = {
        'Livros': livros
    }
    return render(request, 'biblioteca/lista_livros.html',contexto)

