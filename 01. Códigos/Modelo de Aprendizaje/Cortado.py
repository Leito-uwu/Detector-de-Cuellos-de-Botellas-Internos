# CELDA: Módulo Recortador
import cv2
import numpy as np

def recortar_botella_dinamico(imagen_bgr_original, bbox, margen=30):
    """
    Recorta la región de interés (ROI) de la botella usando su Bounding Box.
    Añade un margen de seguridad (padding) para no perder bordes en la IA.
    Protege contra recortes fuera de los límites de la imagen.
    """
    if bbox is None:
        return None
        
    x, y, w, h = bbox
    alto_img, ancho_img = imagen_bgr_original.shape[:2]
    
    