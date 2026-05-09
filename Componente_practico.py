# ----------------------------------------------------------
# Autor: Brayan Monsalve
# Fase 4 - Sistema de Gestión de Servicios
#
# Este programa aplica Programación Orientada a Objetos:
# abstracción, herencia y polimorfismo.
# ----------------------------------------------------------

# Importamos módulo para clases abstractas
from abc import ABC, abstractmethod


# ----------------------------------------------------------
# CLASE ABSTRACTA: Entidad
# Clase base para entidades del sistema
# ----------------------------------------------------------
class Entidad(ABC):

    def __init__(self, nombre):
        self._nombre = nombre  # Atributo protegido


# ----------------------------------------------------------
# CLASE: Cliente (hereda de Entidad)
# ----------------------------------------------------------
class Cliente(Entidad):

    def __init__(self, nombre, documento):
        super().__init__(nombre)  # Llama al constructor padre
        self._documento = documento

    # Método para mostrar información del cliente
    def mostrar_info(self):
        return f"Cliente: {self._nombre}, Documento: {self._documento}"


# ----------------------------------------------------------
# CLASE ABSTRACTA: Servicio
# Define comportamiento común de servicios
# ----------------------------------------------------------
class Servicio(ABC):

    def __init__(self, nombre):
        self._nombre = nombre

    # Método abstracto para calcular costo (polimorfismo)
    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    # Método abstracto para describir el servicio
    @abstractmethod
    def descripcion(self):
        pass


# ----------------------------------------------------------
# CLASE: ServicioSala
# ----------------------------------------------------------
class ServicioSala(Servicio):

    # Calcula el costo según la duración
    def calcular_costo(self, duracion):
        return duracion * 50

    # Describe el servicio
    def descripcion(self):
        return "Servicio de reserva de sala"


# ----------------------------------------------------------
# CLASE: ServicioEquipo
# ----------------------------------------------------------
class ServicioEquipo(Servicio):

    def calcular_costo(self, duracion):
        return duracion * 30

    def descripcion(self):
        return "Servicio de alquiler de equipos"


# ----------------------------------------------------------
# CLASE: ServicioAsesoria
# ----------------------------------------------------------
class ServicioAsesoria(Servicio):

    def calcular_costo(self, duracion):
        return duracion * 80

    def descripcion(self):
        return "Servicio de asesoría"


# ----------------------------------------------------------
# CLASE: Reserva
# Representa una reserva realizada por un cliente
# ----------------------------------------------------------
class Reserva:

    def __init__(self, cliente, servicio, duracion):
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = "Pendiente"

    # Confirma la reserva
    def confirmar(self):
        self._estado = "Confirmada"

    # Cancela la reserva
    def cancelar(self):
        self._estado = "Cancelada"

    # Procesa la reserva y calcula el costo total
    def procesar(self):
        costo = self._servicio.calcular_costo(self._duracion)
        return f"Reserva para {self._cliente._nombre} - Total: ${costo}"


# ----------------------------------------------------------
# CLASE: Sistema
# Gestiona clientes, servicios y reservas
# ----------------------------------------------------------
class Sistema:

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    # Agrega un cliente al sistema
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    # Agrega un servicio al sistema
    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)

    # Crea una reserva
    def crear_reserva(self, reserva):
        self.reservas.append(reserva)

    # Muestra todas las reservas
    def mostrar_reservas(self):
        for r in self.reservas:
            print(r.procesar())


# ----------------------------------------------------------
# PRUEBA BÁSICA (SIMULACIÓN)
# ----------------------------------------------------------

# Crear sistema
sistema = Sistema()

# Crear cliente
cliente1 = Cliente("Brayan", "123")

# Crear servicios
sala = ServicioSala("Sala")
equipo = ServicioEquipo("Equipo")
asesoria = ServicioAsesoria("Asesoria")

# Registrar datos en el sistema
sistema.agregar_cliente(cliente1)
sistema.agregar_servicio(sala)

# Crear reserva
reserva1 = Reserva(cliente1, sala, 2)

# Guardar reserva
sistema.crear_reserva(reserva1)

# Mostrar resultado
sistema.mostrar_reservas()

# ----------------------------------------------------------
# EXCEPCIONES PERSONALIZADAS
# ----------------------------------------------------------

# Error para clientes inválidos
class ClienteInvalidoError(Exception):
    pass


# Error para reservas inválidas
class ReservaError(Exception):
    pass


# ----------------------------------------------------------
# VALIDACIONES EN CLIENTE
# ----------------------------------------------------------

class Cliente(Entidad):

    def __init__(self, nombre, documento):

        # Validar nombre vacío
        if not nombre.strip():
            raise ClienteInvalidoError(
                "El nombre del cliente no puede estar vacío"
            )

        # Validar documento vacío
        if not documento.strip():
            raise ClienteInvalidoError(
                "El documento no puede estar vacío"
            )

        super().__init__(nombre)
        self._documento = documento

    def mostrar_info(self):
        return f"Cliente: {self._nombre}, Documento: {self._documento}"


# ----------------------------------------------------------
# VALIDACIONES EN RESERVA
# ----------------------------------------------------------

class Reserva:

    def __init__(self, cliente, servicio, duracion):

        # Validar duración
        if duracion <= 0:
            raise ReservaError(
                "La duración debe ser mayor a cero"
            )

        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = "Pendiente"

    def confirmar(self):
        self._estado = "Confirmada"

    def cancelar(self):
        self._estado = "Cancelada"

    # Procesar reserva con manejo de errores
    def procesar(self):

        try:
            costo = self._servicio.calcular_costo(
                self._duracion
            )

        except Exception as e:

            return f"Error al procesar reserva: {e}"

        else:

            return (
                f"Reserva para "
                f"{self._cliente._nombre} "
                f"- Total: ${costo}"
            )

        finally:
            print("Proceso de reserva finalizado")


# ----------------------------------------------------------
# PRUEBAS DE EXCEPCIONES
# ----------------------------------------------------------

try:

    # Cliente inválido
    cliente_error = Cliente("", "")

except ClienteInvalidoError as e:

    print(f"Error de cliente: {e}")

finally:

    print("Validación de cliente terminada")


print("\n")


try:

    # Reserva inválida
    reserva_error = Reserva(cliente1, sala, -2)

except ReservaError as e:

    print(f"Error de reserva: {e}")

finally:

    print("Validación de reserva terminada")