
from variablesGlobales import *

# Funcions
def mostrar_menu_bitllets():
    print("Quin bitllet desitja adquirir?")
    print("1 - Bitllet senzill")
    print("2 - TCasual")
    print("3 - TUsual")
    print("4 - TFamiliar")
    print("5 - TJove")


def seleccionar_bitllet():
    while True:
        mostrar_menu_bitllets()
        opcions = ["Bitllet senzill", "TCasual", "TUsual", "TFamiliar", "TJove"]
        try:
            eleccio = int(input())
            if 1 <= eleccio <= 5:
                return opcions[eleccio - 1]
            else:
                print("Opció no vàlida. Torna-ho a intentar.")
        except ValueError:
            print("Entrada no vàlida. Introdueix un número.")


def seleccionar_zona():
    while True:
        try:
            zona = int(input("Quina zona vol viatjar? (1-3): "))
            if 1 <= zona <= 3:
                return zona
            else:
                print("Zona no vàlida. Introdueix una zona entre 1 i 3.")
        except ValueError:
            print("Entrada no vàlida. Introdueix un número.")


def calcular_preu(tipus_bitllet, zona):
    preu_base = PREUS_BASE[tipus_bitllet]
    preu_final = preu_base * (1.25 ** (zona - 1))
    return round(preu_final, 2)


def introduir_moneda(preu_total):
    total_introduit = 0
    while total_introduit < preu_total:
        print(f"Ha introduït: {total_introduit:.2f}€, li resta per pagar {preu_total - total_introduit:.2f}€")
        try:
            moneda = float(input("Introdueixi monedes o bitllets vàlids de EURO: "))
            if moneda in VALID_COINS:
                total_introduit += moneda
            else:
                print("Moneda no vàlida.")
        except ValueError:
            print("Entrada no vàlida. Introdueix un número.")
    canvi = round(total_introduit - preu_total, 2)
    return canvi


def imprimir_tiquet(compres):
    print("_____TIQUET_____")
    total = 0
    for bitllet, zona, preu in compres:
        print(f"{bitllet} zona {zona} - Preu: {preu:.2f}€")
        total += preu
    print(f"Total: {total:.2f}€")
    print("-----------------------------")
    print("Reculli el teu tiquet.")


def comprar_bitllets():
    compres = []
    seguir_comprant = True
    while len(compres) < MAX_BILLETES and seguir_comprant:
        tipus_bitllet = seleccionar_bitllet()
        zona = seleccionar_zona()
        preu = calcular_preu(tipus_bitllet, zona)
        print(f"Ha escollit la opció: {tipus_bitllet}, Zona {zona}")
        print(f"El preu del bitllet és {preu:.2f}€")
        compres.append((tipus_bitllet, zona, preu))

        seguir = input("Vols seguir comprant? [S, N]: ").lower()
        seguir_comprant = seguir == 's'
    return compres


def proces_venda():
    continuar_venda = True
    while continuar_venda:
        compres = comprar_bitllets()
        total = sum(preu for _, _, preu in compres)
        print(f"Has comprat {len(compres)} bitllet(s), ha de pagar {total:.2f}€")

        canvi = introduir_moneda(total)
        if canvi > 0:
            print(f"Reculli el seu bitllet i el seu canvi: {canvi:.2f}€")
        else:
            print("Reculli el seu bitllet.")

        tiquet = input("Vols el tiquet? [S, N]: ").lower()
        if tiquet == 's':
            imprimir_tiquet(compres)
        print("Adeu!!\n")

