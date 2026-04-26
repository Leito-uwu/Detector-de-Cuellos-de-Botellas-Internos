import customtkinter as ctk
import os
from PIL import Image

class PantallaMenuPrincipal(ctk.CTkToplevel):
    def __init__(self, on_abrir_botellas=None, on_abrir_usuarios=None, on_abrir_bd=None, on_abrir_entrenamiento=None):
        super().__init__()
        
        # Guardamos los callbacks
        self.on_abrir_botellas = on_abrir_botellas
        self.on_abrir_usuarios = on_abrir_usuarios
        self.on_abrir_bd = on_abrir_bd 
        self.on_abrir_entrenamiento = on_abrir_entrenamiento
        
        self.title("Menu - Aranjuez")
        self.geometry("750x650") 
        self.resizable(False, False) 
        
        # ==========================================
        # 🎨 PALETA DE COLORES ARANJUEZ (Extraída de tu imagen)
        # ==========================================
        self.COLOR_CAFE = "#2B1D15"     # Marrón Chocolate Profundo (Para el fondo)
        self.COLOR_VINO = "#721B35"     # Rojo Vino Profundo (Para los botones)
        self.COLOR_CREMA = "#F5EFE7"    # Crema Muy Claro (Para los textos)
        self.COLOR_HOVER = "#5A152A"    # Vino un poco más oscuro para el efecto al pasar el mouse
        
        # Fondo general a Café para resaltar los logos dorados/claros
        self.configure(fg_color=self.COLOR_CAFE)

        # ==========================================
        # 🍷 LOGO PRINCIPAL (ARRIBA AL MEDIO)
        # ==========================================
        ruta_actual = os.path.dirname(__file__)
        ruta_logo_principal = os.path.join(ruta_actual, "..", "Assets", "Aranjuez_logo_1.png")
            
        try:
            pil_image_main = Image.open(ruta_logo_principal)
            self.ctk_logo_main = ctk.CTkImage(light_image=pil_image_main, dark_image=pil_image_main, size=(200, 160))
            self.label_logo_main = ctk.CTkLabel(self, text="", image=self.ctk_logo_main)
        except:
            self.label_logo_main = ctk.CTkLabel(self, text="[ LOGO ARANJUEZ ]", font=("Arial", 30, "bold"), text_color=self.COLOR_CREMA)
        
        self.label_logo_main.pack(pady=(20, 0))

        # ==========================================
        # ⬇️ ÁREA INFERIOR (Empaquetada PRIMERO para que no se corte)
        # ==========================================
        # Le damos un alto fijo de 60px y prohibimos que se encoja
        self.frame_bottom = ctk.CTkFrame(self, fg_color="transparent", height=60)
        self.frame_bottom.pack(side="bottom", fill="x", padx=30, pady=(0, 20))
        self.frame_bottom.pack_propagate(False) 

        # 🟢 LOGO 50 AÑOS (Más pequeño y bien anclado a la izquierda)
        ruta_logo_50 = os.path.join(ruta_actual, "..", "Assets", "logo_50.png")
        try:
            pil_image_50 = Image.open(ruta_logo_50)
            # Reducido a 50x50 para que encaje perfecto
            self.ctk_logo_50 = ctk.CTkImage(light_image=pil_image_50, dark_image=pil_image_50, size=(50, 50))
            self.label_logo_50 = ctk.CTkLabel(self.frame_bottom, text="", image=self.ctk_logo_50)
        except:
            self.label_logo_50 = ctk.CTkLabel(self.frame_bottom, text="[50 Años]", text_color=self.COLOR_CREMA)
        
        self.label_logo_50.pack(side="left", pady=5)

        # 🟢 BOTÓN CERRAR SESIÓN (Alineado a la derecha)
        self.btn_logout = ctk.CTkButton(self.frame_bottom, text="Cerrar Sesión", width=120, height=40,
                                       corner_radius=20, fg_color="transparent", border_width=2, 
                                       border_color=self.COLOR_CREMA, text_color=self.COLOR_CREMA, 
                                       hover_color="#452e22", font=("Roboto", 14, "bold"), 
                                       command=self.cerrar_programa)
        self.btn_logout.pack(side="right", pady=10)

        # ==========================================
        # 📦 CUADRÍCULA DE BOTONES (2x2)
        # ==========================================
        # Empaquetado con expand=True, llenará el espacio restante sin aplastar lo de abajo
        self.frame_grid = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_grid.pack(expand=True)

        # Ajuste leve de altura para que respire mejor la interfaz
        ancho_btn = 210
        alto_btn = 150 
        fuente_btn = ("Roboto", 15, "bold")

        # [FILA 0, COLUMNA 0]
        self.btn_entrenamiento = ctk.CTkButton(self.frame_grid, text="🧠\n\nENTRENAMIENTO\nIA", 
                                               width=ancho_btn, height=alto_btn, corner_radius=20,
                                               font=fuente_btn, fg_color=self.COLOR_VINO, text_color=self.COLOR_CREMA,
                                               hover_color=self.COLOR_HOVER, command=self.btn_entrenamiento_click)
        self.btn_entrenamiento.grid(row=0, column=0, padx=20, pady=15)

        # [FILA 0, COLUMNA 1]
        self.btn_botellas = ctk.CTkButton(self.frame_grid, text="🔍\n\nINSPECCIÓN\nDE LÍNEA", 
                                          width=ancho_btn, height=alto_btn, corner_radius=20,
                                          font=fuente_btn, fg_color=self.COLOR_VINO, text_color=self.COLOR_CREMA,
                                          hover_color=self.COLOR_HOVER, command=self.btn_botellas_click)
        self.btn_botellas.grid(row=0, column=1, padx=20, pady=15)

        # [FILA 1, COLUMNA 0]
        self.btn_bd = ctk.CTkButton(self.frame_grid, text="📊\n\nREPORTES Y\nESTADÍSTICAS", 
                                    width=ancho_btn, height=alto_btn, corner_radius=20,
                                    font=fuente_btn, fg_color=self.COLOR_VINO, text_color=self.COLOR_CREMA,
                                    hover_color=self.COLOR_HOVER, command=self.btn_bd_click)
        self.btn_bd.grid(row=1, column=0, padx=20, pady=15)

        # [FILA 1, COLUMNA 1]
        self.btn_usuarios = ctk.CTkButton(self.frame_grid, text="👥\n\nGESTIÓN DE\nUSUARIOS", 
                                          width=ancho_btn, height=alto_btn, corner_radius=20,
                                          font=fuente_btn, fg_color=self.COLOR_VINO, text_color=self.COLOR_CREMA,
                                          hover_color=self.COLOR_HOVER, command=self.btn_usuarios_click)
        self.btn_usuarios.grid(row=1, column=1, padx=20, pady=15)


    # ==========================================
    # 🔗 FUNCIONES DE CONEXIÓN
    # ==========================================
    def btn_entrenamiento_click(self):
        if self.on_abrir_entrenamiento: self.on_abrir_entrenamiento()

    def btn_botellas_click(self):
        if self.on_abrir_botellas: self.on_abrir_botellas()

    def btn_bd_click(self):
        if self.on_abrir_bd: self.on_abrir_bd()

    def btn_usuarios_click(self):
        if self.on_abrir_usuarios: self.on_abrir_usuarios()

    def cerrar_programa(self):
        self.destroy()