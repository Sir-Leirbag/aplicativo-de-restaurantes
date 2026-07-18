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

    def verificar_disponibilidade():
        ano = int(input('Digite o ano que deseja: '))
        print('Livros disponívies:')
        for livro in Livro.livros:
            if livro._disponivel and livro._ano_publicacao == ano:
                print(livro)

livro1 = Livro('Entendendo Algoritmos', 'Aditya Y. Bhargava', 2017)
livro2 = Livro('Curso Intensivo de Python', 'Eric Matthes', 2016)
livro3 = Livro('Código Limpo', 'Robert Cecil Martin', 2008)
livro4 = Livro('O Programador Pragmático', 'Andy Hunt e Dave Thomas', 1999)
livro5 = Livro('Designing Data-Intensive Applications', 'Martin Kleppmann', 2017)

livro1.emprestar()

Livro.verificar_disponibilidade()
