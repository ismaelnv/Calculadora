from tkinter import *
from tkinter import messagebox

def cerrar(ventana):
    ventana.destroy()
def suma(texto,texto1,resultado):
    suma = int(texto.get()) + int(texto1.get()) 
    return resultado.set(suma)
def resta(texto,texto1,resultado):
    resta = int(texto.get()) - int(texto1.get()) 
    return resultado.set(resta)
def muultiplicacion(texto,texto1,resultado):
    multiplicacion = int(texto.get()) * int(texto1.get()) 
    return resultado.set(multiplicacion)
def division(texto,texto1,resultado):
    try:
     division = int(texto.get()) / int(texto1.get()) 
     return resultado.set(division)
    except ZeroDivisionError:
        messagebox.showinfo(title="ERROR",message="Datos ingresados incorrectos...!!!")
        texto.delete(0,END)
        texto1.delete(0,END)
        texto.focus()