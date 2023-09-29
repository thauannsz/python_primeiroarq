nome = str(input("Digite seu nome: "))
sobrenome = input("\nDigite seu sobrenome: ")

print("\nTipo da variavel nome:", type(nome))
print("Tipo da variavel sobrenome", type(sobrenome))
print(f"Nome e Sobrenome: {nome} {sobrenome}")
print("O numero de letras do nome eh:", len(nome))
print("O numero de letras do sobrenome eh:", len(sobrenome))
print("A primeira letra do nome eh:", nome[0])
print("A ultima letra do nome eh:", nome[-1])
#-1 sempree vai mostrar o ultimo elemento
print("As 3 primeiras letras:", nome[0:3])
#o ultimo numero n conta

#"\n" QUEBRA A LINHA
#"f" MOSTRA AS VARIAVEIS QUE ESTAO DENTRO DE CHAVES {}
#"len" MOSTRA A QUANTIDADE DE ALGO(COMPRIMENTO)