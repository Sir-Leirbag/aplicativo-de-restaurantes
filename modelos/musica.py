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
# musica1.nome = "Don't Look back in anger"
# musica1.artista = 'Oasis'
# musica1.duracao = 287

musica2 = Musica('No Surprises', 'RadioHead', 228)
# musica2.nome = 'No Surprises'
# musica2.artista = 'RadioHead'
# musica2.duracao = 228

musica3 = Musica('Runaway', 'Kanye West', 548)
# musica3.nome = 'Runaway'
# musica3.artista = 'Kanye West'
# musica3.duracao = 548

Musica.listar_musicas()
