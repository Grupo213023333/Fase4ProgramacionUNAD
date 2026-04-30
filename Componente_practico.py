# ----------------------------------------------------------
# Fase 4 - Sistema de Gestión de Servicios
#
# Este programa aplica Programación Orientada a Objetos:
# abstracción, herencia y polimorfismo.
# ----------------------------------------------------------

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox


# ----------------------------------------------------------
# BASE CLASS: Dispositivo
# ----------------------------------------------------------
class Dispositivo:

    def __init__(self, nombre):
        self._nombre = nombre
        self._estado = "OFF"

    def encender(self):
        self._estado = "ON"
        return f"{self._nombre} turned ON"

    def apagar(self):
        self._estado = "OFF"
        return f"{self._nombre} turned OFF"

    # Polymorphic method
    def status(self):
        return f"{self._nombre} is {self._estado}"

    # Method overloading simulated with optional parameters
    def configurar(self, modo=None, intensidad=None, hora=None):
        return f"{self._nombre} configured"


# ----------------------------------------------------------
# CHILD CLASS: BombillaInteligente
# ----------------------------------------------------------
class BombillaInteligente(Dispositivo):

    def encender(self):
        return "Light bulb ON 💡"

    def apagar(self):
        return "Light bulb OFF 💡"

    def status(self):
        return "Light bulb status checked"

    def configurar(self, modo=None, intensidad=None, hora=None):
        return f"Light configured: mode={modo}, intensity={intensidad}, time={hora}"


# ----------------------------------------------------------
# CHILD CLASS: CortinaInteligente
# ----------------------------------------------------------
class CortinaInteligente(Dispositivo):

    def encender(self):
        return "Curtain opened 🪟"

    def apagar(self):
        return "Curtain closed 🪟"

    def status(self):
        return "Curtain status checked"

    def configurar(self, modo=None, intensidad=None, hora=None):
        return f"Curtain configured: mode={modo}, level={intensidad}, time={hora}"


# ----------------------------------------------------------
# CHILD CLASS: TermostatoInteligente
# ----------------------------------------------------------
class TermostatoInteligente(Dispositivo):

    def encender(self):
        return "Thermostat ON 🌡"

    def apagar(self):
        return "Thermostat OFF 🌡"

    def status(self):
        return "Thermostat status checked"

    def configurar(self, modo=None, intensidad=None, hora=None):
        return f"Thermostat configured: mode={modo}, temp={intensidad}, time={hora}"


# ----------------------------------------------------------
# CLASS: ControlCentral
# Manages all devices
# ----------------------------------------------------------
class ControlCentral:

    def __init__(self):
        self.dispositivos = []

    def agregar_dispositivo(self, dispositivo):
        self.dispositivos.append(dispositivo)

    # Polymorphism: same method for all devices
    def encender_todos(self):
        return [d.encender() for d in self.dispositivos]

    def apagar_todos(self):
        return [d.apagar() for d in self.dispositivos]

    def estado_general(self):
        return [d.status() for d in self.dispositivos]


# ----------------------------------------------------------
# CREATE CONTROL SYSTEM
# ----------------------------------------------------------
control = ControlCentral()

# Add devices
control.agregar_dispositivo(BombillaInteligente("Light"))
control.agregar_dispositivo(CortinaInteligente("Curtain"))
control.agregar_dispositivo(TermostatoInteligente("Thermostat"))


# ----------------------------------------------------------
# GUI
# ----------------------------------------------------------
ventana = ttk.Window(themename="cosmo")
ventana.title("Smart Home Control")
ventana.geometry("500x450")

ttk.Label(ventana, text="Select Device").pack(pady=5)

combo = ttk.Combobox(
    ventana,
    values=["Light", "Curtain", "Thermostat"]
)
combo.pack()

ttk.Label(ventana, text="Mode").pack()
entry_mode = ttk.Entry(ventana)
entry_mode.pack()

ttk.Label(ventana, text="Intensity / Value").pack()
entry_intensity = ttk.Entry(ventana)
entry_intensity.pack()

ttk.Label(ventana, text="Schedule Time").pack()
entry_time = ttk.Entry(ventana)
entry_time.pack()

resultado = ttk.Label(ventana, text="Status:")
resultado.pack(pady=15)


# ----------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------
def obtener_dispositivo(nombre):
    for d in control.dispositivos:
        if nombre.lower() in d._nombre.lower():
            return d
    return None


def encender_todos():
    mensajes = control.encender_todos()
    resultado.config(text="\n".join(mensajes))


def apagar_todos():
    mensajes = control.apagar_todos()
    resultado.config(text="\n".join(mensajes))


def ver_estado():
    mensajes = control.estado_general()
    resultado.config(text="\n".join(mensajes))


def configurar():
    nombre = combo.get()
    dispositivo = obtener_dispositivo(nombre)

    if dispositivo is None:
        messagebox.showerror("Error", "Select a device")
        return

    modo = entry_mode.get()
    intensidad = entry_intensity.get()
    hora = entry_time.get()

    mensaje = dispositivo.configurar(modo, intensidad, hora)
    resultado.config(text=mensaje)


# ----------------------------------------------------------
# BUTTONS
# ----------------------------------------------------------
ttk.Button(ventana, text="Turn ON All", bootstyle=SUCCESS, command=encender_todos).pack(pady=5)
ttk.Button(ventana, text="Turn OFF All", bootstyle=DANGER, command=apagar_todos).pack(pady=5)
ttk.Button(ventana, text="Check Status", command=ver_estado).pack(pady=5)
ttk.Button(ventana, text="Configure Device", bootstyle=INFO, command=configurar).pack(pady=10)

ventana.mainloop()

