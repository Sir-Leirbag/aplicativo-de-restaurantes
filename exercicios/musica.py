class Musica:
    musicas = []
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)
    
    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')

musica1 = Musica("Don't Look back in anger", 'Oasis', 287)

musica2 = Musica('No Surprises', 'RadioHead', 228)

musica3 = Musica('Runaway', 'Kanye West', 548)

Musica.listar_musicas()
print(Musica.musicas)
