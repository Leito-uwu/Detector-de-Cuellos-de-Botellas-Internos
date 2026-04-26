import cv2
import numpy as np
import os
from tensorflow.keras.models import load_model

from Modulos_Vision.Centrado import trabajar_con_contorno_blanco
from Modulos_Vision.Cortado import recortar_botella_dinamico
from Modulos_Vision.Filtrado import procesar_imagen

class InspectorVision:
    def __init__(self, nombre_modelo="modelo_inspector_botellas.keras"):
        """ Inicializa y carga el modelo de Keras desde su ruta absoluta. """
        directorio_actual = os.path.dirname(__file__)
        ruta_absoluta = os.path.join(directorio_actual, nombre_modelo)
        
        print("Cargando modelo de Inteligencia Artificial (Keras)...")
        self.modelo = load_model(ruta_absoluta)
        print("Motor de Visión Artificial Iniciado y listo.")

    def evaluar_botella(self, frame_camara):
        """ Procesa el frame mediante los módulos de visión y emite un veredicto. """
        
        # 1. Centrado
        bbox = trabajar_con_contorno_blanco(frame_camara)
        if bbox is None: return "MALA" 

        # 2. Cortado
        imagen_recortada = recortar_botella_dinamico(frame_camara, bbox)
        if imagen_recortada is None: return "MALA"

        # 3. Filtrado y Preparación Matemática
        imagen_lista = procesar_imagen(imagen_recortada, tamano_final=(224, 224))
        if imagen_lista is None: return "MALA"

        # 4. Predicción de IA
        prediccion = self.modelo.predict(imagen_lista, verbose=0)
        valor_resultado = prediccion[0][0]

        # 5. Veredicto Final
        if valor_resultado >= 0.5:
            return "BUENA"
        else:
            return "MALA"