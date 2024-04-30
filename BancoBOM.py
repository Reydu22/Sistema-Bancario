class Usuario:
    def __init__(self,name,saldo,key):
        self.name = name
        self.saldo = saldo
        self.key = key
    def deposito(self,quantia,destino):
        if self.saldo > 0 and self.saldo >= quantia and quantia > 0:
            for usuario in usuarios:
                if usuario.key == destino:
                    self.saldo -= quantia
                    usuario.saldo += quantia
        elif quantia <= 0:
            print("Quantia deve ser maior que ZERO")
        else:
            print("Saldo Insuficiente")

usuarios = [
Usuario("Gabriel",100,123),
Usuario("Mick",0,943)
]

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
gabriel.deposito(100,943)
print(""" 
Depois""")
print(f"Saldo de Gabriel: {gabriel.saldo}")
print(f"Saldo de mick: {mick.saldo}" )
