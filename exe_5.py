idades = []

for i in range(5):
    inserir = int(input('Digite as idades:'))
    idades.append(inserir)
   
maiorValor = max(idades)
menorValor = min(idades)
media = sum(idades) / len(idades)

print('Maior idade registrada', maiorValor)
print('Menor idade registrada', menorValor)
print('Média das idades:', media)