

def comprobarEntero( mensajeIntroducir:str, mensajeRetorno:str, min:int = -2_147_483_648, max:int = 2_147_483_647, mensajeRango:str = None) -> int:
    if mensajeRango is None:
        mensajeRango = mensajeRetorno

    while True:
        try:
            numero = int(input(mensajeIntroducir))
            if min <= numero <= max:
                return numero
            else:
                print(mensajeRango)
        except ValueError:
            print(mensajeRetorno)

