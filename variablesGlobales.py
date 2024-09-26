from array import ArrayType

cambioZona2 = 1.3125
cambioZona3 = 1.8443

class TipoBoleto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio



class Boleto:
    def __init__(self, tipo_billete: int, zona: int, cantidad: int, tipos_billetes: list, cambio_zona2: float, cambio_zona3: float):
        self.tipo_billete = tipo_billete
        self.zona = zona
        self.cantidad = cantidad
        self.precio = self.calcular_precio(tipos_billetes, cambio_zona2, cambio_zona3)

    def calcular_precio(self, tipos_billetes: list, cambio_zona2: float, cambio_zona3: float) -> float:
        if self.zona == 1:
            return self.cantidad * tipos_billetes[self.tipo_billete]['precio']
        elif self.zona == 2:
            return self.cantidad * tipos_billetes[self.tipo_billete]['precio'] * cambio_zona2
        elif self.zona == 3:
            return self.cantidad * tipos_billetes[self.tipo_billete]['precio'] * cambio_zona3
        else:
            return 0.0


class TipoBoleto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

# Lista de tipos de boletos
tipos_billetes = [
    TipoBoleto(nombre="Bitllet senzill", precio=2.40),
    TipoBoleto(nombre="TCasual", precio=11.35),
    TipoBoleto(nombre="TUsual", precio=40.00),
    TipoBoleto(nombre="TFamiliar", precio=10.00),
    TipoBoleto(nombre="TJove", precio=80.00)
]
