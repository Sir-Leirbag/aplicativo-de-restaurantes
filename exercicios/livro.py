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

    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    def __str__(self):
        return f'nome: {self.nome} | idade: {self.idade} anos | profissão: {self.profissao}'
    
    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}, trabalho com {self.profissao}.'
        else:
            return f'Olá, sou {self.nome}.'
    
    def aniverario(self):
        self.idade += 1

pessoa1 = Pessoa('Gabriel', 23, 'bancário')


pessoa1.aniverario()
print(pessoa1)
print(pessoa1.saudacao)
