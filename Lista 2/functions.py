def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero não é permitida."
    return a / b

def potencia(a, b):
    return a ** b

def raiz_quadrada(a):
    if a < 0:
        return "Erro: Raiz quadrada de número negativo não é permitida."
    return a ** 0.5

numeroA = float(input("Digite o primeiro número: "))
numeroB = float(input("Digite o segundo número: "))

print("Soma:", soma(numeroA, numeroB))
print("Subtração:", subtracao(numeroA, numeroB))
print("Multiplicação:", multiplicacao(numeroA, numeroB))
print("Divisão:", divisao(numeroA, numeroB))
print("Potência:", potencia(numeroA, numeroB))
print("Raiz quadrada do primeiro número:", raiz_quadrada(numeroA))
print("Raiz quadrada do segundo número:", raiz_quadrada(numeroB))