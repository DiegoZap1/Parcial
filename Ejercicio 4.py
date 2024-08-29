'''Ejercicio 4

Una empresa de renta de transporte tiene varios tipos de vehículos a su
disposición cada uno con sus características y coste de renta. La
empresa periódicamente registra los nuevos vehículos que ingresan al
lote para su posterior puesta en renta.

 Implementa la funcionalidad de rentar los vehículos disponibles
tomando en cuenta los datos del cliente.
'''

import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

class NuevoVehiculo():
    def __init__(self,placa,marca,modelo,año,clase,transmision,color,motor,chasis,precio_renta):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.clase = clase
        self.asientos = "5.00 asientos"
        self.ruedas = 4
        self.transmision = transmision
        self.color = color
        self.motor = motor
        self.chasis = chasis
        self.precio_renta = precio_renta

    
    def mostrarinfo(self):
        tipo = ["Placa: ","Marca: ","Modelo: ","Año: ","Clase: ","Asientos: ",
                "Ruedas: ","Transmision: ","Color: ","Motor: ","Chasis: ","Precio: $"]
        lista = [self.placa,self.marca,self.modelo,self.año,self.clase,self.asientos,
                 self.ruedas,self.transmision,self.color,self.motor,self.chasis,self.precio_renta]
        print("============ Nuevo Vehiculo ===============")
        for i in range(1,len(lista)+1):
            print(f"{tipo[i-1]}{lista[i-1]}")

class Vehiculos():
    def __init__(self,placa,marca,modelo,año,pais,clase,transmision,color,motor,chasis,precio_renta):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.pais = pais
        self.clase = clase
        self.asientos = "5.00 asientos"
        self.ruedas = 4
        self.transmision = transmision
        self.color = color
        self.motor = motor
        self.chasis = chasis
        self.precio_renta = precio_renta
    
    def mostrarinfo(self):
        tipo = ["Placa: ","Marca: ","Modelo: ","Año: ","Pais: ","Clase: ","Asientos: ",
                "Ruedas: ","Transmision: ","Color: ","Motor: ","Chasis: ","Precio: $"]
        lista = [self.placa,self.marca,self.modelo,self.año,self.pais,self.clase,self.asientos,
                 self.ruedas,self.transmision,self.color,self.motor,self.chasis,self.precio_renta]
        print("============ Vehiculo =================")
        for i in range(1,len(lista)+1):
            print(f"{tipo[i-1]}{lista[i-1]}")
        print("==============================================")

def menu():
    limpiar_consola()
    print("========= Menu ========")
    print("1. Rentar un nuevo carro")
    print("2. Rentar un carro")
    print("=======================")
    opcion = int(input("Que quiere hacer? : "))
    if opcion == 1:
        nuevoVehiculo()
    elif opcion == 2:
        rentarVehiculo()
    else:
        print("Opcion no valida")

def nuevoVehiculo():
    limpiar_consola()
    placa = input("Numero de placa: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    año = int(input("Año: "))
    clase = input("Clase: ")
    transmision = input("Transmisión: ")
    color = input("Color")
    motor = input("Motor: ")
    chasis = input("Chasis: ")
    precio = float(input("Rentado por: $"))
    nuevo = NuevoVehiculo(placa,marca,modelo,año,clase,transmision,color,motor,chasis,precio)
    limpiar_consola()
    nuevo.mostrarinfo()
    print("==============================================")

def rentarVehiculo():
    limpiar_consola()
    placa = input("Numero de placa: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    año = int(input("Año: "))
    pais = input("País: ")
    clase = input("Clase: ")
    transmision = input("Transmisión: ")
    color = input("Color")
    motor = input("Motor: ")
    chasis = input("Chasis: ")
    precio = float(input("Rentado por: $"))
    rentado = Vehiculos(placa,marca,modelo,año,pais,clase,transmision,color,motor,chasis,precio)
    limpiar_consola()
    rentado.mostrarinfo()    
    print("==============================================")

menu()