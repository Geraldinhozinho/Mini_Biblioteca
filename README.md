# Mini_Biblioteca-
Atividade de pesquisa - Models


autor = models.ForeignKey(Author, related_name="books", null=True, on_delete=models.SET_NULL)

Ao usar o on_delete=models.SET_NULL eu estou fazendo com que caso o model Pai (Author) seja deletado, o model filho (Livro) não é deletado, permanecendo existindo. Porém, é importante observar que o models Livro precisa aceitar null, para quando o author for excluído não quebrar a aplicação por que o valor correpondente a Author foi deletado. 






1 - Que dados se perdem quando a migração é revertida? Por quê?
Os relacionamentos adicionais entre os livros e seus autores que foram 
copiados para o campo mul_autor podem ser perdidos, pois a migração reversa 
não possui uma função para a manipulação dos campos do antigo campo autor. 
Além disso, se o campo antigo já tiver sido removido, os dados originais não
poderão ser recuperados automaticamente, pois o campo antigo deixou de 
existir no esquema atual do banco.


2 - Com ManyToMany, o que acontece com um livro quando o seu único autor é
 apagado? Como garantir que todo livro tenha pelo menos um autor?
Quando o único autor de um livro é apagado, o livro continua existindo, mas 
fica sem autores associados. 
Para garantir que todo livro tenha pelo menos um autor, é necessário 
implementar uma validação na aplicação, por exemplo, nos formulários ou na 
própria lógica de salvamento, impedindo que um livro seja salvo sem autores. 


python manage.py makemigrations biblioteca --empty -n copiar_autores


O que acontece quando essa proteção é removida do template?

O sistema fica vulnerável a ataques de sites maliciosos, fazendo com que o navegador da vítima envie requisições e informações para um outro site que rouba esses dados.

O navegador envia junto os cookies do seu site, então a requisição parece legítima.
Por isso, o CSRF é tão importante para a segurança do sistema. 


PRINT da resposta do navegador ao indentificar a remoção do CSRF:

Proibido (403)
Verificação CSRF falhou. Pedido cancelado.

Help
Reason given for failure:

    CSRF token missing.
    
In general, this can occur when there is a genuine Cross Site Request Forgery, or when Django’s CSRF mechanism has not been used correctly. For POST forms, you need to ensure:

Your browser is accepting cookies.
The view function passes a request to the template’s render method.
In the template, there is a {% csrf_token %} template tag inside each POST form that targets an internal URL.
If you are not using CsrfViewMiddleware, then you must use csrf_protect on any views that use the csrf_token template tag, as well as those that accept the POST data.
The form has a valid CSRF token. After logging in in another browser tab or hitting the back button after a login, you may need to reload the page with the form, because the token is rotated after a login.
You’re seeing the help section of this page because you have DEBUG = True in your Django settings file. Change that to False, and only the initial error message will be displayed.

You can customize this page using the CSRF_FAILURE_VIEW setting.