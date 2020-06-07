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

def Funcion1 ():
    M=int(dia.get())
    N=int(mes.get())
    O=int(año.get())
    bindia=format(M, '0b' )
    binmes=format(N, '0b')
    binaño=format(O, '0b')

    lblResp['text'] = "La fecha es: {}/{}/{} y  en binario es:{}/{}/{}".format(M,N,O,bindia,binmes,binaño)

def Funcion2():
    fechaString = f"{año.get()}-{mes.get()}-{dia.get()}"
    date_object = datetime.strptime(fechaString, '%Y-%m-%d')

    today= datetime.today()
    d1 = today
    d2 = date_object
    result1 = abs(d1-d2).days 
    respuesta = f"Usted nacio el {date_object} y ha vivido {result1} días."
    lblResp.configure(text = respuesta)




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

btnFuncion2 = Button(miFrame, text = "Opcion 2", command= Funcion2, bg="blue", font="Arial")
btnFuncion2.grid(row=6, column=1)
btnFuncion2.config(padx=10, pady=10)

btnFuncion3 = Button(miFrame, text = "Opcion 3", command=Funcion3, bg="blue", font="Arial")
btnFuncion3.grid(row=7, column=0)
btnFuncion3.config(padx=10, pady=10)

btnFuncion4 = Button(miFrame, text = "Opcion 4", command = Funcion4, bg="blue", font="Arial")
btnFuncion4.grid(row=7, column=1)
btnFuncion4.config(padx=10, pady=10)

btnFuncion5 = Button(miFrame, text = "Opcion 5", command = Funcion5, bg="blue", font="Arial")
btnFuncion5.grid(row=8, column=0)
btnFuncion5.config(padx=10, pady=10)



    
    def Funcion3():
    sNombre = f"{nombre.get()}"
    sApellido = f"{apellido.get()}"
    conteoN = len(sNombre)
    conteoA = len(sApellido)
  
    if conteoN % 2 == 0:
        r1 = f"{sNombre} su Nombre es de número Par"
    else:
        r1 = f"{sNombre} su Nombre es de número Inpar"

    if conteoA % 2 == 0:
        r2 = f"{sApellido} su Apellido es de número Par."
    else:
        r2 = f"{sApellido} su Apellido es de número Inpar."
    respuesta = f"{r1} y  {r2} "
    lblResp.configure(text =respuesta )

    def Funcion4():
    sNombre = f"{nombre.get()}"
    sApellido = f"{apellido.get()}"
    cuenta = 0
    for carac in sNombre:
            if carac == 'a' or carac =='A' or carac =='e' or carac =='E' or carac =='i' or carac=='I' or carac=='o' or carac=="O" or carac=="u" or carac=="U":
                cuenta += 1
    for carac in sApellido:
            if carac == 'a' or carac =='A' or carac =='e' or carac =='E' or carac =='i' or carac=='I' or carac=='o' or carac=="O" or carac=="u" or carac=="U":
                cuenta += 1
    cajita=len(sNombre)
    cajita1=len(sApellido)
    consonante=cajita+cajita1-cuenta
    lblResp['text'] = 'Su nombre y apellido tienen {} vocales y {} consonantes'.format(cuenta,consonante)

    def Funcion5():
    cajita = nombre.get()+" "+apellido.get()
    cajita = cajita[::-1]
    lblResp["text"] = nombre.get() + " " + apellido.get() + " al revés es: " + cajita