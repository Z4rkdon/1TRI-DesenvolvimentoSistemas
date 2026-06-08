import tkinter as tk
from conta import Conta
import json

def login():
    if input_titular.get() == "admin":
        if input_agencia.get() == "1234":
            if input_cpf.get() == "6789":
                label_resposta.configure(text="Login realizado com sucesso!!", fg="green")
            else:
                label_resposta.configure(text="Falha no login", fg="red")
        else:
            label_resposta.configure(text="Falha no login", fg="red")
    else:
        label_resposta.configure(text="Falha no login", fg="red")

def cadastrar():
    conta = Conta(input_titular.get(), input_agencia.get(), input_cpf.get())
    print(conta.extrato())
    print(conta.numero)

    with open("clientes.json", "r") as clientes_arq:
        clientes = json.load(clientes_arq)

    clientes.append({
        "titular": conta.titular,
        "agencia": conta.agencia,
        "numero": conta.numero,
        "cpf": conta.cpf,
        "saldo": conta.saldo,
        "senha": conta.senha,
        "chavepix": conta.chavepix
    })
    
    with open("clientes.json", "w") as clientes_escritas:
        json.dump(clientes, clientes_escritas, indent=4)
        
    label_resposta.configure(
        text=f"Conta: {conta.numero} Titular {conta.titular} cadastrado com sucesso!!!",
        fg="green")

app = tk.Tk()
app.title("Banco Red Dessert")
app.geometry("400x400") 

label_titular = tk.Label(app, text="titular:")
label_titular.pack(pady=5)
input_titular = tk.Entry(app)
input_titular.pack()


label_agencia = tk.Label(app, text="agência:")
label_agencia.pack(pady=5)
input_agencia = tk.Entry(app)
input_agencia.pack()

label_cpf = tk.Label(app, text="cpf:")
label_cpf.pack(pady=5)
input_cpf = tk.Entry(app)
input_cpf.pack()


botao_cadastrar = tk.Button(app, text="Cadastrar", command=cadastrar)
botao_cadastrar.pack(pady=5)

botao_login = tk.Button(app, text="Login", command=login)
botao_login.pack(pady=5)

label_resposta = tk.Label(app, text="")

label_resposta.pack(pady=5)

app.mainloop()
