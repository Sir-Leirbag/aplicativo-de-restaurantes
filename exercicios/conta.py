class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False #Atributo protegido

    def __str__(self):
        return f'Titular: {self.titular} | Saldo: R$ {self.saldo} | Ativo: {self.ativo}'
    
    def ativar_conta(self):
        self._ativo = True

    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'

class ClienteBanco:
    def __init__(self, nome, idade, sexo, cidade, profissao):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.cidade = cidade
        self.profissao = profissao

    def __str__(self):
        return f'Nome: {self.nome} | Idade: {self.idade} anos | \
Sexo: {self.sexo} | Cidade: {self.cidade} | Profissão: {self.profissao} | '

conta1 = ContaBancaria('Mateus', 41587.54)
conta2 = ContaBancaria('João', 5247.45)
cliente1 = ClienteBanco('Mateus', 27, 'masculino', 'São Paulo', 'Jornalista')
cliente2 = ClienteBanco('João', 32, 'masculino', 'Rio de Janeiro', 'Advogado')


conta1.ativar_conta()

print(conta1)
print(conta2)
print(cliente1)
print(cliente2)