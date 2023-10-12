tentativa = 0

while tentativa < 3:
    senha = str(input("Digite sua senha:")) 
    tentativa = tentativa + 1
    if senha == 'Proz@2022':
        print("Senha correta!")
        break
    elif senha != 'Proz@2022':
        print('Senha incorreta.')
if tentativa == 3:
    print("Número de tentativas atingido, conta bloqueada!")


    

