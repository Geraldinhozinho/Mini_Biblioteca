from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=120)
    nationality = models.CharField(max_length=200, null=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Author, related_name="books", null=True, on_delete=models.SET_NULL)
    categoria = models.ManyToManyField(Category, null=True)
    ano_publicacao = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.ano_publicacao}"

