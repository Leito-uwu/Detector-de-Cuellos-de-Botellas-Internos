import customtkinter as ctk
import os
from PIL import Image

class PantallaEntrenamiento(ctk.CTkToplevel):
    def __init__(self, on_volver, formato_actual):
        super().__init__()
        self.on_volver = on_volver
        # El formato inicial viene del Menú, pero ahora se puede cambiar aquí
        self.formato_actual = formato_actual

        # CONTADORES LOCALES (Simulados para la demostración)
        self.conteo_buenas_demo = 0
        self.conteo_malas_demo = 0

        self.title("Entrenamiento de IA - Milcast Corp")
        self.geometry("950x700") # Un poco más amplio para el nuevo campo
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.btn_volver_click)

        # ==========================================
        # 🎨 PALETA DE COLORES
        # ==========================================
        self.COLOR_FONDO = "#F5EFE7"    
        self.COLOR_HEADER = "#2B1D15"   
        self.COLOR_TEXTO_HD = "#F5EFE7" 
        self.COLOR_TEXTO = "#212121"    
        self.COLOR_BLANCO = "#FFFFFF"   
        self.COLOR_ACENTO = "#721B35"   # Color vino para resaltar el nombre
        
        self.configure(fg_color=self.COLOR_FONDO)

        # ==========================================
        # 🍫 CABECERA CORPORATIVA
        # ==========================================
        self.header_frame = ctk.CTkFrame(self, fg_color=self.COLOR_HEADER, corner_radius=0, height=120)
        self.header_frame.pack(side="top", fill="x")
        self.header_frame.pack_propagate(False)

        self.frame_titulos = ctk.CTkFrame(self.header_frame, fg_color="transparent")
        self.frame_titulos.pack(expand=True)

        ruta_logo = os.path.join(os.path.dirname(__file__), "..", "Assets","Aranjuez_logo_1.png")
             
        try:
            pil_image = Image.open(ruta_logo)
            self.ctk_logo = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(70, 60))
            self.label_logo = ctk.CTkLabel(self.frame_titulos, text="", image=self.ctk_logo)
        except:
            self.label_logo = ctk.CTkLabel(self.frame_titulos, text="[ LOGO ]", text_color=self.COLOR_TEXTO_HD)
        self.label_logo.pack(pady=(5, 0))

        self.label_titulo = ctk.CTkLabel(self.frame_titulos, text="SISTEMA DE ENTRENAMIENTO", 
                                         font=("Roboto", 22, "bold"), text_color=self.COLOR_TEXTO_HD)
        self.label_titulo.pack(pady=(5, 5))

        self.btn_volver = ctk.CTkButton(self.header_frame, text="Volver al Menú", width=120, height=35,
                                        corner_radius=8, fg_color=self.COLOR_FONDO, text_color=self.COLOR_HEADER, 
                                        hover_color="#D1CCC0", font=("Roboto", 13), command=self.btn_volver_click)
        self.btn_volver.place(relx=0.97, rely=0.5, anchor="e")

        # ==========================================
        # 📦 CUERPO DE ENTRENAMIENTO
        # ==========================================
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(fill="both", expand=True, padx=30, pady=20)

        # ------------------------------------------
        # 🖥️ ÁREA IZQUIERDA: CÁMARA (SIMULADA)
        # ------------------------------------------
        self.frame_camara = ctk.CTkFrame(self.main_frame, fg_color=self.COLOR_BLANCO, corner_radius=15, border_width=1, border_color="#D1CCC0")
        self.frame_camara.pack(side="left", fill="both", expand=True, padx=(0, 20))

        self.label_cam_titulo = ctk.CTkLabel(self.frame_camara, text="📺 Monitor de Captura", 
                                              font=("Roboto", 16, "bold"), text_color=self.COLOR_TEXTO)
        self.label_cam_titulo.pack(pady=15)

        self.label_video = ctk.CTkLabel(self.frame_camara, text="[ Cámara Desactivada para el Demo ]", 
                                        font=("Roboto", 14, "italic"), text_color="gray50")
        self.label_video.pack(fill="both", expand=True, padx=15)

        self.frame_botones_captura = ctk.CTkFrame(self.frame_camara, fg_color="transparent")
        self.frame_botones_captura.pack(side="bottom", fill="x", padx=15, pady=25)

        self.btn_capturar_buena = ctk.CTkButton(self.frame_botones_captura, text="📸 CAPTURAR BUENA", 
                                                 font=("Roboto", 14, "bold"), width=180, height=45,
                                                 fg_color="#1E7B40", hover_color="#145A2D",
                                                 command=self.btn_capturar_buena_click)
        self.btn_capturar_buena.pack(side="left", expand=True)

        self.btn_capturar_mala = ctk.CTkButton(self.frame_botones_captura, text="📸 CAPTURAR MALA", 
                                                font=("Roboto", 14, "bold"), width=180, height=45,
                                                fg_color="#A94442", hover_color="#7B2F2D",
                                                command=self.btn_capturar_mala_click)
        self.btn_capturar_mala.pack(side="right", expand=True)

        # ------------------------------------------
        # 📝 ÁREA DERECHA: CONFIGURACIÓN Y ESTADO
        # ------------------------------------------
        self.frame_config = ctk.CTkFrame(self.main_frame, fg_color="transparent", width=300)
        self.frame_config.pack(side="right", fill="both")

        # 🖊️ NUEVA SECCIÓN: ESCRIBIR TIPO DE BOTELLA
        self.lbl_input_tit = ctk.CTkLabel(self.frame_config, text="🏷️ Registrar Nuevo Tipo", 
                                          font=("Roboto", 16, "bold"), text_color=self.COLOR_HEADER)
        self.lbl_input_tit.pack(pady=(0, 10), anchor="w")

        self.entry_tipo_botella = ctk.CTkEntry(self.frame_config, 
                                               placeholder_text="Escriba nombre de botella...",
                                               width=280, height=45, corner_radius=10,
                                               fg_color=self.COLOR_BLANCO, text_color=self.COLOR_TEXTO,
                                               border_color="#D1CCC0", border_width=1)
        self.entry_tipo_botella.pack(pady=(0, 10))
        
        # Botón para confirmar el nombre escrito
        self.btn_confirmar_nombre = ctk.CTkButton(self.frame_config, text="Actualizar Formato", 
                                                  width=280, height=35, corner_radius=8,
                                                  fg_color=self.COLOR_HEADER, text_color=self.COLOR_BLANCO,
                                                  command=self.actualizar_nombre_formato)
        self.btn_confirmar_nombre.pack(pady=(0, 25))

        # --- ESTADO DEL DATASET ---
        self.label_estado_titulo = ctk.CTkLabel(self.frame_config, text="📊 Resumen de Capturas", 
                                                 font=("Roboto", 16, "bold"), text_color=self.COLOR_HEADER)
        self.label_estado_titulo.pack(pady=(5, 5), anchor="w")

        # Muestra qué botella se está capturando actualmente
        self.label_formato_status = ctk.CTkLabel(self.frame_config, text=f"Editando: {self.formato_actual}", 
                                                 font=("Roboto", 14, "bold"), text_color=self.COLOR_ACENTO)
        self.label_formato_status.pack(pady=(0, 15), anchor="w")

        # CONTADORES
        # Buenas
        self.frame_count_buenas = ctk.CTkFrame(self.frame_config, fg_color=self.COLOR_BLANCO, corner_radius=12, border_width=1, border_color="#D1CCC0")
        self.frame_count_buenas.pack(pady=10, fill="x")
        ctk.CTkLabel(self.frame_count_buenas, text="BUENAS REGISTRADAS", font=("Roboto", 11), text_color="gray40").pack(pady=(5, 0))
        self.label_conteo_buenas = ctk.CTkLabel(self.frame_count_buenas, text="0", font=("Arial", 35, "bold"), text_color="#1E7B40")
        self.label_conteo_buenas.pack(pady=(0, 5))

        # Malas
        self.frame_count_malas = ctk.CTkFrame(self.frame_config, fg_color=self.COLOR_BLANCO, corner_radius=12, border_width=1, border_color="#D1CCC0")
        self.frame_count_malas.pack(pady=10, fill="x")
        ctk.CTkLabel(self.frame_count_malas, text="MALAS REGISTRADAS", font=("Roboto", 11), text_color="gray40").pack(pady=(5, 0))
        self.label_conteo_malas = ctk.CTkLabel(self.frame_count_malas, text="0", font=("Arial", 35, "bold"), text_color="#A94442")
        self.label_conteo_malas.pack(pady=(0, 5))

        self.label_mensaje_info = ctk.CTkLabel(self.frame_config, text="", font=("Roboto", 12))
        self.label_mensaje_info.pack(pady=10)

    # ==========================================
    # ⚙️ LÓGICA DE LA INTERFAZ
    # ==========================================
    def actualizar_nombre_formato(self):
        nuevo_nombre = self.entry_tipo_botella.get().strip()
        if nuevo_nombre:
            self.formato_actual = nuevo_nombre
            self.label_formato_status.configure(text=f"Editando: {self.formato_actual}")
            # Resetear contadores para el nuevo tipo (opcional, para el demo)
            self.conteo_buenas_demo = 0
            self.conteo_malas_demo = 0
            self.label_conteo_buenas.configure(text="0")
            self.label_conteo_malas.configure(text="0")
            self.label_mensaje_info.configure(text="✅ Nuevo formato listo", text_color="#1E7B40")
        else:
            self.label_mensaje_info.configure(text="⚠️ Escriba un nombre válido", text_color="#A94442")

    def btn_capturar_buena_click(self):
        self.conteo_buenas_demo += 1
        self.label_conteo_buenas.configure(text=str(self.conteo_buenas_demo))
        self.mostrar_confirmacion("BUENA")

    def btn_capturar_mala_click(self):
        self.conteo_malas_demo += 1
        self.label_conteo_malas.configure(text=str(self.conteo_malas_demo))
        self.mostrar_confirmacion("MALA")

    def mostrar_confirmacion(self, tipo):
        self.label_mensaje_info.configure(text=f"✨ Capturada {tipo} de {self.formato_actual}", text_color=self.COLOR_HEADER)
        self.after(1500, lambda: self.label_mensaje_info.configure(text=""))

    def btn_volver_click(self):
        self.destroy() 
        self.on_volver()