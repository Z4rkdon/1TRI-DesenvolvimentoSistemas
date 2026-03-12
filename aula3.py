# menu de opições usado no terminal
while True:
    print("1 - facil")
    print("2 -  médio")
    print("3 - díficio")
    print("4 - imposivel")
    print("5 - sair")

    opcao = input("Digite a opção desejada (1 a 5)")

    if opcao == '1':
        print("Selecionado opção 1")
        tentativas_max = 5
        sorteio_max = 10
    elif opcao == '2':
        print("Selecionado opção 2")
        tentativas_max = 5
        sorteio_max = 25
    elif opcao == '3':
        print("Selecionado opção 3")
        tentativas_max = 4
        sorteio_max = 50
    elif opcao == '4':
        print("Selecionado opção 4")
        tentativas_max = 3
        sorteio_max = 90
    elif opcao == '5':
        print("Selecionado sair")
        break
    else:
        print("Opção Incorreta")
        


    import random
    tentativas = 1
    numero = random.randint(0,sorteio_max)
    errou = True

        
    while (tentativas <= tentativas_max):
        print("Tentativa:, {tentativas}")
        chute = int(input("Digite o seu chute (0 a 10):"))
        if chute == numero:
            print("Parabéns, você é o bonzão mesmo :)")
            errou = False
            break
        else:
            print("Errou :c")
        tentativas = tentativas + 1
        
    if errou == True:
        print("O número sorteado era:", numero) # mostra p quem errou
    print("### FIM DO JOGO ###")
    

   
