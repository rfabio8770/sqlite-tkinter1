from tkinter import Misc, Tk, Button, Entry, Label, ttk, PhotoImage
from tkinter import StringVar, Scrollbar, Frame, messagebox
from comunicacion import Comunicacion
from time import strftime
# from pandas import pd


class Ventana(Frame):
    
    def __init__(self, master):
        super().__init__(master)

        self.nombre = StringVar()
        self.edad = StringVar()
        self.correo  = StringVar()
        self.telefono = StringVar()

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=5)
        self.base_datos = Comunicacion()

        self.crear_widgets()

    def crear_widgets(self):
        self.frame_uno = Frame(self.master, bg="white", height=200, width=800)
        self.frame_uno.grid(column=0, row=0,sticky="nsew")
        self.frame_dos = Frame(self.master, bg="white", height=300, width=800)
        self.frame_dos.grid(column=0, row=1,sticky="nsew")

        self.frame_uno.columnconfigure([0, 1, 2], weight=1)
        self.frame_uno.rowconfigure([0, 1, 2, 3, 4, 5], weight=1)

        self.frame_dos.columnconfigure(0, weight=1)
        self.frame_dos.rowconfigure(0, weight=1)

        # creacion de controles
        Label(self.frame_uno, text="Operaciones", bg="white", fg="black", font=("Arial", 13, "bold")).grid(column=2, row=0)
        Button(self.frame_uno, text="REFRESCAR",  font=("Arial", 9, "bold"), command=self.actualizar_tabla,
               fg="black", bg="deep sky blue", width=20, bd=3).grid(column=2, row=1, pady=5)
        Label(self.frame_uno, text="Agregar y actualizar datos", fg="black", bg="white",
              font=("Kaufmann BT", 13, "bold")).grid(columnspan=2, column=0, row=0, pady=5)
        Label(self.frame_uno, text="Nombre", fg="black", bg="white",
              font=("Rockwell", 13, "bold")).grid(column=0, row=1, pady=5)
        Label(self.frame_uno, text="Edad", fg="black", bg="white",
              font=("Rockwell", 13, "bold")).grid(column=0, row=2, pady=5)
        Label(self.frame_uno, text="Correo", fg="black", bg="white",
              font=("Rockwell", 13, "bold")).grid(column=0, row=3, pady=5)
        Label(self.frame_uno, text="Telefono", fg="black", bg="white",
              font=("Rockwell", 13, "bold")).grid(column=0, row=4, pady=5)
        
        # controles entry
        Entry(self.frame_uno, textvariable=self.nombre, font=("Comic Sans MS",12),
              highlightbackground="deep sky blue", highlightthickness=5).grid(column=1, row=1)
        Entry(self.frame_uno, textvariable=self.edad, font=("Comic Sans MS",12),
              highlightbackground="deep sky blue", highlightthickness=5).grid(column=1, row=2)
        Entry(self.frame_uno, textvariable=self.correo, font=("Comic Sans MS",12),
              highlightbackground="deep sky blue", highlightthickness=5).grid(column=1, row=3)
        Entry(self.frame_uno, textvariable=self.telefono, font=("Comic Sans MS",12),
              highlightbackground="deep sky blue", highlightthickness=5).grid(column=1, row=4)
        
        # botones de operaciones
        Button(self.frame_uno, text="AÑADIR DATOS", font=("Arial", 9, "bold"), bg="deep sky blue",
               width=20, bd=3, command=self.agregar_datos).grid(column=2, row=2, pady=5, padx=5)
        Button(self.frame_uno, text="LIMPIAR CAMPOS", font=("Arial", 9, "bold"), bg="deep sky blue",
               width=20, bd=3, command=self.limpiar_campos).grid(column=2, row=3, pady=5, padx=5)
        Button(self.frame_uno, text="ACTUALIZAR DATOS", font=("Arial", 9,"bold"), bg="deep sky blue",
               width=20, bd=3, command=self.actualizar_datos).grid(column=2, row=4, pady=5, padx=5)
        Button(self.frame_uno, text="SALIR", font=("Arial", 9, "bold"), bg="deep sky blue",
               width=20, bd=3, command=self.salir).grid(column=2, row=5, pady=5, padx=5)
        
        # estilos para la tabla
        estilo_tabla = ttk.Style()
        estilo_tabla.configure("Treeview", font=("Helvetica", 10, "bold"),foreground="black", background="white")
        estilo_tabla.map("Treeview", background=[("selected", "deep sky blue")], foreground=[("selected", "black")])
        estilo_tabla.configure("Heading", background="white", foreground="deep sky blue", padding=3, font=("Arial", 10, "bold"))
        
        # tabla
        self.tabla = ttk.Treeview(self.frame_dos)
        self.tabla.grid(row=0, column=0, sticky="nsew")
        ladox = ttk.Scrollbar(self.frame_dos, orient="horizontal", command=self.tabla.xview)
        ladox.grid(column=0,row=1, sticky="ew")
        ladoy = ttk.Scrollbar(self.frame_dos, orient="vertical", command=self.tabla.yview)
        ladoy.grid(column=1,row=0, sticky="ns")
        self.tabla.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
        
        self.tabla["columns"] = ("Edad", "Correo", "Telefono")
        self.tabla.column("#0", minwidth=100, width=120, anchor="center")
        self.tabla.column("Edad", minwidth=100, width=120, anchor="center")
        self.tabla.column("Correo", minwidth=100, width=120, anchor="center")
        self.tabla.column("Telefono", minwidth=100, width=120, anchor="center")    

        self.tabla.heading("#0", text="Nombre", anchor="center")
        self.tabla.heading("Edad", text="Edad", anchor="center")
        self.tabla.heading("Correo", text="Correo", anchor="center")
        self.tabla.heading("Telefono", text="Telefono", anchor="center")

        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)
        self.tabla.bind("<Double-1>", self.eliminar_datos)
      


    def actualizar_tabla(self):
        pass

    def agregar_datos(self):
        pass

    def limpiar_campos(self):
        pass

    def actualizar_datos(self):
        pass

    def salir(self):
        pass

    def obtener_fila(self):
        item = self.tabla.focus()
        self.data = self.tabla.item(item)
        self.nombre.set(self.data['text'])
        self.nombre.set(self.data['values'][0])
        self.nombre.set(self.data['values'][1])
        self.nombre.set(self.data['values'][2])

    
    def eliminar_datos(self):
        self.limpiar_campos()

if __name__ == "__main__":
    ventana = Tk()
    ventana.title("Ejemplo tkinter y sqlite3")
    ventana.minsize(height=400, width= 600)
    ventana.geometry("800x500")
    app = Ventana(ventana)
    app.mainloop()