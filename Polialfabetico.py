from tkinter import *
root = Tk()
textoSalida = StringVar()

def cifrar():
    textoCifrado = []
    for i in range(len(texto.get())):
        x = (ord(texto[i]) +
             ord(clave[i])) % 26
        x += ord('A')
        textoCifrado.append(chr(x))
    textoSalida.set("".join(textoCifrado))

def descifrar():
    textoDescifrado = []
    for i in range(len(textoDescifrado)):
        x = (ord(textoDescifrado[i]) -
             ord(clave[i]) + 26) % 26
        x += ord('A')
        textoDescifrado.append(chr(x))
    textoSalida.set("" . join(textoDescifrado))

def generarClave():
    llave = list(clave)
    if len(texto)==len(llave):
        return llave
    else:
        for i in range (len(texto)-len(llave)):
            llave.append(llave[i%len(llave)])
        return("".join(llave))



root.title("Cifrado Polialfabetico" )
root.geometry('400x250')

miFrame = Frame(root)
miFrame.pack()
miFrame.config(background="white")

texto = Entry(miFrame)
texto.grid(row=0, column=1, padx=20, pady=20)
cadenaLabel = Label(miFrame, text="Ingrese la oración: ")
cadenaLabel.grid(row=0, column=0, padx=10, pady=10)

clave = Entry(miFrame)
clave.grid(row=1, column=1, padx=20, pady=20)
claveLabel = Label(miFrame, text="Ingrese la clave de seguridad: ")
claveLabel.grid(row=1, column=0, padx=10, pady=10)

cifrarButton = Button(miFrame, text="Cifrar", command=cifrar, background="#FFBF00")
cifrarButton.grid(row=2, column=0, padx=10, pady=10)

descifrarButton = Button(miFrame, text="Descifrar", command=descifrar, background="#84DE02")
descifrarButton.grid(row=2, column=1, padx=10, pady=10)

salida = Entry(miFrame, text=textoSalida)
salida.grid(row=3, column=1, padx=20, pady=20)
salidaLabel = Label(miFrame, text="Tu texto es: ")
salidaLabel.grid(row=3, column=0, padx=10, pady=10)

root.mainloop()