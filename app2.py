from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'japonesa')

restaurante_praca.receber_avaliacao('João', 10)
restaurante_praca.receber_avaliacao('Guilherme', 8)
restaurante_praca.receber_avaliacao('Fernanda', 7)

restaurante_japones.receber_avaliacao('Julia', 9)

restaurante_mexicano.receber_avaliacao('Talita', 8)

def main():
    pass

Restaurante.alternar_estado(restaurante_praca)
Restaurante.alternar_estado(restaurante_japones)
Restaurante.listar_restaurantes()



if __name__ == '__main__':
    main()
