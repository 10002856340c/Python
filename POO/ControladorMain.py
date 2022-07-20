
from tkinter import *
# iniciar tkinder
aplicacion = Tk()

# Tamaño de la ventana
aplicacion.geometry('1020x630')

# Evitar que la pantalla se maximize o se agrande el tamaño de la ventana
aplicacion.resizable(0, 0)

# Titulo de la Ventana
aplicacion.title("Sistema de Facturacion")

# Color dondo de la ventana
aplicacion.config(bg='orange')

# Panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)
# etiqueta del titulo
etiqueta_titulo = Label(
    panel_superior, text='Sistema de Facturacion', fg='azure4', font=('Dosis', 58), bg='burlywood', width=27)
etiqueta_titulo.grid(row=0, column=0)

# Panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel Costos

panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT)
panel_costos.pack(side=BOTTOM)

# panel comidas

panel_comidas = LabelFrame(panel_izquierdo, text='comidas', font=(
    'Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

# panel Bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='bebidas', font=(
    'Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

# panel postres
panel_postres = LabelFrame(panel_izquierdo, text='bebidas', font=(
    'Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

# panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

# panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

# panel_botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()


# Para Ejecutar que la ventana se abra y no se cierre
aplicacion.mainloop()
