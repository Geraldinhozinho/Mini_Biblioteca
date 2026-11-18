# Mini_Biblioteca-
Class-Based Views

1.2. Perguntas
a) O LivroModelForm mudou? Por que as regras do Model 
funcionam nele e no Admin sem nenhuma alteração?

Não mudou nada no LivroModelForm. Não precisou mudar por que no ModelForm o Django 
utiliza os validadores definidos no próprio Model automaticamente. Além disso,
o Django também aplica essas validações automaticamente no Admin, pois ele utiliza os formulários baseados nos Models.

b) Os validator são funções independentes aplicadas em um campo e 
recebem valor para verificar se ele atende a determinada regra. se não atender, lança uma exceção ValidationError.

O clean_<campo>() é um método definido dentro do formulário que permite validar e 
modificar o valor de um campo específico antes de salvar.
    Ex:
    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        return titulo.strip()

c) 
O título não pode ser igual ao nome do autor.
    clean() -> É usado quando é preciso tratar dois campos ou mais

O título deve ser salvo sem espaços no início e no fim.
    clean_titulo() -> Permite tratar e modificar especificamente o valor de um campo
    especifico.

O número de páginas deve ser no máximo 5000.
    validators=[...] -> É uma validação simples, que verifica se o valor não 
    ultrapassa um limite.

Um livro "indisponível" precisa ter o ISBN preenchido.
    clean() -> 	por que é necessário verificar a relação entre dois campos: disponibilidade e 
    ISBN.