import random
class  Conta:
    def __init__(self, titular, agencia, numero, cpf):
        self.__titular = titular
        self.__agencia = agencia
        self.__numero = f"{random.randint(1000, 9999)}-{random.randint(1,9)}"
        self.__cpf = cpf
        self.__saldo = 0
        self.__senha = random.randint(777777, 333333)
        self.__chavepix = []

    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self, novo_nome):
        self.__titular = novo_nome
    @property
    def agencia(self):
        return self.__agencia
    @property
    def numero(self):
        return self.__numero
    @property
    def cpf(self):
        return self.__cpf
    @property
    def saldo(self):
        return self.__saldo
    @property
    def chavepix(self):
        return self.__chavepix


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
        self.__saldo -= valor
        conta_destino.__saldo += valor
