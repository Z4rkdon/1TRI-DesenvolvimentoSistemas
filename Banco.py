class  conta:
    def __init__(self, titular, agencia, numero):
        self.__titular = titular
        self.__agencia = agencia
        self.__numero = numero
        self.__saldo = 0

    def extrato(self):
        print(f"O saldo da {self.__titular} é {self.__saldo}")    

    def deposito(self, valor):
        if valor > 0:
           self.__saldo = self.__saldo + valor
           print("Depósito efetuado com sucesso!")
        else:
            print("Não foi póssivel efetuar o depósito")

    def saque(self, valor):
        if valor <= self.__saldo and valor > 0:
            self.__saldo = self.__saldo - valor
            print("Saque efetuado com sucesso!")
        else:
            print("Erro em efetuar o saque")
 
    def transferir(self, conta_destino, valor):
