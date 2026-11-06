from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro, Author
from .forms import Cadastrar_Autor_Form, Cadastrar_Book_Form
# Create your views here.

def listar_livros(request):
    livros = Livro.objects.all()
    contexto = {
        'Livros': livros
    }
    return render(request, 'biblioteca/lista_livros.html',contexto)

def author_detail(request, id_A):
    author = get_object_or_404(Author, id = id_A)
    livros = Livro.objects.filter(mul_autor__id = id_A)

    contexto = {
        'Autor': author,
        'Livros': livros
    }

    return render(request, 'biblioteca/author_detail.html',contexto)



def create_author(request):
    if request.method == "POST":
        form = Cadastrar_Autor_Form(request.POST)
        if form.is_valid():
            autor = Author(name = form.cleaned_data["name"], nationality=form.cleaned_data["nationality"])
            autor.save()

            return redirect("detail_author", autor.id)  
    else:
        form = Cadastrar_Autor_Form() 
    return render(request, "biblioteca/create_author.html", {"form": form})


def create_book(request):
    if request.method == "POST":
        form = Cadastrar_Book_Form(request.POST)
        if form.is_valid():
            book = Livro(titulo=form.cleaned_data["titulo"], ano_publicacao=form.cleaned_data["ano_publicacao"], disponivel=form.cleaned_data["disponivel"])
            book.save()
            return redirect("lista_livros")
    else:
        form = Cadastrar_Book_Form()
    return render(request, "biblioteca/create_books.html", {"form": form})
