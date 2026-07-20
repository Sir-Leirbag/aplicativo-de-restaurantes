class Livro:

    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f'{self._titulo} | {self._autor} | {self._ano_publicacao} | disponível: {self._disponivel}'

    def emprestar(self):
        self._disponivel = False

    @staticmethod
    def verificar_disponibilidade():
        ano = int(input('Digite o ano que deseja: '))
        print('Livros disponívies:')
        livros_disponiveis = [str(livro) for livro in Livro.livros if livro._disponivel and livro._ano_publicacao == ano]
        return livros_disponiveis
