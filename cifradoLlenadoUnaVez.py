import binascii
from random import getrandbits
from tkinter import *
root = Tk()
textoSalida = StringVar()
bitsRelleno = StringVar()
#funciones
def convertir_a_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def generar_relleno_aleatorio(n):
    return bin(getrandbits(n))[2:].zfill(n)


def xor(m, k):
    a = int(m, base=2)
    b = int(k, base=2)
    return bin(a ^ b)[2:].zfill(len(m))


def convertir_bits_a_texto(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return bytes_a_int(n).decode(encoding, errors)


def bytes_a_int(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

#......................Cifrado y Descifrado....................
def cifrar():
    bits = convertir_a_bits(mensaje.get())
    relleno = generar_relleno_aleatorio(len(bits))
    mensaje_cifrado = xor(bits,relleno)
    textoSalida.set(mensaje_cifrado)
    bitsRelleno.set(relleno)

def descifrar():
    bits_originales = xor(relleno_mensaje.get(), mensaje.get())
    mensaje_descifrado = convertir_bits_a_texto(bits_originales)

    textoSalida.set(mensaje_descifrado)

#..................Parte Grafica...............................
root.title("Cifrado de Relleno de una vez" )
root.geometry('400x450')

miFrame = Frame(root)
miFrame.pack()

mensaje = Entry(miFrame)
mensaje.grid(row=0, column=1, padx=40, pady=20)
cadenaLabel = Label(miFrame, text="Ingrese la oración: ")
cadenaLabel.grid(row=0, column=0, padx=10, pady=10)

relleno_mensaje = Entry(miFrame)
relleno_mensaje.grid(row=1, column=1, padx=20, pady=20)
claveLabel = Label(miFrame, text="Ingrese bits de seguridad: ")
claveLabel.grid(row=1, column=0, padx=10, pady=10)

cifrarButton = Button(miFrame, text="Cifrar", command=cifrar, background="#FFBF00")
cifrarButton.grid(row=2, column=0, padx=10, pady=10)

descifrarButton = Button(miFrame, text="Descifrar", command=descifrar, background="#84DE02")
descifrarButton.grid(row=2, column=1, padx=10, pady=10)

salida = Entry(miFrame, text=textoSalida)
salida.grid(row=3, column=1, padx=20, pady=20,)
salidaLabel = Label(miFrame, text="Tu texto en bits es: " )
salidaLabel.grid(row=3, column=0, padx=10, pady=10)

relleno = Entry(miFrame, text=bitsRelleno)
relleno.grid(row=4, column=1, padx=20, pady=20)
rellenoLabel = Label(miFrame, text="Bits usados en el cifrado: ")
rellenoLabel.grid(row=4, column=0, padx=10, pady=10)
root.mainloop()
