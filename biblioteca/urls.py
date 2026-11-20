from django.urls import path
from .views import delete_book, listar_livros, author_detail, create_author, create_book, sobre, update_book
urlpatterns = [
    path('', listar_livros.as_view(), name="list_books"),
    path('detail/<int:pk>', author_detail.as_view(), name="detail_author"),
    path('create_author', create_author.as_view(), name="create_author"),
    path('create_book', create_book.as_view(), name="create_book"),
    path('delete/<int:pk>/', delete_book.as_view(), name="delete_book"),
    path('<int:pk>/edit/', update_book.as_view(), name="edit_book"),
    path('<int:pk>/<int:author_id>/edit/', update_book.as_view(), name='edit_book_author'),
    path('sobre/', sobre.as_view(), name='sobre'),
]