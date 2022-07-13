from tkinter import *
import tkinter as tk
import interfaceGrafica
import sys
import CRUD

# 1 cargamos tareas es decir cargamos nuestro formato json
tareas = CRUD.Read

# 2 cargar la interface
ventana = interfaceGrafica.ventanaPrincipal(tareas)

# 3
if not (tareas):
    # la funcion sys.exit(1) --> sirve para salir de un programa
    sys.exit(1)

# 4 mostrar ventana
ventana.mainloop()
