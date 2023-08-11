nome = 'Nicole Souza'
altura = 1.52
peso = 45
imc = peso / (altura ** 2)

# f-strings
# podemos formatar as linhas utilizando o 'f'
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é {imc}'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
