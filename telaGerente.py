import tkinter as tk
from conta import Conta
import json

def cadastrar():
    conta = Conta(input_titular.get(), input_agencia.get(), input_cpf.get())
    with open("clientes.json", "r") as clientes_arq
      clientes = json.load(clientes_arq)

    clientes_append({
        "titular": conta.titular
        "agencia": conta.agencia
        "numero": conta.numero
        "cpf": conta.cpf
        "saldo": conta.saldo
        "senha:" conta.senha
        "chavepix": conta.chavepix
    })
    with open("clientes.json", "w") as clientes_escritas:
        json.dump(clientes, clientes_escritas, indent=4)
    label_resposta.configure(
        text=f"Conta: {conta.numero} Titulat {conta.titular} cadastrado com sucesso!!!",
        fg="green")

app = tk.Tk()
app.title("Banco Red Dessert")
app.geometry("400x300")

label_senha = 