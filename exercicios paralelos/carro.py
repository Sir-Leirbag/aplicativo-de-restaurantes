class Carro:
    carros = []
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.carros.append(self)

    def listar_carros():
        for carro in Carro.carros:
            print(f'{carro.modelo} | {carro.cor} | {carro.ano}')

carro1 = Carro('Volkswagen Gol GTi', 'Azul Mônaco', 1989)

carro2 = Carro('Fiat Palio Young', 'Amarelo Dourado', 2001)

carro3 = Carro('Chevrolet Corsa Wind', 'Vermelho Stilo', 1996)

carro4 = Carro('Renault Twingo', 'Verde Jade', 1994)

carro5 = Carro('Fiat Bravo Wolverine', 'Branco Kalahari' , 2014)

Carro.listar_carros()