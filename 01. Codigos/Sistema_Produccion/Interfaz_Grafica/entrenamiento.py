import customtkinter as ctk
import os
from PIL import Image

class PantallaEntrenamiento(ctk.CTkToplevel):
    def __init__(self, on_volver):
        super().__init__()
        self.on_volver = on_volver
        
        self.title("Entrenamiento de IA - Milcast Corp")
        self.geometry("700x600")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)

        # --- CABECERA ---
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.pack(side="top", fill="x", padx=20, pady=20)

        ruta_logo = os.path.join(os.path.dirname(__file__), "..", "Aranjuez_logo.png")
        try:
            pil_image = Image.open(ruta_logo)
            self.ctk_logo = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(80, 80))
            self.label_logo = ctk.CTkLabel(self.header_frame, text="", image=self.ctk_logo)
        except:
            self.label_logo = ctk.CTkLabel(self.header_frame, text="[ LOGO ]", width=80, height=80, fg_color="gray30")
        self.label_logo.pack(side="left", padx=(0, 20))

        self.label_titulo = ctk.CTkLabel(self.header_frame, text="CAPTURA DE DATOS (DATASET)", font=("Roboto", 22, "bold"))
        self.label_titulo.pack(side="left")

        self.btn_volver = ctk.CTkButton(self.header_frame, text="Volver al Menú", width=100, 
                                        fg_color="gray40", hover_color="gray30", command=self.cerrar_ventana)
        self.btn_volver.pack(side="right")

        self.separador = ctk.CTkFrame(self, height=2, fg_color="gray30")
        self.separador.pack(fill="x", padx=20, pady=(0, 10))

        # --- CUERPO ---
        # 1. Entrada del Nombre
        self.frame_nombre = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_nombre.pack(pady=10)
        
        self.label_nombre = ctk.CTkLabel(self.frame_nombre, text="Nombre del nuevo formato:", font=("Roboto", 14))
        self.label_nombre.pack(side="left", padx=10)
        
        self.entry_nombre = ctk.CTkEntry(self.frame_nombre, placeholder_text="Ej: Botella Tipo F", width=250)
        self.entry_nombre.pack(side="left", padx=10)

        # 2. Visor de la Cámara (El espacio visual)
        self.frame_camara = ctk.CTkFrame(self, width=450, height=300, fg_color="black")
        self.frame_camara.pack(pady=15)
        self.frame_camara.pack_propagate(False) # Esto obliga a que el recuadro negro mantenga su tamaño
        
        self.label_camara = ctk.CTkLabel(self.frame_camara, text="📷\nVISOR DE CÁMARA\n(Listo para conectar OpenCV)", font=("Roboto", 16), text_color="gray")
        self.label_camara.pack(expand=True)

        # 3. Botones de Captura
        self.frame_botones = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_botones.pack(pady=10)

        self.btn_buenas = ctk.CTkButton(self.frame_botones, text="📷 Capturar\nBOTELLA BUENA", width=180, height=60, 
                                        font=("Roboto", 14, "bold"), fg_color="green", hover_color="darkgreen", 
                                        command=self.capturar_buena)
        self.btn_buenas.pack(side="left", padx=20)

        self.btn_malas = ctk.CTkButton(self.frame_botones, text="📷 Capturar\nBOTELLA MALA", width=180, height=60, 
                                        font=("Roboto", 14, "bold"), fg_color="#d32f2f", hover_color="#9a0007", 
                                        command=self.capturar_mala)
        self.btn_malas.pack(side="right", padx=20)

        # 4. Mensajes de confirmación
        self.lbl_mensaje = ctk.CTkLabel(self, text="", font=("Roboto", 14))
        self.lbl_mensaje.pack(pady=10)

    def capturar_buena(self):
        nombre = self.entry_nombre.get().strip()
        if not nombre:
            self.lbl_mensaje.configure(text="⚠️ Primero escribe el nombre de la botella", text_color="yellow")
            return
        self.lbl_mensaje.configure(text=f"✅ Foto de '{nombre}' BUENA guardada correctamente.", text_color="green")

    def capturar_mala(self):
        nombre = self.entry_nombre.get().strip()
        if not nombre:
            self.lbl_mensaje.configure(text="⚠️ Primero escribe el nombre de la botella", text_color="yellow")
            return
        self.lbl_mensaje.configure(text=f"❌ Foto de '{nombre}' MALA guardada correctamente.", text_color="red")

    def cerrar_ventana(self):
        self.destroy()
        self.on_volver()