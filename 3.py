# Escreva um programa que leia diversos números inteiros positivos e exiba o dobro de cada um. A leitura deve ser interrompida quando for digitado um número negativo.

numero = 0

for i in range(1000): #loop innfinito
    numero = int(input("digite um número : "))

    if numero < 0:
        print("programa encerrado.")
        break #interrompe o loop
    print("o dobro de", numero, "é : ", numero * 2)