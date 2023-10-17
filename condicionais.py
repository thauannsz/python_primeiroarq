#condicional simples:

#nota = int(input('Digite a nota:'))

#if nota == 10:
#   print('Excelente!')
#elif nota <= 5:
#   print('Péssimo!')
#else:
#   print('Bom!')

#condicional composta:

idade = int(input('Digite sua idade:'))
sexo = input('Digite o sexo M ou F:').lower()

if idade < 18 and sexo == 'm':
    print('homem menor de idade')
elif idade >= 18 and sexo == 'm':
    print('homem maior de idade')
elif idade < 18 and sexo == 'f':
    print('mulher menor de idade')
elif idade >= 18 and sexo == 'f':
    print('mulher maior de idade')
else:
    print('Erro na entrada de dados')
