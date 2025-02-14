#Bibliotecas
import datetime
#Classes
class Dispertador:


    #Funções do dispertador
    #Adicionar o parametro self
    def __init__(self):
        self.__hora = datetime.datetime.now().hour
        self.__minuto = datetime.datetime.now().minute
        self.__segundo = datetime.datetime.now().second

    def menu(self):
        print("Digite a opção desejada:\n")
        print("1 - Mostrar Hora\n")
        print("2 - Ajustar Hora\n")
        print("3 - Mostrar separado\n")
        print("4 - Sair\n")
        while True:
            opcao = input("R: ")
            if opcao not in ('1', '2', '3', '4'):
                print("Opção inválida, tente novamente\n")
                continue
            else:
                break
        return opcao

    def setHora(self, hora):
        self.__hora = hora

    def setMinuto(self, minuto):
        self.__minuto = minuto

    def setSegundo(self, segundo):
        self.__segundo = segundo

    def getHora(self):
        return self.__hora

    def getMinuto(self):
        return self.__minuto

    def getSegundo(self):
        return self.__segundo

    def mostrarHora(self):
        return f"{self.__hora}:{self.__minuto}:{self.__segundo}"

    def ajustarHora(self, hora=0, minuto=0, segundo=0):
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo


