from django.shortcuts import render, get_object_or_404
from .models import Livro, Author
# Create your views here.

def listar_livros(request):
    livros = Livro.objects.all()
    contexto = {
        'Livros': livros
    }
    return render(request, 'biblioteca/lista_livros.html',contexto)

def author_detail(request, author_id):
    author = get_object_or_404(Author, id = author_id)
    livros = Livro.objects.filter(autor__id = author_id)

    contexto = {
        'Autor': author,
        'Livros': livros
    }

    return render(request, 'biblioteca/author_detail.html',contexto)