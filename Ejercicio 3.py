'''Ejercicio 3

Un hotel de playa cuenta con un recepcionista que se encarga de
presentar a los clientes las opciones de habitaciones disponibles junto
con sus precios. Tras la elección de la habitación, el recepcionista
solicita los datos personales del cliente y el número de noches que
permanecerá en el hotel. Finalmente, entrega al cliente una factura
detallada con el total de los gastos.

Adicionalmente, los clientes pueden solicitar servicios extra,
como el uso de la piscina o la cancha de golf, que tienen un costo
adicional. Implementa esta funcionalidad en tu programa
'''

import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

class extra():
    def __init__(self,numeroextra):
        self.numeroextra = numeroextra
        self.extras = self.definir_Extra()
    
    def definir_Extra(self):
        if self.numeroextra == 0:
            return "Vacio"
        elif self.numeroextra == 1:
            return "Piscina"
        elif self.numeroextra == 2:
            return "Cancha de golf"

class habitacion(extra):
    def __init__(self,numero,fecha_entrada,fecha_salida, numeroextra):
        super().__init__(numeroextra)
        self.numero = numero
        self.tipo = self.definir_tipo()
        self.costo = self.definir_costo()
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
    
    def definir_costo(self):
        if self.numero == 1:
            return "$50"
        elif self.numero == 2:
            return "$75"
        elif self.numero == 3:
            return "$100"
        else:
            print("Opcion no valida")
    
    def definir_tipo(self):
        if self.numero == 1:
            return "Individual"
        elif self.numero == 2:
            return "Doble"
        elif self.numero == 3:
            return "Cuadruple"
        else:
            print("Opcion no valida")

class cliente(habitacion):
    def __init__(self,nombre, apellido, telefono, dui, nhuespedes, n_noches, numero, fecha_entrada, fecha_salida, numeroextra):
        super().__init__(numero, fecha_entrada, fecha_salida, numeroextra)
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.dui = dui
        self.nhuespedes = nhuespedes
        self.n_noches = n_noches
        
class factura(cliente):
    def __init__(self, nombre, apellido, telefono, dui, nhuespedes, n_noches, numero, fecha_entrada, fecha_salida, numeroextra):
        super().__init__(nombre, apellido, telefono, dui, nhuespedes, n_noches, numero, fecha_entrada, fecha_salida, numeroextra)

        self.habitacion = [f"Tipo de habitación: {self.tipo}",f"Costo de la habitación: {self.costo}",
                           f"Fecha de entrada: {fecha_entrada}",f"Fecha de salida: {fecha_salida}",f"Extras: {self.extras}"]

    def generarfactura(self):
        limpiar_consola()
        cliente = [f"Nombre: {self.nombre}",f"Apellido: {self.apellido}",f"Telefono: {self.telefono}",
                   f"Dui: {self.dui}",f"Numero de huespedes: {self.nhuespedes}",f"Numero de noches: {self.n_noches}"]
        print("================================")
        for i in range(1,len(cliente)+1):
            print(f"{cliente[i-1]}")
        print("================================")
        for i in range(1,len(self.habitacion)+1):
            print(f"{self.habitacion[i-1]}")
        print("================================")

habitacion_huesped = ["1. Habitacion individual $50","2. Habitacion doble $75","3. Habitación cuadruple $100"]
extras = ["0. Ninguna","1. Piscina $5","2. Cancha de golf $10"]    
    
def genfactura():
    limpiar_consola()
    for i in range(1,len(habitacion_huesped)+1):
        print(f"{habitacion_huesped[i-1]}")
    print("===================================")
    numero = int(input("Que habitación desea? : "))
    limpiar_consola()
    entrada = input("Fecha de entrada: ")
    salida = input("Fecha de salida: ")
    limpiar_consola()
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Telefono: ")
    dui = input("Dui: ")
    n_huespedes = int(input("Numero de huespedes: "))
    noches = int(input("Numero de noches: "))
    limpiar_consola()
    for i in range(1,len(extras)+1):
        print(f"{extras[i-1]}")
    print("===================================")
    numeroextra = int(input("Desea algun extra? : "))
    fac = factura(nombre,apellido,telefono,dui,n_huespedes,noches,numero,entrada,salida,numeroextra)
    fac.generarfactura()

genfactura()