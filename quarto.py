class Quarto:
    
    def __init__(self, id, tipo, valor):
        self.id = id
        self.tipo = tipo
        self.__valor = valor
        self.disponivel = True

    def exibir_detalhes(self):
        print(f"Quarto {self.id} - {self.tipo} - {self.__valor} - {self.disponivel}")

    def preservar(self):
        if(self.disponivel == True):
            self.disponivel = False
            print("Quarto reservado com sucesso :3")
        else:
            print("O quarto esta ocupado :(")

    def liberar(self):
        if(self.disponivel == False):
            self.disponivel = True
            print("Quarto liberado com sucesso!!!")
        else:
            print("O quarto já esta livre")

    def alterar_preco(self, novo_valor):
        self.__valor = novo_valor