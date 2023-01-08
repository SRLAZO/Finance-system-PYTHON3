import csv
from datetime import date, datetime

#Seccion para cuentas bancarias----------------------------------------------------------
class Cuenta:
    def __init__(self, dni, nombre, monto):
        self.dni = dni
        self.nombre = nombre
        self.monto = monto


    def __str__(self):
        return f"({self.dni}) {self.nombre}: {self.monto}"

class Cuentas:

    lista = []
    with open('Ficheros/cuentas.csv', newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for dni, nombre, monto in reader:
            cuenta = Cuenta(dni, nombre, monto)
            lista.append(cuenta)

    @staticmethod
    def buscar(dni):
        for cuenta in Cuentas.lista:
            if cuenta.dni == dni:
                return cuenta

    @staticmethod
    def crear(dni, nombre, monto):
        cuenta = Cuenta(dni, nombre, monto)
        Cuentas.lista.append(cuenta)
        Cuentas.guardar()
        return cuenta

    @staticmethod
    def transferencia():
        fecha = date.today()
        dni1 = input("\nCuenta origen > ")
        dni2 = input("\nCuenta destino > ")
        monto = input("\nMonto> ")
        for indice, cuenta in enumerate(Cuentas.lista):
            if cuenta.dni == dni1:
                Cuentas.lista[indice].monto = int(Cuentas.lista[indice].monto) - int(monto)
        for indice, cuenta in enumerate(Cuentas.lista):
            if cuenta.dni == dni2:
                Cuentas.lista[indice].monto = int(Cuentas.lista[indice].monto) + int(monto)
                Cuentas.guardar()
                with open('Flitchi/Ficheros/registro_transferencias.csv', 'a+') as fichero:
                    writer = csv.writer(fichero, delimiter=';')
                    writer.writerow((fecha, dni1, dni2, monto))

                print("Transaccion realizada")

    @staticmethod
    def modificar(dni, nombre, monto):
        for indice, cuenta in enumerate(Cuentas.lista):
            if cuenta.dni == dni:
                Cuentas.lista[indice].nombre = nombre
                Cuentas.lista[indice].monto = monto
                Cuentas.guardar()
                return Cuentas.lista[indice]

    @staticmethod
    def borrar(dni):
        for indice, cuenta in enumerate(Cuentas.lista):
            if cuenta.dni == dni:
                cuenta = Cuentas.lista.pop(indice)
                Cuentas.guardar()
                return cuenta
    
    @staticmethod
    def guardar():
        with open('Ficheros/cuentas.csv', 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for cuenta in Cuentas.lista:
                writer.writerow((cuenta.dni, cuenta.nombre, cuenta.monto))

    @staticmethod
    def mostrar_transferencias():
        lista = []
        with open('Ficheros/registro_transferencias.csv') as fichero:
            reader = csv.reader(fichero, delimiter=';')
            for fecha, dni1, dni2, monto in reader:
                registro = Registro_transfer(fecha, dni1, dni2, monto)
                lista.append(registro)
                print(registro)

# Seccion para gastos-------------------------------------------------------------------------

class Gasto:
    def __init__(self, dni, nombre, monto, frecuencia):
        self.dni = dni
        self.nombre = nombre
        self.monto = monto
        self.frecuencia = frecuencia

    def __str__(self):
        return f"({self.dni}) {self.nombre}: {self.monto} : {self.frecuencia}"

class Gastos:

    lista = []
    with open('Ficheros/gastos.csv', newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for dni, nombre, monto, frecuencia in reader:
            gasto = Gasto(dni, nombre, monto, frecuencia)
            lista.append(gasto)

    @staticmethod
    def buscar(dni):
        for gasto in Gastos.lista:
            if gasto.dni == dni:
                return gasto

    @staticmethod
    def crear(dni, nombre, monto, frecuencia):
        gasto = Gasto(dni, nombre, monto, frecuencia)
        Gastos.lista.append(gasto)
        Gastos.guardar()
        return gasto

    @staticmethod
    def modificar(dni, nombre, monto, frecuencia):
        for indice, gasto in enumerate(Gastos.lista):
            if gasto.dni == dni:
                Gastos.lista[indice].nombre = nombre
                Gastos.lista[indice].monto = monto
                Gastos.lista[indice].frecuencia = frecuencia
                Gastos.guardar()
                return Gastos.lista[indice]

    @staticmethod
    def borrar(dni):
        for indice, gasto in enumerate(Gastos.lista):
            if gasto.dni == dni:
                gasto = Gastos.lista.pop(indice)
                Gastos.guardar()
                return gasto
    
    @staticmethod
    def guardar():
        with open('Ficheros/gastos.csv', 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for gasto in Gastos.lista:
                writer.writerow((gasto.dni, gasto.nombre, gasto.monto, gasto.frecuencia))

    @staticmethod
    def registrar_gasto(dni1, dni2, monto):
        fecha = date.today()
        for indice, cuenta in enumerate(Cuentas.lista):
            if cuenta.dni == dni1:
                Cuentas.lista[indice].monto = int(Cuentas.lista[indice].monto) - int(monto)

                Cuentas.guardar()
                with open('Ficheros/registro_gastos.csv', 'a+', newline='\n') as fichero:
                    writer = csv.writer(fichero, delimiter=';')
                    writer.writerow((fecha, dni1, dni2, monto))

                print("Gasto registrado")

#TODO Ver porqué guarda la frecuencia con otro formato

# Seccion para Ingresos-------------------------------------------------------------------------

class Ingreso:
    def __init__(self, dni, nombre, monto, frecuencia):
        self.dni = dni
        self.nombre = nombre
        self.monto = monto
        self.frecuencia = frecuencia

    def __str__(self):
        return f"({self.dni}) {self.nombre}: {self.monto}"

class Ingresos:

    lista = []
    with open('Ficheros/ingresos.csv', newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for dni, nombre, monto, frecuencia in reader:
            ingreso = Ingreso(dni, nombre, monto, frecuencia)
            lista.append(ingreso)

    @staticmethod
    def buscar(dni):
        for ingreso in Ingresos.lista:
            if ingreso.dni == dni:
                return ingreso

    @staticmethod
    def crear(dni, nombre, monto, frecuencia):
        ingreso = Ingreso(dni, nombre, monto, frecuencia)
        Ingresos.lista.append(ingreso)
        Ingresos.guardar()
        return ingreso

    @staticmethod
    def modificar(dni, nombre, monto, frecuencia):
        for indice, ingreso in enumerate(Ingresos.lista):
            if ingreso.dni == dni:
                Ingresos.lista[indice].nombre = nombre
                Ingresos.lista[indice].monto = monto
                Ingresos.lista[indice].frecuencia = frecuencia
                Ingresos.guardar()
                return Ingresos.lista[indice]

    @staticmethod
    def borrar(dni):
        for indice, ingreso in enumerate(Ingresos.lista):
            if ingreso.dni == dni:
                ingreso = Ingresos.lista.pop(indice)
                Ingresos.guardar()
                return ingreso
    
    @staticmethod
    def guardar():
        with open('Ficheros/ingresos.csv', 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for ingreso in Ingresos.lista:
                writer.writerow((ingreso.dni, ingreso.nombre, ingreso.monto, ingreso.frecuencia))



# Clase para registros transferencias----------------------------------------------------------------------

class Registro_transfer:
    def __init__(self, fecha, dni1, dni2, monto):
        self.fecha = fecha
        self.dni1 = dni1
        self.dni2 = dni2
        self.monto = monto


    def __str__(self):
        return f"Fecha: [{self.fecha}] Remisor:({self.dni1}) Destinatario({self.dni2}) Monto: {self.monto}"

# Clase para registros gastos----------------------------------------------------------------------

class Registro_gastos:
    def __init__(self, fecha, cuenta, gasto, monto):
        self.fecha = fecha
        self.cuenta = cuenta
        self.gasto = gasto
        self.monto = monto


    def __str__(self):
        return f"Fecha: [{self.fecha}] Remisor:({self.cuenta}) Destinatario({self.gasto}) Monto: {self.monto}"

# Clase para los presupuestos---------------------------------------------------------------------

class Presupuesto:
    def __init__(self, nombre, fecha_inicial, fecha_final):
        self.nombre = nombre
        self.fecha_inicial = fecha_inicial
        self.fecha_final = fecha_final

    def __str__(self):
        return f"Presupuesto: {self.nombre} \nFecha inicial: {self.fecha_inicial} \nFecha final {self.fecha_final}"

class Presupuestos:

    lista = []
    with open('Ficheros/presupuestos.csv', newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for nombre, fecha_inicial, fecha_final in reader:
            presupuesto = Presupuesto(nombre, fecha_inicial, fecha_final)
            lista.append(presupuesto)

    @staticmethod
    def presupuesto_datos():
        nombre = input("Nombre > \n")
        for presupuesto in Presupuestos.lista:
            if presupuesto.nombre == nombre:
                print(presupuesto)
                print("INGRESOS: ")
                for gasto in Gastos.lista:
                    print(gasto + f"Gasto estimado: {presupuesto.fecha_final.month - presupuesto.fecha_inicial.month}")

    @staticmethod
    def buscar(nombre):
        for presupuesto in Presupuestos.lista:
            if presupuesto.nombre == nombre:
                return presupuesto 
        

    @staticmethod
    def crear(nombre, fecha_inicial, fecha_final):
        presupuesto = Presupuesto(nombre, fecha_inicial, fecha_final)
        Presupuestos.lista.append(presupuesto)
        Presupuestos.guardar()
        return presupuesto


    @staticmethod
    def borrar(nombre):
        for indice, presupuesto in enumerate(Presupuestos.lista):
            if presupuesto.nombre == nombre:
                presupuesto = Presupuestos.lista.pop(indice)
                Presupuestos.guardar()
                return presupuesto

    @staticmethod
    def guardar():
        with open('Ficheros/presupuestos.csv', 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for presupuesto in Presupuestos.lista:
                writer.writerow((presupuesto.nombre, presupuesto.fecha_inicial,presupuesto.fecha_final))



