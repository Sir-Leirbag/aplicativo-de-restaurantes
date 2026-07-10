# class Livro:
#     def __init__(self, titulo, autor, paginas):
#         self.titulo = titulo
#         self.autor = autor
#         self.paginas = paginas

#     def __str__(self):
#         return f'{self.titulo} por {self.autor} - {self.paginas} páginas.'
        
#     @property
#     def titulo_autor(self):
#         return f'{self.titulo} por {self.autor}'
    
#     def aumentar_paginas(self):
#         self.paginas += quantidade

class Pessoa:

    pessoas = []

    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self._sindicalizado = False
        Pessoa.pessoas.append(self)
    
    def __str__(self):
        return f'nome: {self.nome} | idade: {self.idade} anos | profissão: {self.profissao} | {self._sindicalizado}'
    
    def aniverario(self):
        self.idade += 1

    def listar_pessoas():
        for pessoa in Pessoa.pessoas:
            print(f'{pessoa.nome} | {pessoa.sindicalizado}')
    
    @property
    def sindicalizado(self):
        return 'v' if self._sindicalizado else 'x'

pessoa1 = Pessoa('Gabriel', 23, 'bancário')

# Pessoa.listar_pessoas()
for pessoa in Pessoa.pessoas:
    print(pessoa)
