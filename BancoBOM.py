class Usuario:
    def __init__(self,name,saldo,key,extrato):
        self.name = name
        self.saldo = saldo
        self.key = key
        self.extrato = extrato

    def deposito(self,quantia):
        if quantia > 0:
            self.saldo += quantia
            self.extrato.append(f"Depósitado: {quantia}")
        else:
            print("Quantia deve ser maior que ZERO")


    def transferencia(self,quantia,destino):
        if self.saldo > 0 and self.saldo >= quantia and quantia > 0:
            for usuario in usuarios:
                if usuario.key == destino:
                    self.saldo -= quantia
                    usuario.saldo += quantia
                    self.extrato.append(f"Transferido: {quantia} para {usuario.name}")
        elif quantia <= 0:
            print("Quantia deve ser maior que ZERO")
        else:
            print("Saldo Insuficiente")


    def saque(self,quantia):
        if self.saldo >= quantia:
            self.saldo -= quantia
            self.extrato.append(f"Saque efetuado de: {quantia}")
        else:
            print("Saldo insuficiente")


usuarios = (
Usuario("Gabriel",100,123,[]),
Usuario("Mick",0,943,[])
)

def obteruser(nome):
    for usuario in usuarios:
        if usuario.name == nome:
            return usuario

gabriel = obteruser("Gabriel")
mick = obteruser("Mick")





print(""" 
Antes""")
print(f"Saldo de Gabriel: {gabriel.saldo}")
print(f"Saldo de mick: {mick.saldo}" )
gabriel.deposito(100)
gabriel.transferencia(100,943)
print(""" 
Depois""")
print(f"Saldo de Gabriel: {gabriel.saldo}")
print(f"Saldo de mick: {mick.saldo}" )
mick.saque(10)
print(""" 
Depois saque""")
print(f"Saldo de Gabriel: {gabriel.saldo}")
print(f"Saldo de mick: {mick.saldo}" )
print(gabriel.extrato)