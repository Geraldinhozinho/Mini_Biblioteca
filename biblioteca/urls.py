from django.urls import path
from .views import listar_livros, author_detail, create_author, create_book
urlpatterns = [
    path('', listar_livros, name="list_books"),
    path('detail/<int:id_A>', author_detail, name="detail_author"),
    path('create_author', create_author, name="create_author"),
    path('create_book', create_book, name="create_book"),
    path('<int:pk>/edit/', create_book, name="edit_book"),



]