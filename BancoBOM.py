class Usuario:
    def __init__(self,name,saldo,key):
        self.name = name
        self.saldo = saldo
        self.key = key
    def deposito(self,quantia,destino):
        if self.saldo > 0 and self.saldo >= quantia and quantia > 0:
            self.saldo -= quantia
        elif quantia <= 0:
            print("Quantia deve ser maior que ZERO")
        else:
            print("Saldo Insuficiente")
        for Usuario in usuarios:
            if Usuario.key == destino:
                return Usuario
                

usuarios = [
Usuario("Gabriel",0,123),
Usuario("Miley",0,943)
]

def obteruser(nome):
    for usuario in usuarios:
        if usuario.name == nome:
            return usuario

gabriel = obteruser("Gabriel")
miley = obteruser("Miley")

print(gabriel.saldo)

gabriel.saldo  += 100

print(gabriel.saldo)