import database as db
import os 
import platform
import re

def dni_valido(dni, lista):
    if not re.match('[A-Z]{3}$', dni):
        print("DNI incorrecto, debe cumplir el formato")
        return False

    for value in lista:
        if value.dni == dni:
            print("DNI utilizado Ya existente.")
            return False
    
    return True

def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')

def ingresar_clase():
    dni = input("> DNI: \n")
    nombre = input("> Nombre: \n")
    monto = input("> Monto: \n")

    db.Cuentas.crear(dni, nombre, monto)

def ingresar_gasto():
    dni = input("\n> DNI: \n")
    nombre = input("\n> Nombre: \n")
    monto = input("\n> Monto: \n")
    frecuencia = input("\n> Frecuencia\n")

    db.Gastos.crear(dni, nombre, monto, frecuencia)
    
def ingresar_ingreso():
    dni = input("\n> DNI: \n")
    nombre = input("\n> Nombre: \n")
    monto = input("\n> Monto: \n")
    frecuencia = input("\n> Frecuencia\n")

    db.Ingresos.crear(dni, nombre, monto, frecuencia)


def ingresar_presupuesto():
    nombre = input("\n> Nombre: \n")
    fecha_inicial = input("\n> Fecha inicial: \n")
    fecha_final = input("\n> Fecha final: \n")

    db.Presupuestos.crear(nombre, fecha_inicial, fecha_final)