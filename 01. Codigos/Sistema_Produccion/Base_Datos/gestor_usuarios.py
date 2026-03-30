import json
import os

def obtener_ruta_bd():
    ruta_script = os.path.dirname(__file__)
    return os.path.join(ruta_script, "usuarios.json")

def cargar_usuarios():  # <--- REVISA QUE ESTE NOMBRE SEA IDÉNTICO AL DEL IMPORT
    ruta_bd = obtener_ruta_bd()
    if not os.path.exists(ruta_bd):
        usuarios_por_defecto = {"admin": "1234"}
        guardar_usuarios(usuarios_por_defecto)
        return usuarios_por_defecto
    
    with open(ruta_bd, "r") as archivo:
        return json.load(archivo)

def guardar_usuarios(diccionario_usuarios):
    ruta_bd = obtener_ruta_bd()
    with open(ruta_bd, "w") as archivo:
        json.dump(diccionario_usuarios, archivo, indent=4)