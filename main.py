from utils import comprobarEntero


def menu():
    print("Que billete quieres elejir?")
    print("1 - Bitllet senzill")
    print("2 - TCasual")
    print("3 - TUsual")
    print("4 - TFamiliar")
    print("5 - TJove")

    numero_billete = comprobarEntero("","Eso no es un numero valido",1,5,"El número debe estar entre 1 y 5.")



menu()