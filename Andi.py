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