login = None
msgmenu = """ 
[d] Depositar
[s] Sacar 
[t] Transferir
[e] Extrato
[bah] Sair
"""
class Usuario:
    def __init__(self,name,saldo,key,extrato,numerosaque):
        self.name = name
        self.saldo = saldo
        self.key = key
        self.extrato = extrato
        self.numerosaque = numerosaque

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
            self.numerosaque += 1
        else:
            print("Saldo insuficiente")


usuarios = (
Usuario("Gabriel",100,123,"",0),
Usuario("Mick",0,943,"",0)
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
            valor =  float(input(menu))
            if valor > 0:
                login.deposito(valor)
        elif opcao == "s":
            menu = "Digite o valor do saque: "
            valor =  float(input(menu))
            if valor > 0:   
                if login.numerosaque < 3:
                    login.saque(valor)
                else:
                    print("Numero de saques diarios excedido")
        elif opcao == "t":
            menu = "Digite o valor da transferencia: "
            valor =  float(input(menu))
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