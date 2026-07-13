from modelos.avaliacao import Avaliacao

class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        self._avaliacao = []

        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    def listar_restaurantes():
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo.ljust(25)}')

    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
