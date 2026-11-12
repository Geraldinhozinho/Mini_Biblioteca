from django import forms

from .models import Author, Category, Livro

class Cadastrar_Autor_Form(forms.Form):
    name = forms.CharField(label="Autor", max_length=20, required=True)
    nationality = forms.CharField(label="Nacionalidade", max_length=20, required=False)


class Cadastrar_Book_Form(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'mul_autor', 'categoria', 'ano_publicacao', 'disponivel']
        widgets = {
            'mul_autor': forms.CheckboxSelectMultiple(),
            'categoria': forms.CheckboxSelectMultiple(),
        }