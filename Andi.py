from tkinter import *
from datetime import date
from datetime import datetime

raiz = Tk()
raiz.geometry("600x600")
raiz.title("Ejecución de Funciones")
miFrame= Frame()
miFrame.pack()
bienvenido = Label(miFrame, text="BIENVENIDO")
bienvenido.grid(row=0, column=0)
bienvenido.config(font=('Algerian', 16)) 

nombre = StringVar()
apellido = StringVar()
dia = IntVar()
mes = IntVar()
año = IntVar()

lblnombre= Label(miFrame, text="Nombre:", bg="red")
lblnombre.grid(row=1, column=0)
lblnombre.config(padx=10, pady=10)
txtNombre=Entry(miFrame, textvariable =nombre)
txtNombre.grid(row=1, column=1)

lblapellido=Label(miFrame, text="Apellido:", bg="red")
lblapellido.grid(row=2, column=0)
lblapellido.config(padx=10, pady=10)
txtApellido=Entry(miFrame, textvariable =apellido)
txtApellido.grid(row=2, column=1)