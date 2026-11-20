
from django.urls import reverse_lazy

from .forms import Cadastrar_Autor_Form, Cadastrar_Book_Form
from .models import Livro, Author

from django.views.generic import ListView, DetailView, CreateView, DeleteView, TemplateView, UpdateView

# Create your views here.

class listar_livros(ListView):
    model = Livro
    template_name = 'biblioteca/list_books.html'
    context_object_name = 'Livros'
    ordering = ['titulo']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_livros'] = Livro.objects.count()
        context['livros_disponiveis'] = Livro.objects.filter(
            disponivel=True
        ).count()
        return context

class author_detail(DetailView):
    model = Author
    template_name = 'biblioteca/author_detail.html'
    context_object_name = 'Autor'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Livros"] = Livro.objects.filter(mul_autor__id=self.object.id)
        return context

class create_author(CreateView):
    model = Author
    form_class = Cadastrar_Autor_Form
    template_name = "biblioteca/create_author.html"
    
    def get_success_url(self):
        return reverse_lazy('detail_author', kwargs={'pk': self.object.pk})
    
class create_book(CreateView):
    model = Livro
    form_class = Cadastrar_Book_Form
    template_name = "biblioteca/create_books.html"
    success_url = reverse_lazy("list_books")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastrar Livro'
        context['botao'] = 'Cadastrar Livro'
        context['author_id'] = None
        return context

class update_book(UpdateView):
    model = Livro
    form_class = Cadastrar_Book_Form
    template_name = 'biblioteca/create_books.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Livro'
        context['botao'] = 'Editar Livro'
        context['author_id'] = self.kwargs.get('author_id')
        return context

    def get_success_url(self):
        author_id = self.kwargs.get('author_id')
        if author_id:
            return reverse_lazy('detail_author', kwargs={'pk': author_id})
        return reverse_lazy('list_books')
     
class delete_book(DeleteView):
    model = Livro
    template_name = 'biblioteca/livro_confirm_delete.html'
    success_url = reverse_lazy('list_books')
    
class sobre(TemplateView):
    template_name = 'biblioteca/sobre.html'