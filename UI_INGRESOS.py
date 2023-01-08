import helpers
import database as db
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, WARNING

class CenterWidgetMixin:
    def center(self):
        self.update()
        #self.geometry("WIDTHxHEIGHT+OFFSET_X+OFFSET_Y")
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int(ws/2 - w/2)
        y = int(hs/2 - h/2)

        self.geometry(f"{w}x{h}+{x}+{y}")

#------------VENTANA PARA CREAR INGRESO------------------------------------------------------------------

class CreateIngresoWindow(Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Crear Ingreso")
        self.build()
        self.center()
        self.transient(parent)
        self.grab_set()

    def build(self):
        frame = Frame(self)
        frame.pack(padx=20,pady=10)
        Label(frame, text="DNI").grid(row=0, column=0)
        Label(frame, text="Nombre").grid(row=0, column=1)
        Label(frame, text="Monto").grid(row=0, column=2)
        Label(frame, text="Frecuencia").grid(row=0, column=3)

        dni = Entry(frame)
        dni.grid(row=1, column=0)
        dni.bind("<KeyRelease>", lambda event: self.validate(event, 0))

        nombre = Entry(frame)
        nombre.grid(row=1, column=1)
        nombre.bind("<KeyRelease>", lambda event: self.validate(event, 1))

        monto = Entry(frame)
        monto.grid(row=1, column=2)
        monto.bind("<KeyRelease>", lambda event: self.validate(event, 2))

        frecuencia = Entry(frame)
        frecuencia.grid(row=1, column=3)
        frecuencia.bind("<KeyRelease>", lambda event: self.validate(event, 3))

        frame = Frame(self)
        frame.pack(pady=10)

        crear = Button(frame, text="Crear", command=self.create_ingreso, width=8)
        crear.configure(state=DISABLED)
        crear.grid(row=0, column=0, padx=10)
        Button(frame, text="Cancelar", command=self.close, width=8).grid(row=0, column=1, padx=10)

        self.validaciones = [0, 0, 0, 0]
        self.crear = crear
        self.dni = dni
        self.nombre = nombre
        self.monto = monto
        self.frecuencia = frecuencia

    def create_ingreso(self):
        self.master.treeview.insert(
            parent='', index='end', iid=self.dni.get(),
            values=(self.dni.get(), self.nombre.get(), self.monto.get(), self.frecuencia.get()))
        db.Ingresos.crear(self.dni.get(), self.nombre.get(), self.monto.get(), self.frecuencia.get())
        self.close()# Con esta funcion se cierra la ventana despues de crear la cuenta.

    def close(self):
        self.destroy() #TODO para que sirve?
        self.update() #TODO para que sirve?
    
    def validate(self, event, index):
        valor = event.widget.get()

        valido = helpers.dni_valido(valor, db.Ingresos.lista) if index == 0 \
            else (len(valor) >= 2 and len(valor) <= 30)
        event.widget.configure({"bg":"Green" if valido else "Red"})
        #Cambiar el estado del boton en base a las validaciones
        self.validaciones[index] = valido
        self.crear.config(state=NORMAL if self.validaciones == [1, 1, 1, 1] else DISABLED)

# Hay que valorar la funcion "Validate" de la línea 77 del gestor

#-------------VENTADA PARA MODIFICAR INGRESO-------------------------------------------------------

class EditIngresoWindow(Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Actualizar Ingreso")
        self.build()
        self.center()
        self.transient(parent)
        self.grab_set()

    def build(self):
        frame = Frame(self)
        frame.pack(padx=20,pady=10)

        Label(frame, text="DNI (no editable)").grid(row=0, column=0)
        Label(frame, text="Nombre").grid(row=0, column=1)
        Label(frame, text="Monto").grid(row=0, column=2)
        Label(frame, text="Frecuencia").grid(row=0, column=3)

        dni = Entry(frame)
        dni.grid(row=1, column=0)
        nombre = Entry(frame)
        nombre.grid(row=1, column=1)
        nombre.bind("<KeyRelease>", lambda event: self.validate(event, 0))
        monto = Entry(frame)
        monto.grid(row=1, column=2)
        monto.bind("<KeyRelease>", lambda event: self.validate(event, 1))
        frecuencia = Entry(frame)
        frecuencia.grid(row=1, column=3)
        frecuencia.bind("<KeyRelease>", lambda event: self.validate(event, 2))

        ingreso = self.master.treeview.focus()
        campos = self.master.treeview.item(ingreso, 'values')
        dni.insert(0, campos[0])
        dni.config(state=DISABLED)
        nombre.insert(0, campos[1])
        monto.insert(0, campos[2])
        frecuencia.insert(0, campos[3]) #TODO OUT OF RANGE???

        frame = Frame(self)
        frame.pack(pady=10)

        actualizar = Button(frame, text="Actualizar", command=self.edit_ingreso, width=8)
        actualizar.grid(row=0, column=0, padx=10)
        Button(frame, text="Cancelar", command=self.close, width=8).grid(row=0, column=1, padx=10)

        self.validaciones = [1, 1, 1]
        self.actualizar = actualizar
        self.dni = dni
        self.nombre = nombre
        self. monto = monto
        self.frecuencia = frecuencia



    def edit_ingreso(self):
        ingreso = self.master.treeview.focus()
        self.master.treeview.item(ingreso, values=(
            self.dni.get(), self.nombre.get(), self.monto.get(), self.frecuencia.get()))
        db.Ingresos.modificar(self.dni.get(), self.nombre.get(), self.monto.get(), self.frecuencia.get())
        self.close()

    def close(self):
        self.destroy()
        self.update()

    def validate(self, event, index):
        valor = event.widget.get()
        valido = (len(valor) >= 2 and len(valor) <= 30)
        event.widget.configure({"bg":"Green" if valido else "Red"})
        #Cambiar el estado del boton en base a las validaciones
        self.validaciones[index] = valido
        self.actualizar.config(state=NORMAL if self.validaciones == [1, 1, 1] else DISABLED)

#-------VENTANA PRINCIPAL INGRESOS-----------------------------------------------------

class MainWindow(Tk, CenterWidgetMixin):
    def __init__(self):
        super().__init__()
        self.title("FLITCHI - INGRESOS")
        self.build()
        self.center()
    
    def build(self):
        frame = Frame(self)
        frame.pack()

        treeview = ttk.Treeview(frame)
        treeview['columns'] = ('DNI', 'Nombre', 'Monto', 'Frecuencia')

        treeview.column("#0", width=0, stretch=NO)
        treeview.column("DNI", anchor=CENTER)
        treeview.column("Nombre", anchor=CENTER)
        treeview.column("Monto", anchor=CENTER)
        treeview.column("Frecuencia", anchor=CENTER)

        treeview.heading("DNI", text="DNI", anchor=CENTER)
        treeview.heading("Nombre", text="Nombre", anchor=CENTER)
        treeview.heading("Monto", text="Monto", anchor=CENTER)
        treeview.heading("Frecuencia", text="Frecuencia", anchor=CENTER)

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        treeview['yscrollcommand'] = scrollbar.set
        treeview.pack()

        for ingreso in db.Ingresos.lista:
            treeview.insert(
                parent='', index='end', iid=ingreso.dni,
                 values=(ingreso.dni, ingreso.nombre, ingreso.monto, ingreso.frecuencia))


        treeview.pack()

        frame = Frame(self)
        frame.pack(pady=20)

        Button(frame, text="Crear", command=self.create, width= 8).grid(row=0, column=0, padx=10)
        Button(frame, text="Modificar", command=self.edit, width= 8).grid(row=0, column=1, padx= 10)
        Button(frame, text="Borrar", command=self.delete, width= 8).grid(row=0, column=2, padx= 10)

        self.treeview = treeview

    def delete(self):
        ingreso = self.treeview.focus()
        if ingreso:
            campos = self.treeview.item(ingreso, "values")
            confirmar = askokcancel(
                title="Confirmar borrado",
                message=f"¿Borrar {campos[1]} {campos[2]}?",
                icon = WARNING)
            if confirmar:
                self.treeview.delete(ingreso)
                db.Ingresos.borrar(campos[0])

    def create(self):
        CreateIngresoWindow(self)


    def edit(self):
        if self.treeview.focus():
            EditIngresoWindow(self)



if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()

