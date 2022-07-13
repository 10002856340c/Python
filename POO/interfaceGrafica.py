from distutils.command.config import config
from tkinter import *
from tkinter import ttk
from turtle import width


from matplotlib.pyplot import grid, text
from numpy import imag
import CRUD
import tkinter as tk


def ventanaPrincipal(tareas):
    # 1 creamos una ventana con la funcion --> tk.Tk
    ventana = tk.Tk()
    ventana.title("hola")
    # 2 creamos la primera seccion de nuestra interface Grafica
    ventana.geometry("+10+100")
    ventana.geometry("800x600")
    marco = Frame(ventana, borderwidth=1.5, relief="raised")
    marco.config(width='600', height='400')
    marco.config(bg="#800080")
    marco.grid(row=0, column=0, columnspan=2, rowspan=2)
    # 3 creamos la segunda seccion de nuestra interface grafica
    marcoCRUD = Frame(ventana, borderwidth=1.5, relief="raised")
    marcoCRUD.config(width='600', height='400')
    marcoCRUD.config(bg="#808080")
    marcoCRUD.grid(row=2, column=0, columnspan=2, rowspan=2)
    # 4 creamos nuestra tercera seccion de interface grafica
    marcoImg = Frame(ventana, borderwidth=1.5, relief="raised")
    marcoImg.config(width='200', height='300')
    marcoImg.config(bg="#008080")
    marcoImg.grid(row=0, column=2, rowspan=2)
    # 5 creamos nuestra cuarta seccion de nuestra interface grafica
    marcoBotones = Frame(ventana, borderwidth=1.5, relief="raised")
    marcoBotones.config(width='200', height='300')
    marcoBotones.config(bg="#FF0000")
    marcoBotones.grid(row=2, column=2, rowspan=2)
    # 6 creamos las tablas
    TablaTareas = ttk.Treeview(marco)
    TablaTareas["columns"] = ["ID", "Estado", "Descripcion", "Tiempo"]
    TablaTareas.column("#0", width=200, stretch=tk.NO)
    TablaTareas.column("ID", anchor=tk.CENTER, width=40)
    TablaTareas.column("Estado", anchor=tk.W, width=300)
    TablaTareas.column("Descripcion", anchor=tk.W, width=100)
    TablaTareas.column("Tiempo", anchor=tk.CENTER, width=80)
    # 6 Especificacion del encabezado
    TablaTareas.heading("#0", text=" ", anchor=tk.CENTER)
    TablaTareas.heading("ID", text="ID ", anchor=tk.CENTER)
    TablaTareas.heading("Estado", text="Estado", anchor=tk.W)
    TablaTareas.heading("Descripcion", text="Descripcion ", anchor=tk.CENTER)
    TablaTareas.heading("Tiempo", text="Tiempo ", anchor=tk.CENTER)
    TablaTareas.grid(row=0, column=0, rowspan=2, columnspan=2)
    # insertar las tareas con un bucle for
    # ---------------------------------------------------------------------
    # creamos la interface grafica del frame CRUD
    # Agregar entrada para los atributos de las tareas
    # Id Tarea
    etiquetaId = tk.Label(marcoCRUD, text='ID', anchor='w')
    entradaid = tk.Entry(marcoCRUD)
    etiquetaId.config(bg='#F3FBD7')
    # DescripcioN de tarea
    etiquetaDescripcion = tk.Label(marcoCRUD, text='Descripcion :')
    entradadescripcion = tk.Entry(marcoCRUD)
    etiquetaDescripcion.config(bg='#F3FBD7')
    # Estado de tarea
    etiquetaEstado = tk.Label(marcoCRUD, text='Descripcion :')
    entradaEstado = tk.Entry(marcoCRUD)
    etiquetaEstado.config(bg='#F3FBD7')
    # Tiempo  tarea
    etiquetaTiempo = tk.Label(marcoCRUD, text='Descripcion :')
    entradaTiempo = tk.Entry(marcoCRUD)
    etiquetaTiempo.config(bg='#F3FBD7')
    # mostramos en la ventana
    etiquetaId.place(x=60, y=40, width=100, height=30)
    entradaid.place(x=160, y=40, width=200, height=30)

    etiquetaDescripcion.place(x=60, y=80, width=100, height=30)
    entradadescripcion.place(x=160, y=80, width=200, height=30)

    etiquetaEstado.place(x=60, y=120, width=100, height=30)
    entradaEstado.place(x=160, y=120, width=200, height=30)

    etiquetaTiempo.place(x=60, y=160, width=100, height=30)
    entradaTiempo.place(x=160, y=160, width=200, height=30)

    # Creamos los botones Cargar Tareas y Limpiar
    btnLimpiarCampos = tk.Button(marcoCRUD, text='Limpiar')
    btnCargarTareaSeleccionada = tk.Button(marcoCRUD, text='Cargar Tarea')
    btnLimpiarCampos.place(x=450, y=40, width=80, height=40)
    btnCargarTareaSeleccionada.place(x=450, y=90, width=80, height=40)

    # creamos los botones en el marcobotones
    btnAdicionarTarea = tk.Button(marcoBotones, text='Adicionar Tareas')
    btnActualizarTarea = tk.Button(marcoBotones, text='Actualizar Tarea')
    btnEliminarTarea = tk.Button(marcoBotones, text='Eliminar Tarea')
    btnSalir = tk.Button(marcoBotones, text='guardar y salir')

    btnAdicionarTarea.place(x=40, y=20, width=120, height=40)
    btnActualizarTarea.place(x=40, y=70, width=120, height=40)
    btnEliminarTarea.place(x=40, y=130, width=120, height=40)
    btnSalir.place(x=40, y=180, width=120, height=40)

    # cargamos la Imagen
    # carga la imagen para asociar a widget tipo etiqueta
    # --> libreria para procesar imagenes formato png y ridimensionar
    from PIL import ImageTk, Image
    # proporciones de la imagen
    w = 120
    h = 140
    imagenCargada = Image.open(
        "D:\\usuario\\Documents\\python\\POO\\imagen.png")
    imagenCargada.thumbnail((w, h))  # Redimensionando la Imagen
    imagenListasTareas = ImageTk.PhotoImage(
        imagenCargada)  # Encapsular para tkinder
    # Creacion de la Etiquta en el marcoimg
    etiqutaImagenListas = tk.Label(marcoImg)
    # asociacion de la imagen a la Etiqueta
    etiqutaImagenListas.config(image=imagenListasTareas, width=w, height=h)
    etiqutaImagenListas.image = imagenListasTareas
    # mostrar la imagen
    etiqutaImagenListas.place(x=50, y=50, width=120, height=140)
    # cambiar el fondo
    etiqutaImagenListas.config(bg='#F3FBD7')
    return ventana
