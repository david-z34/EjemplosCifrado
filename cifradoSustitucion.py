from tkinter import *
root=Tk()

import string 
alfabeto=string.ascii_letters
textoSalida = StringVar()

#...........................Cifrado Cesar.....................
def cifrarCesar():
    textoCifrado = ''
    for letra in cadena.get():
        juntarCadena = alfabeto.find(letra) + int(clave.get())
        cadenaUnida = int(juntarCadena) % len(alfabeto)
        textoCifrado = textoCifrado + str(alfabeto[cadenaUnida])
    textoSalida.set(textoCifrado)

#...........................descifrado Cesar.....................
def descifrarCesar():
    textoCifrado = ''
    for letra in cadena.get():
        juntarCadena = alfabeto.find(letra) - int(clave.get())
        cadenaUnida = int(juntarCadena) % len(alfabeto)
        textoCifrado = textoCifrado + str(alfabeto[cadenaUnida])
    textoSalida.set(textoCifrado)
    
root.title("Cifrado de César")
root.geometry('400x250')

cadena = Entry(root)
cadena.grid(row=0,column=1, padx=20,pady=20)
cadenaLabel=Label(root, text="Ingrese oración")
cadenaLabel.grid(row=0,column=0,padx=10,pady=10)

clave = Entry(root)
clave.grid(row=1, column=1, padx=20, pady=20)
claveLabel = Label(root, text="Ingrese el numero de desplazamiento: ")
claveLabel.grid(row=1, column=0, padx=10, pady=10)

cifrarButton = Button(root, text="Cifrar", command = cifrarCesar, background="#FFBF00")
cifrarButton.grid(row=2, column=0, padx=10, pady=10)

descifrarButton = Button(root, text="descifrar", command = descifrarCesar, background="#84DE02")
descifrarButton.grid(row=2, column=1, padx=10, pady=10)

salida = Entry(root,text=textoSalida)
salida.grid(row=3, column=1, padx=20, pady=20)
salidaLabel = Label(root, text="Tu texto es: ")
salidaLabel.grid(row=3, column=0, padx=10, pady=10)

root.mainloop()
