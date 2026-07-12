class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False #Atributo protegido

    def __str__(self):
        return f'Titular: {self.titular} | Saldo: R$ {self.saldo} | Ativo: {self.ativo}'
    
    def ativar_conta(self):
        self.ativo = True

conta1 = ContaBancaria('Mateus', 41587.54)
conta2 = ContaBancaria('João', 5247.45)

conta1.ativar_conta()

print(conta1)
print(conta2)