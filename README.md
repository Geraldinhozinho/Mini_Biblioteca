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