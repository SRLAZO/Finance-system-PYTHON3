import csv
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

#------------VENTANA PARA REGISTRAR GASTO------------------------------------------------------------------

class CreateRegistroWindow(Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Crear registro")
        self.build()
        self.center()
        self.transient(parent)
        self.grab_set()

    def build(self):
        frame = Frame(self)
        frame.pack(padx=20,pady=10)
        Label(frame, text="Cuenta").grid(row=0, column=0)
        Label(frame, text="Gasto").grid(row=0, column=1)
        Label(frame, text="Monto").grid(row=0, column=2)

        dni = Entry(frame)
        dni.grid(row=1, column=0)
        dni.bind("<KeyRelease>", lambda event: self.validate(event, 0))

        gasto = Entry(frame)
        gasto.grid(row=1, column=1)
        gasto.bind("<KeyRelease>", lambda event: self.validate(event, 1))

        monto = Entry(frame)
        monto.grid(row=1, column=2)
        monto.bind("<KeyRelease>", lambda event: self.validate(event, 2))

        frame = Frame(self)
        frame.pack(pady=10)

        registrar = Button(frame, text="Registrar", command=self.registrar, width=8)
        registrar.configure(state=DISABLED)
        registrar.grid(row=0, column=0, padx=10)
        Button(frame, text="Cancelar", command=self.close, width=8).grid(row=0, column=1, padx=10)

        self.validaciones = [0, 0, 0]
        self.registrar = registrar
        self.dni = dni
        self.gasto = gasto
        self.monto = monto

    def registrar(self):
        self.master.treeview.insert(
            parent='', index='end',
            values=(self.dni.get(), self.gasto.get(), self.monto.get()))
        db.Gastos.registrar_gasto(self.dni.get(), self.gasto.get(), self.monto.get())
        self.update()
        self.close()# Con esta funcion se cierra la ventana despues de crear la cuenta.

    def close(self):
        self.destroy() #TODO para que sirve?
        self.update() #TODO para que sirve?
    
    def validate(self, event, index):
        valor = event.widget.get()

        valido = (len(valor) >= 2 and len(valor) <= 30)
        event.widget.configure({"bg":"Green" if valido else "Red"})
        #Cambiar el estado del boton en base a las validaciones
        self.validaciones[index] = valido
        self.registrar.config(state=NORMAL if self.validaciones == [1, 1, 1] else DISABLED)


#-------VENTANA PRINCIPAL (Futura venta de Cuentas)-----------------------------------------------------

class MainWindow(Tk, CenterWidgetMixin):
    def __init__(self):
        super().__init__()
        self.title("FLITCHI")
        self.build()
        self.center()


    def build(self):
        frame = Frame(self)
        frame.pack()

        treeview = ttk.Treeview(frame)
        treeview['columns'] = ('fecha','cuenta', 'gasto', 'monto')

        treeview.column("#0", width=0, stretch=NO)
        treeview.column("fecha", anchor=CENTER)
        treeview.column("cuenta", anchor=CENTER)
        treeview.column("gasto", anchor=CENTER)
        treeview.column("monto", anchor=CENTER)

        treeview.heading("fecha", text="Fecha", anchor=CENTER)
        treeview.heading("cuenta", text="DNI", anchor=CENTER)
        treeview.heading("gasto", text="Nombre", anchor=CENTER)
        treeview.heading("monto", text="Monto", anchor=CENTER)

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        treeview['yscrollcommand'] = scrollbar.set
        treeview.pack()

        lista = []
        with open('Ficheros/registro_gastos.csv') as fichero:
            reader = csv.reader(fichero, delimiter=';')
            for fecha, cuenta, gasto, monto in reader:
                registro = db.Registro_gastos(fecha, cuenta, gasto, monto)
                lista.append(registro)
        for registro in lista: #TODO Llamar a los registros del doc
            treeview.insert(
                parent='', index='end', 
                values=(registro.fecha, registro.cuenta, registro.gasto, registro.monto))

        treeview.pack()

        frame = Frame(self)
        frame.pack(pady=20)

        Button(frame, text="Registrar", command=self.create, width= 8).grid(row=0, column=0, padx=10)
        Button(frame, text="Borrar", command=self.delete, width= 8).grid(row=0, column=1, padx= 10)

        self.treeview = treeview

    def delete(self):
        cuenta = self.treeview.focus()
        if cuenta:
            campos = self.treeview.item(cuenta, "values")
            confirmar = askokcancel(
                title="Confirmar borrado",
                message=f"¿Borrar {campos[1]} {campos[2]}?",
                icon = WARNING)
            if confirmar:
                self.treeview.delete(cuenta)
                db.Cuentas.borrar(campos[0])

    def create(self):
        CreateRegistroWindow(self)





if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()



