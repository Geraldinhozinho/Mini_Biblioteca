from django.contrib import admin
from biblioteca.models import Livro, Author, Category

admin.site.register(Category)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ["titulo","autor", "ano_publicacao", "disponivel"]
    search_fields = ["título", "autor"]
    list_filter = ["disponivel", "categoria"]
    filter_horizontal = ["categoria"]

class LivrosInline(admin.TabularInline):
    model = Livro
    extra = 1

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ["name"]
    inlines = [LivrosInline]
 