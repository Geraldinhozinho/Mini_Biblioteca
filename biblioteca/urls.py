from django.urls import path
from .views import listar_livros, author_detail
urlpatterns = [
    path('', listar_livros, name="lista_livros"),
    path('detail/<int:id_A>', author_detail, name="detail_author")
]