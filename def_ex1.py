# Crie uma calculadora simples que possa realizar operações de adição, subtração, multiplicação e divisão. 
# Você vai definir uma função para cada operação e depois perguntar ao usuário qual operação ele deseja realizar.


def somar(a,b):
    return a + b
def subtrair(a,b):
    return a - b
def multiplicar(a,b):
    return a * b
def dividir(a,b):
    return a / b

operador = input('Digite um operador entre +, -, *, /: ')
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

if operador == '+':
    resultado = somar(numero1, numero2)
elif operador == '-':
    resultado = subtrair(numero1, numero2)
elif operador == '*':
    resultado = multiplicar(numero1, numero2)
elif operador == '/':
    resultado = dividir(numero1, numero2)
else:
    print('Operador inválido')

print(f'O resultado é: {resultado}')