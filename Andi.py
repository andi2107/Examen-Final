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

lbldia=Label(miFrame, text="Día:", bg="red")
lbldia.grid(row=3, column=0)
lbldia.config(padx=10, pady=10)
txtDia=Entry(miFrame, textvariable =dia)
txtDia.grid(row=3, column=1)

lblmes=Label(miFrame, text="Mes:", bg="red")
lblmes.grid(row=4, column=0)
lblmes.config(padx=10, pady=10)
txtMes=Entry(miFrame, textvariable =mes)
txtMes.grid(row=4, column=1)

lblanio=Label(miFrame, text="Año:", bg="red")
lblanio.grid(row=5, column=0)
lblanio.config(padx=10, pady=10)
txtanio=Entry(miFrame, textvariable =año)
txtanio.grid(row=5, column=1)

btnFuncion1 = Button(miFrame, text="Opcion 1", command = Funcion1, bg="blue", font="Arial")
btnFuncion1.grid(row=6, column=0)
btnFuncion1.config(padx=10, pady=10)