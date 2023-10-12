while True :
    try:
        print ("Digite 1 para: Alugar um imóvel ")
        print ("Digite 2 para: Comprar um imóvel")
        print ("Digite 3 para: Falar com um corretor")
        print ("Digite 4 para: Falar com o setor jurídico")

        opcao = int (input('\n'"Insira um numero correspondente a opção que deseja:"))
        if opcao == 1:
            print("Abrindo atendimento para alugar um imóvel.")
            break
        elif opcao == 2:
            print("Abrindo atendimento para comprar um imóvel.")
            break
        elif opcao == 3:
            print ("Um corretor irá de chamar em breve.")
            break
        elif opcao == 4:
            print ("O setor jurídico irá te retornar.")
            break
        else:
            print ('\n'"Digite uma opção valida.")
    except ValueError:
        print ("Digite uma opção valida ao menu.")
