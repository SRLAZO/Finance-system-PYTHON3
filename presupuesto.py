import database as db
import helpers
from datetime import datetime

def iniciar():
    
    while True:
        helpers.limpiar_pantalla()

        print("=======================")
        print(" Bienvenido a Flitchi  ")
        print("   < PRESUPUESTO >     ")
        print("=======================")
        print("[1] Crear Presupuesto  ")
        print("[2] Mostrar Presupuesto")#PENDIENTE
        print("[3] Buscar             ")#PENDIENTE
        print("[4] Añadir             ")#PENDIENTE
        print("[5] Modificar           ")#PENDIENTE
        print("[6] Borrar             ") 
        print("[E] Salir             ")
        print("=======================")    

        opcion = input("\n\n> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Listando cuentas...")
            helpers.ingresar_presupuesto()
            print("\n Cuenta ingresada correctamente... \n")

        if opcion == '2':
            print("Mostrando presupuesto...\n")
            nombre = input(">> Ingresar nombre: \n")
            db.Presupuestos.buscar(nombre)
            for presupuesto in db.Presupuestos.lista:
                if presupuesto.nombre == nombre:
                    Fi = presupuesto.fecha_inicial
                    Ff = presupuesto.fecha_final
                    
                    start = datetime.strptime(Fi, "%Y-%m-%d")
                    end = datetime.strptime(Ff, "%Y-%m-%d")

                    diff = (end.year - start.year)*12 +(end.month - start.month)

                    print("\n>> Ingresos Presupuestados: \n")
                    for ingreso in db.Ingresos.lista:
                        ingreso_anual = int(ingreso.monto) * diff
                        print(f"Ingreso: {ingreso.nombre} Presupuesto: {ingreso_anual}")


                    print("\n>> Gastos Presupuestados: \n")
                    for gasto in db.Gastos.lista:
                        gasto_anual = int(gasto.monto) * diff
                        print(f"Gasto: {gasto.nombre} Presupuesto: {gasto_anual}")


        if opcion == '6':
            print("Borrando un presupuesto...")
            nombre = input("\n> nombre: \n")
            if db.Presupuestos.buscar(nombre):
                db.Presupuestos.borrar(nombre)
                print(">\nPresupuesto borrado correctamente... \n")
            else:
                print("\n Nombre no encontrado...")

        if opcion == 'E':
            print("\nSaliendo...\n")
            break

        input("> Presiona ENTER para continuar...")


