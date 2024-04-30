login = None
msgmenu = """ 
[d] Depositar
[s] Sacar 
[t] Transferir
[e] Extrato
[bah] Sair
"""
class Usuario:
    def __init__(self,name,saldo,key,extrato):
        self.name = name
        self.saldo = saldo
        self.key = key
        self.extrato = extrato

    def deposito(self,quantia):
        if quantia > 0:
            self.saldo += quantia
            self.extrato += f"Depósitado: {quantia}\n"
        else:
            print("Quantia deve ser maior que ZERO")


    def transferencia(self,quantia,destino):
        if self.saldo > 0 and self.saldo >= quantia and quantia > 0:
            for usuario in usuarios:
                if usuario.key == destino:
                    self.saldo -= quantia
                    usuario.saldo += quantia
                    self.extrato += f"Transferido: {quantia} para {usuario.name}\n"
        elif quantia <= 0:
            print("Quantia deve ser maior que ZERO")
        else:
            print("Saldo Insuficiente")


    def saque(self,quantia):
        if self.saldo >= quantia:
            self.saldo -= quantia
            self.extrato += f"Saque efetuado de: {quantia}\n"
            print(self.extrato)
        else:
            print("Saldo insuficiente")


usuarios = (
Usuario("Gabriel",100,123,""),
Usuario("Mick",0,943,"")
)

def obteruser(nome):
    for usuario in usuarios:
        if usuario.name == nome:
            return usuario

gabriel = obteruser("Gabriel")
mick = obteruser("Mick")


while True:
    if login != None:
        menu = msgmenu
        opcao = input(menu)
        
        if opcao == "d":
            menu = "Digite o valor do deposito: "
            valor =  int(input(menu))
            if valor > 0:
                login.deposito(valor)
        elif opcao == "s":
            menu = "Digite o valor do saque: "
            valor =  int(input(menu))
            if valor > 0:
                login.saque(valor)
        elif opcao == "t":
            menu = "Digite o valor da transferencia: "
            valor =  int(input(menu))
            menu = "Digite a chave do destinatario: "
            chave = int(input(menu))
            if valor > 0:
                login.transferencia(valor,chave)
        elif opcao == "e":
           print(login.extrato)
        elif opcao == "bah":
            break
    else:
        menu = "Digite seu Nome: "
        login = obteruser(input(menu))