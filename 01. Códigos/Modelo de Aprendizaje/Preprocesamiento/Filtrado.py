import cv2


def procesar_imagen(imagen_recortada,tamano_final = (224,224)):
    if imagen_recortada is None:
        return None
    
    # 1. Convertir a escalas de grises
    imagen_procesada = cv2.cvtColor(imagen_recortada,cv2.COLOR_BGR2GRAY)

    # 2. Filtro Gausseano
    # Un kernel de (5,5) es perfecto para no perder la forma del cuello
    imagen_procesada = cv2.GaussianBlur(imagen_procesada,(5,5),0)

    # 3. Redimensionamiento de la Imagen
    imagen_final = cv2.resize(imagen_procesada, tamano_final, interpolation=cv2.INTER_AREA)
    
    return imagen_final
