from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'japonesa')

def main():
    pass

Restaurante.alternar_estado(restaurante_praca)
Restaurante.alternar_estado(restaurante_japones)
Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()
