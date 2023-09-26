while True:
    numero_usuario_1 = input("Insira um numero: ")
    numero_usuario_2 = input("Insira um segundo numero :")
    numeros_validos = None
    try:
        numero_usuario_1_INT = int(numero_usuario_1)                    # Conversao dos dados do usuario para Int
        numero_usuario_2_INT = int(numero_usuario_2)                    #
        numeros_validos = True
    except:
        numeros_validos = None

        if numeros_validos is None:
            print("Um ou ambos digitos inseridos sao invalidos!")

            break


    operacao = input("Insira a operaçao que deseja fazer (+, *, - ou /): ")

    if operacao == "+":
        resposta =  numero_usuario_1_INT + numero_usuario_2_INT

        print(resposta)

    if operacao == "*":
        resposta = numero_usuario_1_INT * numero_usuario_2_INT

        print(resposta)

    if operacao == "-":
        resposta = numero_usuario_1_INT - numero_usuario_2_INT

        print(resposta)

    if operacao == "/":
        resposta = numero_usuario_1_INT / numero_usuario_2_INT

        print(resposta)
     
    saida =input("Deseja Sair? [S] [N]")  # possibilidade de saida do usuario 
    saida_usada = saida.upper()
    

    if saida_usada == "S" :
        print("Sair")
        break
    elif saida_usada == "N":
        continue
