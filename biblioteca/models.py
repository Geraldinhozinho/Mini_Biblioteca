

from datetime import timezone

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator


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
    titulo = models.CharField(max_length=200, validators=[MinLengthValidator(3)])
    mul_autor = models.ManyToManyField(Author, related_name="books2")
    categoria = models.ManyToManyField(Category, null=True, blank=True)
    ano_publicacao = models.IntegerField(validators=[MinValueValidator(1450), MaxValueValidator(timezone.now().year)])
    disponivel = models.BooleanField(default=True)
    paginas = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5000)])
    isbn = models.CharField(max_length=13, unique=True, validators=[MinLengthValidator(13)])
    
    
    def __str__(self):
        return f"{self.titulo} - {self.mul_autor} - {self.ano_publicacao}"

