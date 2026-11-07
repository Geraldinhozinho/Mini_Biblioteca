from django import forms

from .models import Author, Category

class Cadastrar_Autor_Form(forms.Form):
    name = forms.CharField(label="Autor", max_length=20, required=True)
    nationality = forms.CharField(label="Nacionalidade", max_length=20, required=False)


class Cadastrar_Book_Form(forms.Form):
    titulo = forms.CharField(max_length=200)
    mul_autor = forms.ModelMultipleChoiceField(queryset=Author.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    categoria = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    ano_publicacao = forms.IntegerField()
    disponivel = forms.BooleanField(required=False)