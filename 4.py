r1 = 0 #regular
r2 = 0 #bom
r3 = 0 #ótimo

resposta = input("Qual sua opinião sobre o filme? (3 - ótimo, 2 - bom, 1 - regular) : ")

for i in range(15):
    resposta = input("Qual sua opinião sobre o filme? (3 - ótimo, 2 - bom, 1 - regular) : ")
    if resposta == "3":
       r3 += 1
       print ("obrigado pela sua opinião.")

    elif resposta == "2":
        r2 += 1
        print ("obrigado pela sua opinião.")

    elif resposta == "1":
        r1 += 1
        print ("obrigado pela sua opinião.")

print("A quantidade de pessoas que responderam Ótimo: ", r3)
print("A quantidade de pessoas que responderam Bom: ", r2)
print("A quantidade de pessoas que responderam Regular: ", r1)