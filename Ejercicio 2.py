from datetime import datetime, timedelta

class Prestamo:
    def __init__(self, nombre, libro, fecha_retiro):
        self.nombre = nombre
        self.libro = libro
        self.fecha_retiro = datetime.strptime(fecha_retiro, "%d/%m/%Y")
        self.fecha_limite = self.fecha_retiro + timedelta(days=15)  
        self.devuelto = False

    def verificar_devolucion(self, fecha_devolucion):
        #Aqui es para verificar su devolucion del libro 
        fecha_devolucion = datetime.strptime(fecha_devolucion, "%d/%m/%Y")
        if fecha_devolucion > self.fecha_limite:
            dias_tarde = (fecha_devolucion - self.fecha_limite).days
            print(f"Libro devuelto tarde por {dias_tarde} días. Se aplicará una sanción.")
        else:
            print("Libro devuelto a tiempo.")
        self.devuelto = True

class Biblioteca:
    def __init__(self):
        self.prestamos = []

    def registrar_prestamo(self, nombre, libro, fecha_retiro):
        #Aqui es donde registramos los prestamos de los libros 
        nuevo_prestamo = Prestamo(nombre, libro, fecha_retiro)
        self.prestamos.append(nuevo_prestamo)
        print(f"Préstamo registrado: {nombre} ha retirado el libro '{libro}' el {fecha_retiro}. Fecha límite de devolución: {nuevo_prestamo.fecha_limite.strftime('%d/%m/%Y')}")

    def devolver_libro(self, nombre, libro, fecha_devolucion):
        for prestamo in self.prestamos:
            if prestamo.nombre == nombre and prestamo.libro == libro and not prestamo.devuelto:
                prestamo.verificar_devolucion(fecha_devolucion)
                return
        print("No se encontró el préstamo o el libro ya fue devuelto.")

biblioteca = Biblioteca()

while True:
    print("************* BIENVENIDOS AL SISTEMA DE PRESTAMOS DE LA BIBLIOTECA**************")
    print("1. Registrar Préstamo")
    print("2. Devolver Libro")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        print("----------------------------------")
        nombre = input("Ingrese su nombre: ")
        libro = input("Ingrese el título del libro: ")
        fecha_retiro = input("Ingrese la fecha de retiro (dd/mm/aaaa): ")
        biblioteca.registrar_prestamo(nombre, libro, fecha_retiro)

    elif opcion == '2':
        print("----------------------------------")
        nombre = input("Ingrese su nombre: ")
        libro = input("Ingrese el título del libro: ")
        fecha_devolucion = input("Ingrese la fecha de devolución (dd/mm/aaaa): ")
        biblioteca.devolver_libro(nombre, libro, fecha_devolucion)

    elif opcion == '3':
        print("Saliendo del sistema, Gracias")
        break

    else:
        print("Opción no válida. Intente de nuevo.")
    