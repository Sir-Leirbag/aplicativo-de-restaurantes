from livros.livro import Livro

livro1 = Livro('Entendendo Algoritmos', 'Aditya Y. Bhargava', 2017)
livro2 = Livro('Curso Intensivo de Python', 'Eric Matthes', 2016)
livro3 = Livro('Código Limpo', 'Robert Cecil Martin', 2008)
livro4 = Livro('O Programador Pragmático', 'Andy Hunt e Dave Thomas', 1999)
livro5 = Livro('Designing Data-Intensive Applications', 'Martin Kleppmann', 2017)

livro1.emprestar()

print(Livro.verificar_disponibilidade())
