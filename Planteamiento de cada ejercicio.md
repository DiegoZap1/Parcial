Integrantes:
Diego Alexander Zapata López SMSS013123 
Jose Luis Escobar Caceres SMSS012223



1) Sistema de Gestión de Pacientes
Planteamiento:
Este código tiene como objetivo gestionar un consultorio médico, permitiendo registrar pacientes, verificar si ya tienen una consulta previa y asignar fechas de consulta.

Motivo de la solución:
Se utiliza la programación orientada a objetos para modelar tanto a los pacientes como al consultorio, lo que permite organizar mejor las funciones y los datos.

Clases: Paciente y Consultorio se utilizan para representar pacientes individuales y el sistema de gestión del consultorio, respectivamente.
Métodos:
registrar_paciente: Permite registrar un paciente nuevo o moverlo a la sala de espera si ya tiene una consulta.
buscar_paciente: Busca si un paciente ya está registrado.
asignar_fecha_consulta: Asigna una fecha de consulta a un paciente ya registrado.
Estos métodos ayudan a mantener el sistema ordenado y permiten realizar acciones específicas según el estado del paciente.



2) Sistema de Préstamos de Biblioteca
Planteamiento:
Este código gestiona el sistema de préstamos de una biblioteca, permitiendo registrar préstamos de libros y verificar si las devoluciones se realizan a tiempo.

Motivo de la solución:
La programación orientada a objetos facilita la representación de los préstamos y la gestión de los libros.

Clases:
Prestamo: Modela cada préstamo con detalles como el nombre del usuario, libro, fechas de retiro y devolución.
Biblioteca: Gestiona los préstamos registrados.
Métodos:
verificar_devolucion: Verifica si la devolución se realiza a tiempo y calcula si hay sanciones.
registrar_prestamo: Añade un nuevo préstamo al sistema.
devolver_libro: Marca un préstamo como devuelto y verifica si fue devuelto a tiempo.
Estos métodos aseguran que el sistema pueda gestionar y supervisar de manera eficiente los préstamos y devoluciones.



3) Sistema de Gestión de Reservas en un Hotel
Planteamiento:
Este ejercicio simula la reserva de habitaciones en un hotel, permitiendo seleccionar habitaciones, solicitar servicios extra, y generar una factura detallada.

Motivo de la solución:
Se utiliza la herencia en la programación orientada a objetos para simplificar la creación de clases relacionadas entre sí, como habitaciones, extras, y facturas.

Clases:
extra, habitacion, cliente, y factura: Cada una de estas clases añade funcionalidades y características específicas que se heredan entre sí para construir la factura final.
Métodos:
definir_tipo, definir_costo: Determinan las características y costos de las habitaciones.
generarfactura: Genera y muestra la factura detallada para el cliente.
La solución facilita la reutilización de código y la extensión del sistema, permitiendo agregar más servicios o tipos de habitaciones sin reescribir la lógica central.



4) Sistema de Renta de Vehículos
Planteamiento:
Este código permite registrar y rentar vehículos, considerando las características específicas de cada tipo de vehículo y los datos del cliente.

Motivo de la solución:
La programación orientada a objetos se usa para modelar los vehículos y su proceso de renta de forma estructurada y organizada.

Clases:
NuevoVehiculo y Vehiculos: Representan los vehículos que ingresan al sistema y los que están disponibles para rentar, respectivamente.
Métodos:
mostrarinfo: Muestra la información completa del vehículo, lo cual es útil para que el cliente vea los detalles antes de tomar una decisión.
nuevoVehiculo y rentarVehiculo: Permiten registrar nuevos vehículos y procesar la renta de un vehículo disponible.
Estos métodos permiten una gestión clara y concisa del inventario de vehículos y de las operaciones de renta, mejorando la organización del sistema.
