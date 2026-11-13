from django import forms

from .models import Author, Category, Livro

class Cadastrar_Autor_Form(forms.Form):
    name = forms.CharField(label="Autor", max_length=20, required=True)
    nationality = forms.CharField(label="Nacionalidade", max_length=20, required=False)


class Cadastrar_Book_Form(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'mul_autor', 'categoria', 'ano_publicacao', 'disponivel']
        labels = {
            'titulo': 'Título',
            'mul_autor': 'Autor(es)',
            'categoria': 'Categoria(s)',
            'ano_publicacao': 'Ano de Publicação',
            'disponivel': 'Disponível',
        }
        widgets = {
            'mul_autor': forms.CheckboxSelectMultiple(),
            'categoria': forms.CheckboxSelectMultiple(),
        }
        #Espaços sobrando no começo, no fim e repetidos no meio são removidos antes de salvar. Depois da limpeza, o título precisa ter pelo menos 3 caracteres.
    def clean_titulo(self):
        titulo = ' '.join(self.cleaned_data.get('titulo', '').split())

        if len(titulo) <= 3:
            raise forms.ValidationError(
                "O título deve ter pelo menos 3 caracteres."
            )

        return titulo