import customtkinter as ctk
import os
# Importamos Pillow para manejo avanzado de imágenes
from PIL import Image 

# ==========================================
# CONFIGURACIÓN GENERAL DE LA INTERFAZ
# ==========================================
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue") 

# ==========================================
# 2. VENTANA PRINCIPAL (PANEL DE OPERACIÓN)
# ==========================================
class PantallaPrincipal(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.title("Panel de Control - Milcast Corp")
        self.geometry("650x500") # Agrandamos un poco la ventana para el diseño
        self.resizable(False, False)
        
        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.cerrar_sistema)

        # ====================================================
        # 🟢 SECCIÓN 1: CABECERA (HEADER) - LOGO Y TÍTULO
        # ====================================================
        # 1. Creamos un frame horizontal en la parte superior
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent") # Transparente para no romper la estética
        self.header_frame.pack(side="top", fill="x", padx=20, pady=10)

        # 2. CARGAR LA IMAGEN (LOGO)
        # Intentamos cargar la imagen real. Si no existe, usamos un placeholder.
        ruta_script = os.path.dirname(r'C:\Users\leona\Documents\PPP_Aranjuez\01. Codigos\Aranjuez_logo.png') # Ruta de la carpeta actual
        ruta_logo = os.path.join(ruta_script, "Aranjuez_logo") # Nombre de tu imagen real

        try:
            # Cargamos imagen con PIL y definimos tamaño visual
            pil_image = Image.open(ruta_logo)
            self.ctk_logo = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(60, 60))
            
            # Label para mostrar la imagen real
            self.label_imagen = ctk.CTkLabel(self.header_frame, text="", image=self.ctk_logo)
        except Exception as e:
            # Placeholder visual si no encuentra el archivo 'logo.png'
            print(f"⚠️ Nota: No se encontró 'logo.png', usando placeholder. Error: {e}")
            self.label_imagen = ctk.CTkLabel(self.header_frame, text="[ LOGO ]", 
                                              width=60, height=60, 
                                              fg_color="gray30", corner_radius=10)

        # Posicionamos la imagen a la IZQUIERDA SUPERIOR dentro del frame
        self.label_imagen.pack(side="left", anchor="nw") # NW = North West (Nor-Oeste)

        # 3. MOVER EL TÍTULO DENTRO DE LA CABECERA
        # Ahora el título está dentro de header_frame, a la derecha de la imagen
        self.label_titulo = ctk.CTkLabel(self.header_frame, text="CONFIGURACIÓN DE LÍNEA", 
                                          font=("Roboto", 22, "bold"))
        self.label_titulo.pack(side="left", padx=(20, 0), expand=True, fill="x") # expand y fill lo centran en el espacio restante


        # ====================================================
        # 🟡 SECCIÓN 2: CUERPO DEL PANEL (SEPARADOR Y CONTROLES)
        # ====================================================
        # Una línea separadora visual
        self.separador = ctk.CTkFrame(self, height=2, fg_color="gray30")
        self.separador.pack(fill="x", padx=20, pady=(0, 20))

        self.label_instruccion = ctk.CTkLabel(self, text="Seleccione el formato de botella a inspeccionar:", 
                                               font=("Roboto", 14), text_color="gray")
        self.label_instruccion.pack(pady=(10, 20))

        # --- EL SELECTOR DESPLEGABLE (Igual que antes) ---
        opciones_botellas = ["Botella Tipo A", "Botella Tipo B", "Botella Tipo C", "Botella Tipo D", "Botella Tipo E"]
        
        self.selector_formato = ctk.CTkOptionMenu(
            self, 
            values=opciones_botellas, 
            command=self.al_cambiar_formato,
            width=250, 
            height=40,
            font=("Roboto", 14)
        )
        self.selector_formato.pack(pady=10)

        self.label_estado = ctk.CTkLabel(self, text="Formato actual: Botella Tipo A", 
                                          font=("Roboto", 16), text_color="yellow")
        self.label_estado.pack(pady=20)

        self.btn_arrancar = ctk.CTkButton(
            self, text="ARRANCAR INSPECCIÓN", 
            width=250, height=50, font=("Roboto", 16, "bold"), 
            fg_color="green", hover_color="darkgreen"
        )
        self.btn_arrancar.pack(pady=30)

    # Lógica de cambio de formato (Igual)
    def al_cambiar_formato(self, eleccion):
        self.label_estado.configure(text=f"Formato actual: {eleccion}")
        print(f"⚙️ Formato cambiado a: {eleccion}")

    # Lógica de cierre (Igual)
    def cerrar_sistema(self):
        print("Apagando sistema...")
        self.parent.destroy()

# ==========================================
# 1. VENTANA DE LOGIN (PANTALLA DE INICIO)
# ==========================================
# (Esta clase no cambia, se mantiene exactamente igual)
class PantallaLogin(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Milcast Corp - Acceso de Seguridad")
        self.geometry("400x450")
        self.resizable(False, False) 
        self.label_titulo = ctk.CTkLabel(self, text="SISTEMA DE INSPECCIÓN", font=("Roboto", 22, "bold"))
        self.label_titulo.pack(pady=(50, 5))
        self.label_subtitulo = ctk.CTkLabel(self, text="Identificación de Operador", font=("Roboto", 14), text_color="gray")
        self.label_subtitulo.pack(pady=(0, 40))
        self.entry_usuario = ctk.CTkEntry(self, placeholder_text="ID de Operador", width=250, height=40, justify="center")
        self.entry_usuario.pack(pady=10)
        self.entry_password = ctk.CTkEntry(self, placeholder_text="Contraseña", show="*", width=250, height=40, justify="center")
        self.entry_password.pack(pady=10)
        self.label_mensaje = ctk.CTkLabel(self, text="", font=("Roboto", 12))
        self.label_mensaje.pack(pady=5)
        self.btn_ingresar = ctk.CTkButton(self, text="INICIAR SESIÓN", width=250, height=40, font=("Roboto", 14, "bold"), command=self.validar_acceso)
        self.btn_ingresar.pack(pady=20)
    def validar_acceso(self):
        if self.entry_usuario.get() == "admin" and self.entry_password.get() == "1234":
            self.withdraw() 
            ventana_principal = PantallaPrincipal(self)
            ventana_principal.focus() 
        else:
            self.label_mensaje.configure(text="❌ ID o Contraseña incorrectos", text_color="red")

# ==========================================
# ARRANQUE DEL PROGRAMA
# ==========================================
if __name__ == "__main__":
    app = PantallaLogin()
    app.mainloop()
