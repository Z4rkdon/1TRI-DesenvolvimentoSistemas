import tkinter as tk

def login():
    print("Login realizado")

app = tk.Tk()
app.title("Tela Exemplo :3")
app.geometry("400x300")

label1_email = tk.Label(app, text="Email:")
label1_email.pack(pady=5)
input_email = tk.Entry(app)
input_email.pack()


label1_senha = tk.Label(app, text="Senha:")
label1_senha.pack(pady=5)
input_senha = tk.Entry(app, show="*")
input_senha.pack()

botao = tk.Button(app, text="Enviar", command=login)
botao.pack(pady=10)

label1_resposta = tk.label1(app, text="")


    
app.mainloop()