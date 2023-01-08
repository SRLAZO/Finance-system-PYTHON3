import database as db
import helpers
import os
import presupuesto

def iniciar():
    
    while True:
        helpers.limpiar_pantalla()

        print("======================")
        print(" Bienvenido a Flitchi ")
        print("======================")
        print("[1] Listar Cuentas    ")
        print("[2] Listar Gastos     ")
        print("[3] Listar Ingresos   ")
        print("[4] Buscar            ") 
        print("[5] Añadir            ")
        print("[6] Modificar         ")
        print("[7] Borrar            ")
        print("[8] Transferencia     ")
        print("[9] Presupuestos.     ") 
        print("[10] Trans Realizads  ")
        print("[11] Registrar gasto  ")
        print("[E] Salir             ")
        print("======================")    

        opcion = input("\n\n> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Listando cuentas...")
            for cuenta in db.Cuentas.lista:
                print(cuenta)
            

        elif opcion == '2':
            print("Listando gastos...")
            for gasto in db.Gastos.lista:
                print(gasto)

        elif opcion == '3':
            print("Listando ingreso...")
            for ingreso in db.Ingresos.lista:
                print(ingreso)

        elif opcion == '4':
            print("Buscando...")
            seleccion = input(">>[C] Buscar cuenta \n>>[G] Buscar gasto\n>>[I] Buscar un ingreso\n\n ")
            if seleccion == 'C':
                print("\nBuscando cuenta...")
                nombre = input("\n> ID:")
                cuenta = db.Cuentas.buscar(nombre)
                print(cuenta) if cuenta else print("Dato no encontrado")

            elif seleccion == 'G':
                print("\nBuscando gasto...")
                nombre = input("\n> ID:")
                gasto = db.Gastos.buscar(nombre)
                print(gasto) if gasto else print("Dato no encontrado")

            elif seleccion == 'I':
                print("\nBuscando ingreso...")
                nombre = input("\n> ID:")
                ingreso = db.Ingresos.buscar(nombre)
                print(ingreso) if ingreso else print("Dato no encontrado")

        
        elif opcion == '5':
            print("Creando...")
            seleccion = input(">>[C] crear cuenta \n>>[G] crear gasto\n>>[I] crear un ingreso\n>>[P] crear presupuesto\n\n ")
            if seleccion == 'C':
                print("\nIngresando cuenta...")
                helpers.ingresar_clase()
                print("\nCliente ingresado correctamente.\n")

            elif seleccion == 'G':
                print("\nIngresando gasto...")
                helpers.ingresar_gasto()
                print("\nGasto ingresado correctamente.\n")

            elif seleccion == 'I':
                print("\nIngresando ingreso...")
                helpers.ingresar_ingreso()
                print("\nGasto ingresado correctamente.\n")

            elif seleccion == 'P':
                print("\nAccediendo a Menu Presupuesto...")
                presupuesto.iniciar()

            else:
                print("Favor seleccionar una opcion valida")
            pass

        elif opcion == '6':
            print("Modificando dato...")
            seleccion = input(">>[C] Buscar cuenta \n>>[G] Buscar gasto\n>>[I] Buscar un ingreso\n\n ")
            if seleccion == 'C':
                print("\nBuscando cuenta...")
                dni = input("\n> ID:")
                cuenta = db.Cuentas.buscar(dni)
                if cuenta:
                    nombre = input("\n> Nombre: \n")
                    monto = input("\n> Monto: \n")
                    db.Cuentas.modificar(cuenta.dni, nombre, monto)
                print(cuenta) if cuenta else print("Dato no encontrado")

            elif seleccion == 'G':
                print("\nBuscando gasto...")
                dni = input("\n> ID:")
                gasto = db.Gastos.buscar(dni)
                if gasto:
                    nombre = input("\n> Nombre: \n")
                    monto = input("\n> Monto: \n")
                    frecuencia = input("\n> Frecuencia: \n")
                    db.Gastos.modificar(gasto.dni, nombre, monto, frecuencia)
                print(gasto) if gasto else print("Dato no encontrado")

            elif seleccion == 'I':
                print("\nBuscando ingreso...")
                dni = input("\n> ID:")
                ingreso = db.Ingresos.buscar(dni)
                if ingreso:
                    nombre = input("\n> Nombre: \n")
                    monto = input("\n> Monto: \n")
                    frecuencia = input("\n> Frecuencia: \n")
                    db.Ingresos.modificar(ingreso.dni, nombre, monto, frecuencia)
                print(ingreso) if ingreso else print("Dato no encontrado")


        elif opcion == '7':
            print("Borrando dato...")
            dni = input("\nDNI > ")
            if db.Cuentas.buscar(dni) or db.Gastos.buscar(dni):
                print("DNI encontrado.") 
            else:
                print("DNI no encontrado.")
                break
            if db.Cuentas.borrar(dni) or db.Gastos.borrar(dni):
                print(f"({dni}) Borrado correctamente") 
            
        elif opcion == '8':
            print("Realizando transferencia...")
            db.Cuentas.transferencia()

        elif opcion == '9':
            print("\n Ingresando al menu de presupuesto...\n\n")
            presupuesto.iniciar()

        elif opcion == '10':
            print("Listando transferencias...")
            db.Cuentas.mostrar_transferencias()
            
        elif opcion == '11':
            print("registrando gasto...")
            dni1 = input("\nCuenta utilizada > ")
            dni2 = input("\nGasto > ")
            monto = input("\nMonto> ")
            db.Gastos.registrar_gasto(dni1, dni2, monto)

        elif opcion == 'E':
            print("\n\nSaliendo... \n")
            break 

        input("\n> Presiona ENTER para continuar...")
