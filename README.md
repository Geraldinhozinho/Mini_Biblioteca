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


2. Upload
2.2. Perguntas
a) O que acontece se esquecermos request.FILES na view?
    
    O Django receberá os outros dados normalmente, mas não receberá o arquivo 
    enviado. Isso acontece por que a imagem não será validada nem processada 
    pelo formulário e se o campo for opcional, o formulário poderá ser enviado 
    sem a imagem, sem necessariamente apresentar um erro.

E se esquecermos o enctype no template?
    O navegador não enviará o arquivo corretamente, vai enviar somente o nome.

Reproduza os dois erros e descreva o que viram (o formulário dá algum aviso?).
    - Esquecer request.FILES
        Os outros campos são recebidos normalmente.
        A imagem não é recebida pelo formulário.

    - Esquecer o enctype
        Os outros campos são enviados normalmente.
        O arquivo não é enviado corretamente pelo navegador.
        O Django recebe request.FILES vazio.


b) Qual é a diferença entre STATICFILES_DIRS / {% static %} e MEDIA_ROOT / .
url? Quando usar cada um na Mini biblioteca?

    STATIC - Servem para utilizar um arquivo estático no template.

    MEDIA - São arquivos enviados durante a utilização do sistema e servem para 
    exibir uma imagem enviada pelo usuário

    STATIC: usa-se para o CSS, JavaScript e possível logotipo da biblioteca.
    MEDIA: usa-se para as capas dos livros cadastradas pelos usuários.
    

c) Ao excluir um livro (ou trocar a capa), o arquivo antigo continua em media/
capas/. Por que isso acontece e que problema pode causar a longo prazo?

    Isso acontece por que o banco de dados armazena o caminho da imagem, mas o 
    arquivo fica separado na pasta Medi de arquivos.

    A longo prazo é um problema por que causa: 
        Acúmulo de arquivos desnecessários.
        Desperdício de espaço em disco.
        Aumento dos custos de armazenamento.
        Dificuldade na organização e manutenção dos arquivos.

d). Por que a extensão do arquivo não basta como proteção? Que outros cuidados 
o servidor deve ter com uploads?
    A extensão não é suficiente porque pode ser facilmente alterada por um 
    usuário mal-intencionado.
        Por exemplo, alguém pode renomear um arquivo executável para imagem.
        jpg, fazendo parecer que é uma imagem, mesmo não sendo.

    Por isso:
        Validar os formatos permitidos
        Gerar nomes únicos
        Armazenar em local seguro
        Utilizar bibliotecas confiáveis
    São camadas outros tipos de proteção desejaveis. 
