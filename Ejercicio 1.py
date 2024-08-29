class Paciente:
    def __init__(self, nombre, motivo_consulta):
        self.nombre = nombre
        self.motivo_consulta = motivo_consulta
        self.tiene_consulta_previa = False

class Consultorio:
    def __init__(self):
        self.pacientes = []
        self.pacientes_en_espera = []

    def registrar_paciente(self, nombre, motivo_consulta):
        # Aqui es para comprobar si el paciente ya tiene consulta 
        paciente = self.buscar_paciente(nombre)
        if paciente:
            print(f"Paciente {nombre} ya tiene consulta. Pase a sala de espera.")
            self.pacientes_en_espera.append(paciente)
        else:
            # Aqui para registar un nuevo paciente 
            nuevo_paciente = Paciente(nombre, motivo_consulta)
            self.pacientes.append(nuevo_paciente)
            print(f"Paciente {nombre} registrado con motivo de consulta: {motivo_consulta}.")

    def buscar_paciente(self, nombre):
        for paciente in self.pacientes:
            if paciente.nombre == nombre:
                paciente.tiene_consulta_previa = True
                return paciente
        return None

    def asignar_fecha_consulta(self, nombre, fecha):
        paciente = self.buscar_paciente(nombre)
        if paciente:
            print(f"Asignando fecha de consulta para {nombre}: {fecha}.")
        else:
            print(f"Paciente {nombre} no encontrado.")

consultorio = Consultorio()

while True:
    print("***************BIENVENIDOS AL CONSULTORIO MEDICO**************")
    print("1. Registrar Paciente")
    print("2. Asignar Fecha de Consulta")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        print("----------------------------------")
        nombre = input("Ingrese el nombre del paciente: ")
        motivo = input("Ingrese el motivo de la consulta: ")
        consultorio.registrar_paciente(nombre, motivo)

    elif opcion == '2':
        print("----------------------------------")
        nombre = input("Ingrese el nombre del paciente para asignar fecha: ")
        fecha = input("Ingrese la fecha de la consulta (dd/mm/aaaa): ")
        consultorio.asignar_fecha_consulta(nombre, fecha)

    elif opcion == '3':
        print("Saliendo del sistema, Gracias") 
        break

    else:
        print("Opción no válida. Intente de nuevo.")
