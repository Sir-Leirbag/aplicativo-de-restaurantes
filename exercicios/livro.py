class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True

    def __str__(self):
        return f'{self._titulo} | {self._autor} | {self._ano_publicacao}'

livro1 = Livro('Entendendo Algoritmos', 'Aditya Y. Bhargava', 2017)
livro2 = Livro('Curso Intensivo de Python', 'Eric Matthes', 2016)

print(livro1)
print(livro2)
