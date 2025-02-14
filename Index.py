#Bibliotecas
from dispertador import Dispertador

#VARIAVEIS
user = ""
hora = 0
minuto = 0
segundo = 0

#CODIGO PRINCIPAL
print(f"Bem vindos ao meu Dispertador Pessoal ou PD")
dispertador = Dispertador()

while True:
    user = dispertador.menu()
    if user == "1":
        print(dispertador.mostrarHora())
    elif user == "2":
        hora = int(input("Digite a hora: "))
        minuto = int(input("Digite o minuto: "))
        segundo = int(input("Digite o segundo: "))
        dispertador.ajustarHora(hora, minuto, segundo)

    elif user == "3":
        print(f"Deseja ver algo separado como: hora ou segundo?")
        print(f"Digite \n1 - hora \n2 - minuto \n3 - segundo")
        user = input("R: ")
        if user == "1":
            print(dispertador.getHora())
        elif user == "2":
            print(dispertador.getMinuto())
        elif user == "3":
            print(dispertador.getSegundo())
    elif user == "4":
        print("Obrigado por usar o PD\nSaindo...")  
        break
    else:
        print("Opção inválida, tente novamente\n")
        continue
