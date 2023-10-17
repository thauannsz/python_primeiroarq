#inicializa uma lista vazia para armazenar os valores
valores = []

#loop para o usuario digitar os valores
for i in range(5):
    numero = float(input(f'Digite o {i+1}º número: '))
    valores.append(numero)
#calcula a média
media = sum(valores) / len(valores)

#calcula a soma
soma = sum(valores)

#encontra o maior e menor valor
maiorValor = max(valores)
menorValor = min(valores)

#exibe os resultados
print(f'Média dos valores: {media}')
print(f'Soma dos valores: {soma}')
print(f'Maior valor: {maiorValor}')
print(f'Menor valor: {menorValor}')
