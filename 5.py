for i in range(1000): #loop infinito
   km = float(input("Digite a distância percorrida em km: "))
   tempo = float(input("Digite o tempo gasto em horas: "))
   velocidade = km / tempo
   print("A velocidade média é : ", velocidade, "km/h")

   continuar = input("Deseja continuar usando o programa? (sim ou não) : ").lower()

   if continuar == "não" or continuar == "nao":
      break