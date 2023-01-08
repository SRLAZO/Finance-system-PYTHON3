import helpers
import database as db
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, WARNING
import UI_CUENTAS as UIC
import UI_GASTOS as UIG
import UI_INGRESOS as UII
import UI_REGISTRO_GASTOS as UIRG

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

class MainWindow(Tk, CenterWidgetMixin):
    def __init__(self):
        super().__init__()
        self.title("FLITCHI")
        self.build()
        self.center()
    
    def build(self):
        frame = Frame(self)
        frame.pack(pady=20)

        treeview = ttk.Treeview(frame)
        treeview['columns'] = ('DNI', 'Nombre', 'Monto')

        treeview.column("#0", width=0, stretch=NO)
        treeview.column("DNI", anchor=CENTER)
        treeview.column("Nombre", anchor=CENTER)
        treeview.column("Monto", anchor=CENTER)

        treeview.heading("DNI", text="DNI", anchor=CENTER)
        treeview.heading("Nombre", text="Nombre", anchor=CENTER)
        treeview.heading("Monto", text="Saldo", anchor=CENTER)

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        treeview['yscrollcommand'] = scrollbar.set

        for cuenta in db.Cuentas.lista:
            treeview.insert(
                parent='', index='end', iid=cuenta.dni,
                values=(cuenta.dni, cuenta.nombre, cuenta.monto))

        treeview.pack()


        frame = Frame(self)
        frame.pack(pady=2)

        Button(frame, text="Cuentas", command=self.cuentas, width= 8).grid(row=0, column=1, padx=10)
        Button(frame, text="Gastos", command=self.gastos, width= 8).grid(row=0, column=2, padx=10)
        Button(frame, text="Ingresos", command=self.ingresos, width= 8).grid(row=0, column=3, padx=10)

        frame = Frame(self)
        frame.pack(pady=20)
        Button(frame, text="Registrar Gasto", command=self.registro_gasto, width= 15).grid(row=1, column=2, padx=10)


    def cuentas(self):
        UIC.MainWindow()

    def gastos(self):
        UIG.MainWindow()

    def ingresos(self):
        UII.MainWindow()

    def registro_gasto(self):
        UIRG.MainWindow() #TODO Verificar que funciona!
        self.update()

    def close(self):
        self.destroy()
        self.update()

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
