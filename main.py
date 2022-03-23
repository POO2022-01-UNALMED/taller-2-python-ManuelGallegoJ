class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

        def cambiarColor(color):
            if color == "rojo" or color == "verde" or color == "amarillo" or color == "negro" or color == "blanco":
                self.color = color

class Motor:
    def __init__(self, numero, tipo, registro):
        self.numero = numero
        self.tipo = tipo
        self.registro = registro

        def cambiarRegistro(numero):
            self.numero = numero
        def asignarTipo(tipo):
            if tipo == "electrico" or tipo == "gasolina":
                self.tipo = tipo

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asiento, marca, motor, registro, cantidadCreados):
        self.modelo = modelo
        self.precio = precio
        self.asiento = asiento
        self.marca = marca
        self.motor = motor
        self.registro = registro

        def cantidadAsientos(self):
            c = 0
            for i in self.asientos:
                if type(i) == Asiento:
                    c += 1
            return c
            
        def verificarIntegridad(self):
            if self.motor.registro == self.registro:
                for i in self.asientos:
                    if type(i) == Asiento:
                        if self.registro != self.asiento.registro:
                            return "Las piezas no son originales"
                return "Auto original"
            else:
                return "Las piezas no son originales"
