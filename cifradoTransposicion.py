from tkinter import *
root = Tk()
textoSalida = StringVar()

def cifrar():
    matriz = crearMatrizIncrem(len(clave.get()), texto.get())
    secuenciaClave = obtenerSecuenciaClave(clave.get())
    textoCifrado = "";
    for num in range(len(secuenciaClave)):
        pos = secuenciaClave.index(num + 1)
        for fila in range(len(matriz)):
            if len(matriz[fila]) > pos:
                textoCifrado += matriz[fila][pos]    
    textoSalida.set(textoCifrado)

def descifrar():
    matriz = crearMatrizDecrem(obtenerSecuenciaClave(clave.get()), texto.get())
    textoDescifrado = "";
    for fila in range(len(matriz)):
        for colum in range(len(matriz[fila])):
            textoDescifrado += matriz[fila][colum]
    textoSalida.set(textoDescifrado)

def crearMatrizIncrem(ancho, mensaje):
    fila = 0
    colum = 0
    matriz = [[]]
    for pos, ch in enumerate(mensaje):
        matriz[fila].append(ch)
        colum += 1
        if colum >= ancho:
            colum = 0
            fila += 1
            matriz.append([])

    return matriz

def crearMatrizDecrem(secuenciaClave, mensaje):
    ancho = len(secuenciaClave)
    alto = len(mensaje) // ancho
    if alto * ancho < len(mensaje):
        alto += 1
    matriz = crearMatrizVacia(ancho, alto, len(mensaje))
    pos = 0
    for num in range(len(secuenciaClave)):
        column = secuenciaClave.index(num + 1)
        fila = 0
        while (fila < len(matriz)) and (len(matriz[fila]) > column):
            matriz[fila][column] = mensaje[pos]
            fila += 1
            pos += 1
    return matriz

def crearMatrizVacia(ancho, alto, largo):
    matriz = []
    totalAgregado = 0
    for fila in range(alto):
        matriz.append([])
        for colum in range(ancho):
            if totalAgregado >= largo:
                return matriz
            matriz[fila].append('')
            totalAgregado += 1
    return matriz

def obtenerSecuenciaClave(keyword):
    secuencia = []
    for pos, caracter in enumerate(keyword):
        palabraAnterior = keyword[:pos]
        nuevoNum = 1
        for posAnterior, caracterAnterior in enumerate(palabraAnterior):
            if caracterAnterior > caracter:
                secuencia[posAnterior] += 1
            else:
                nuevoNum += 1
        secuencia.append(nuevoNum)
    return secuencia


root.title("Cifrado de Transposición" )
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