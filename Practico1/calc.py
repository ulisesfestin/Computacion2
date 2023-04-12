#!/usr/bin/env python3
import getopt
import sys
  
try:
    opciones, argumentos = getopt.getopt(sys.argv[1:], "o:n:m:")
except getopt.GetoptError:
    print('Uso: python3 calc.py -o <operador> -n <num1> -m <num2>')
    sys.exit()

operador = None
num1 = None
num2 = None

for opt, arg in opciones:
    if opt == '-o':
        operador = arg
    elif opt == '-n':
        num1 = int(arg)
    elif opt == '-m':
        num2 = int(arg)

if not operador or not num1 or not num2:
    print('Uso: python3 calc.py -o <operador> -n <num1> -m <num2>')
    sys.exit()

if operador == '+':
    resultado = num1 + num2
elif operador == '-':
    resultado = num1 - num2
elif operador == '*':
    resultado = num1 * num2
elif operador == '/':
    resultado = num1 / num2
else:
    print("Uso de operador incorrecto")
    sys.exit()

print(f'{num1} {operador} {num2} = {resultado}')


