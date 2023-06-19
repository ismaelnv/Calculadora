from tkinter import *
from tkinter import messagebox
from Operaciones import suma,resta,muultiplicacion,division,cerrar

ventana = Tk()
ventana.title("Mi calculadora")
ventana.geometry("400x280")
ventana.configure(background = "yellow")

#Creamos nuestras etiquetas(labe1)

lblPrimerNumero = Label(ventana, text = "Primer número", bg = "yellow", fg = "black", font = ("Arial Bold", 15))
lblSengundoNumero = Label(ventana, text = "Segundo número", bg = "yellow", fg = "black", font = ("Arial Bold", 15))
lblPrimerNumero.grid(column=1, row=1, pady= 5)
lblSengundoNumero.grid(column=1, row=2, pady= 5)

#Creamos la caja de texto
texto = Entry(ventana,font=("Arial Blod",15), justify=CENTER)
texto.grid( row =1,column=2, padx= 5, pady= 5)
texto1 = Entry(ventana, font=("Arial blod", 15), justify=CENTER)
texto1.grid(row=2,column=2,padx=5, pady= 5)

#Creacion de variable
resultado = StringVar()
     
#Creamos botones
botonSuma = Button(ventana, text="+",bg="green",fg="white",width=12, font= ("Arial Blod", 15),)
botonSuma.bind("<Button-1>", lambda event: suma(texto,texto1,resultado))
botonSuma.grid( row=3,column= 1, padx=5,pady=5)

botonaResta = Button(ventana, text="-",bg="green",fg="white",width=12, font=("Arial Blod",15))
botonaResta.bind("<Button-1>", lambda event: resta(texto,texto1,resultado))
botonaResta.grid(row=3,column= 2, padx=5, pady=5)

botonMultiplicacion = Button(ventana, text="x",bg="green",fg="white",width=12, font=("Arial Blond",15))
botonMultiplicacion.bind("<Button-1>", lambda event: muultiplicacion(texto,texto1,resultado))
botonMultiplicacion.grid( row=4,column= 1,padx=5,pady=5)

botonDivicion = Button(ventana, text="/",bg="green",fg="white",width=12, font=("Arial Blond",15))
botonDivicion.bind("<Button-1>", lambda event: division(texto,texto1,resultado))
botonDivicion.grid( row=4,column= 2, padx=5,pady=5)

botonCerrar = Button(ventana, text = "Cerrar", bg = "gray", fg = "white", width = 33, font = ("Arial Bold", 15))
botonCerrar.bind("<Button-1>", lambda event: cerrar(ventana))
botonCerrar.grid(row = 5, column = 1, padx = 5, pady = 5, columnspan = 2)

#Creamos etiqueta para respuesta o resultado
lblResultado = Label(ventana, bg = "white", width = 33, font = ("Arial Bold", 15), textvariable = resultado)
lblResultado.grid(row = 6, column= 1, padx = 5, pady = 5, columnspan = 2)


ventana.mainloop()