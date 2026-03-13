palavra = "HILDA"
letras_acertadas = ["_", "_", "_", "_", "_"]
acertou = False

def mostrar_letras_acertadas():
    for letra in letras_acertadas:
        print(letra, end=" ")

print("Tente adivinhar a palavra secreta: ") 
while(not acertou):
    mostrar_letras_acertadas()
    
    print("")
    chute = input("Digite uma letra: ")
    indice = 0
    for letra in palavra:
        if chute.upper() == letra:
            letras_acertadas[indice] = letra
        indice = indice + 1

    if letras_acertadas.count("_") == 0:
        print("Parabéns, você acertou a palavra secreta!")
        mostrar_letras_acertadas()
        acertou = True



        