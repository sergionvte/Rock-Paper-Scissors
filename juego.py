# Librerías
from tkinter import *
from random import choice
from time import sleep
# Creando ventana
ventana = Tk()
ventana.title('Game')
ventana.configure(bd = 10)
# ventana.iconbitmap("game.ico") -> Para windows
# Importando imágenes
versus = PhotoImage(file = 'versus.png')
# Imágenes de jugador
jugador_piedra = PhotoImage(file = 'piedra_izquierda.png')
jugador_papel = PhotoImage(file = 'papel_izquierda.png')
jugador_tijeras = PhotoImage(file = 'tijeras_izquierda.png')
# Imágenes de computadora
pc_piedra = PhotoImage(file = 'piedra_derecha.png')
pc_papel = PhotoImage(file = 'papel_derecha.png')
pc_tijeras = PhotoImage(file = 'tijeras_derecha.png')
# Diccionario
eleccion = {pc_piedra : pc_tijeras, pc_papel : pc_piedra, pc_tijeras : pc_papel}
# Función para que la computadora escoja
def escoge_pc():
    global pc
    for i in range(5):
        pc = choice([pc_papel, pc_piedra, pc_tijeras])
        etiqueta4.configure(image=pc)
        ventana.update()
        sleep(0.05)
# Función para que el jugador escoja
def escoge_jugador(jugador):
    escoge_pc()
    if eleccion[jugador] == pc:
        etiqueta1.configure(text = 'GANASTE :)')
    elif eleccion[pc] == jugador:
        etiqueta1.configure(text = 'PERDISTE :(')
    else:
        etiqueta1.configure(text = 'EMPATE :|')
# Botones de opciones
def boton_piedra():
    etiqueta2.configure(image = jugador_piedra)
    escoge_jugador(pc_piedra)
def boton_papel():
    etiqueta2.configure(image = jugador_papel)
    escoge_jugador(pc_papel)
def boton_tijeras():
    etiqueta2.configure(image = jugador_tijeras)
    escoge_jugador(pc_tijeras)
# Detalles de ventana
marco = Frame(ventana)
marco.grid(column = 0, row = 0, pady = 10)
# Etiquetas
etiqueta1 = Label(marco, font = 'Arial 10', fg = '#000000')
etiqueta1.grid(column = 0, row = 0, columnspan = 3, sticky = E + W)
etiqueta2 = Label(marco, image = jugador_papel)
etiqueta2.grid(column = 0, row = 1)
etiqueta3 = Label(marco, image = versus)
etiqueta3.grid(column = 1, row = 1)
etiqueta4 = Label(marco, image = pc_papel)
etiqueta4.grid(column = 2, row = 1)
# Botones
boton1 = Button(ventana, height = 3, cursor = 'hand2', fg = '#000000', text = 'PIEDRA', command = boton_piedra)
boton1.grid(column = 0, row = 1, sticky= E+W)
boton1 = Button(ventana, height = 3, cursor = 'hand2', fg = '#000000', text = 'PAPEL', command = boton_papel)
boton1.grid(column = 0, row = 2, sticky= E+W)
boton1 = Button(ventana, height = 3, cursor = 'hand2', fg = '#000000', text = 'TIJERAS', command = boton_tijeras)
boton1.grid(column = 0, row = 3, sticky= E+W)
# Loop
ventana.mainloop()

