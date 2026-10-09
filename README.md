# Mini_Biblioteca-
Atividade de pesquisa - Models


autor = models.ForeignKey(Author, related_name="books", null=True, on_delete=models.SET_NULL)

Ao usar o on_delete=models.SET_NULL eu estou fazendo com que caso o model Pai (Author) seja deletado, o model filho (Livro) não é deletado, permanecendo existindo. Porém, é importante observar que o models Livro precisa aceitar null, para quando o author for excluído não quebrar a aplicação por que o valor correpondente a Author foi deletado. 