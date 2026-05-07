#Escreva um programa que leia um número inteiro positivo (n > 1) e imprima os seus divisores.
num = int(input("digite um número inteiro: "))

if num > 1:
    print(f"os divisores de {num} são: ")
    contador = 0
    for i in range(1, num + 1):
        if num % i == 0 :  # o "i" é uma variavel que vai pecorrer todos os numeros dentro do intervalo de range.
            print(i)
            contador += 1

    if contador == 2:
        print(f"{num} é um número primo. ")
else:
    print("o número deve ser maior que 1.")