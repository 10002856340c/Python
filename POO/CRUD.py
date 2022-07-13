import json


# consultar la informacion de todas las tareas


def Read(rutaArchivo="D:\\usuario\\Documents\\python\\POO\\listadoTareas.json"):
    diccionarioTareas = {}
    try:
        with open(rutaArchivo) as archivo:
            diccionarioTareas = json.load(archivo)
    except:
        print("No se pudo caragar la informacion de la capa de datos")
        return False

    return diccionarioTareas


def adicionar_tareas(tareas, descripcion, tareanueva):  # ---> Funcion adicionar tareas
    tareas[descripcion] = tareanueva
    return tareas
