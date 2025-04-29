#Exercício 2 - CHECKPOINT2

print("=== CLASSIFICADOR DE TRIANGULARES ===")

# Lados do triangular
a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))

print()

#Ordena os lados em ordem decrescente
if b > a and b > c:
    a, b = b, a
elif c > a and c > b:
    a, c = c, a

#Verifica a forma do triangular
if a >= b + c:
    print("NÃO FORMA UM TRIÂNGULO")
else:
    if a**2 == b**2 + c**2:
        print("TRIÂNGULO RETÂNGULO")
    elif a**2 > b**2 + c**2:
        print("TRIÂNGULO OBTUSÂNGULO")
    else:
        print("TRIÂNGULO ACUTÂNGULO")

    if a == b == c:
        print("TRIÂNGULO EQUILÁTERO")
    elif a == b or b == c or a == c:
        print("TRIÂNGULO ISÓSCELES")