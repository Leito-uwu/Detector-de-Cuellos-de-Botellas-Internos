import os
from google.colab import drive
drive.mount('/content/drive')

# Ruta de la carpeta:
RUTA_CARPETA = '/content/drive/MyDrive/Dataset/---'

# Prefijo que llevaran todas las imagenes 
# Ej. Botellas Malas
PREFIJO = 'B_M'

def renombrar_imagenes_masivo():
    # Verificar que la ruta exista
    if not os.path.exists(RUTA_CARPETA):
        print(f"Error: La ruta {RUTA_CARPETA} no existe.")
        return

    # Obtener lista de archivos y filtrar solo imágenes
    archivos = os.listdir(RUTA_CARPETA)
    imagenes = [f for f in archivos if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # Ordenar alfabéticamente para mantener cierto orden original si lo había
    imagenes.sort()

    print(f"Se encontraron {len(imagenes)} imágenes para renombrar.\n")

    contador = 1
    for nombre_viejo in imagenes:
        # Extension original del archivo
        _, extension = os.path.splitext(nombre_viejo)

        # Crear el nuevo nombre 000x
        nuevo_nombre = f"{PREFIJO}{contador:04d}{extension}"

        ruta_vieja = os.path.join(RUTA_CARPETA, nombre_viejo)
        ruta_nueva = os.path.join(RUTA_CARPETA, nuevo_nombre)

        try:
            os.rename(ruta_vieja,ruta_nueva)
            print(f"{nombre_viejo} -> {nuevo_nombre}")
        
        except Exception as e:
            print(f"Error al renombrar: {nombre_viejo}: {e}")

        contador += 1
    print("Proceso Terminado")
    
# Ejecutar
renombrar_imagenes_masivo()