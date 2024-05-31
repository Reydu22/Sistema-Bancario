login = None
msgmenu = """ 
[d] Depositar
[s] Sacar 
[t] Transferir
[e] Extrato
[saldo] Ver Saldo
[sair] Sair
"""

msgmenucriar =  """
[c] Criar Conta
[l] Logar
"""

usuarios = [

]

class Usuario:
    def __init__(self,name,senha,cpf,saldo,extrato,numerosaque):
        self.name = name
        self.senha = senha
        self.cpf = cpf
        self.saldo = saldo
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
                if usuario.cpf == str(destino):
                    print("é")
                    self.saldo -= quantia
                    usuario.saldo += quantia
                    self.extrato += f"Transferido: {quantia} para {usuario.name}\n"
        elif quantia <= 0:
            print("Quantia deve ser maior que ZERO")
        else:
            print("Saldo Insuficiente")


    def saque(self,quantia):
        if self.saldo >= quantia and self.numerosaque < 3:
            self.saldo -= quantia
            self.extrato += f"Saque efetuado de: {quantia}\n"
            self.numerosaque += 1
        else:
            print("Saldo insuficiente")
        
    def saldover(self):
        print(self.saldo)

def obteruser(nome):
    for usuario in usuarios:
        if usuario.name == nome:
            return usuario

def checarcpf(bah):
    for usuario in usuarios:
        if usuario.cpf == bah:
            return 
        else: 
            return True
        
def checarsenha(nome,senhaa):
    usuario = obteruser(nome)
    if usuario.senha == senhaa:
        return True
    else:
        return

def criarconta():
    menu = "Digite seu nome: "
    nome = input(menu)
    menu = "Digite sua senha: "
    senha = input(menu)
    menu = "Digite seu cpf: "
    cpf = input(menu)        
    numerodousuario = len(usuarios) + 1
    numerodousuario = Usuario(nome,senha,cpf,0,"",0)
    usuarios.append(numerodousuario)
    return nome

def logar():
    menu = "Digite seu nome: "
    nome = input(menu)
    menu = "Digite sua senha: "
    senha = input(menu)
    if obteruser(nome) != None:
        if checarsenha(nome,senha):
            return nome
    print("Senha ou Nome Invalidos")
    return

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
        elif opcao == "saldo":
           login.saldover()
        elif opcao == "sair":
            login = None
    else:
        menu = msgmenucriar
        opcao = input(menu)
        if opcao == "c":
           print(usuarios)
           nome = criarconta()
           login = obteruser(nome)
        elif opcao == "l":
            nome = logar()
            login = obteruser(nome)