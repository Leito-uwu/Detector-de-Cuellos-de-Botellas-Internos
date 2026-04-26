import customtkinter as ctk
import os
from PIL import Image

# Importación correcta según tu estructura
from Interfaz_Grafica.gestor_usuarios import cargar_usuarios

class PantallaLogin(ctk.CTk):
    def __init__(self, on_login_success):
        super().__init__()
        self.on_login_success = on_login_success 
        
        self.title("Milcast Corp - Acceso")
        self.geometry("400x650") 
        self.resizable(False, False) 
        
        # ==========================================
        # 🎨 PALETA DE COLORES ARANJUEZ
        # ==========================================
        COLOR_VINO = "#6B1428"     # Fondo cabecera
        COLOR_CREMA = "#F5F2E6"    # Fondo cuerpo
        COLOR_BOTON = "#2D1D16"    # Botón oscuro
        COLOR_TEXTO = "#333333"       
        COLOR_BLANCO = "#FFFFFF"

        # Fondo principal de la ventana (Crema)
        self.configure(fg_color=COLOR_CREMA)

        # ==========================================
        # 🍷 CABECERA (TOP FRAME - Color Vino)
        # ==========================================
        self.frame_top = ctk.CTkFrame(self, fg_color=COLOR_VINO, corner_radius=0, height=260)
        self.frame_top.pack(side="top", fill="x")
        self.frame_top.pack_propagate(False) # Mantener el alto fijo de la cabecera
        
        # --- CARGAR LOGO ---
        # Busca el logo en la carpeta Assets un nivel arriba
        ruta_actual = os.path.dirname(__file__)
        ruta_logo = os.path.join(ruta_actual, "..", "Assets", "Aranjuez_logo_1.png")
        
        try:
            pil_image = Image.open(ruta_logo)
            # AUMENTAMOS EL TAMAÑO DEL LOGO A 180x180
            self.ctk_logo = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(180, 180))
            self.label_logo = ctk.CTkLabel(self.frame_top, text="", image=self.ctk_logo)
        except:
            # Si no encuentra el logo, muestra un emoji como salvavidas
            self.label_logo = ctk.CTkLabel(self.frame_top, text="🍷", font=("Arial", 60), text_color=COLOR_BLANCO)
        
        # Centramos el logo grande en la cabecera
        self.label_logo.pack(expand=True)
        
        # (Se eliminaron los textos duplicados de la marca)

        # ==========================================
        # 📦 CUERPO (Fondo Crema)
        # ==========================================
        self.label_login = ctk.CTkLabel(self, text="Login", font=("Roboto", 24, "bold"), text_color=COLOR_VINO)
        self.label_login.pack(pady=(30, 20))

        # Contenedor transparente para agrupar y alinear los inputs
        self.frame_form = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_form.pack(padx=40, fill="x")

        # Campo 1: Usuario
        self.label_user = ctk.CTkLabel(self.frame_form, text="Usuario/ID", font=("Roboto", 14), text_color=COLOR_TEXTO)
        self.label_user.pack(anchor="w", pady=(0, 5))
        
        self.entry_usuario = ctk.CTkEntry(self.frame_form, 
                                          width=320, height=45, 
                                          corner_radius=15, 
                                          fg_color=COLOR_BLANCO, 
                                          text_color=COLOR_TEXTO,
                                          border_color="#D1CCC0", # Gris suave
                                          border_width=1)
        self.entry_usuario.pack(pady=(0, 15))

        # Campo 2: Contraseña
        self.label_pass = ctk.CTkLabel(self.frame_form, text="Contraseña", font=("Roboto", 14), text_color=COLOR_TEXTO)
        self.label_pass.pack(anchor="w", pady=(0, 5))

        self.entry_password = ctk.CTkEntry(self.frame_form, 
                                           show="*", 
                                           width=320, height=45, 
                                           corner_radius=15, 
                                           fg_color=COLOR_BLANCO, 
                                           text_color=COLOR_TEXTO,
                                           border_color="#D1CCC0",
                                           border_width=1)
        self.entry_password.pack(pady=(0, 5))

        # Mensaje de error
        self.label_mensaje = ctk.CTkLabel(self.frame_form, text="", font=("Roboto", 12))
        self.label_mensaje.pack()

        # ==========================================
        # 🔘 BOTÓN
        # ==========================================
        self.btn_ingresar = ctk.CTkButton(self, 
                                          text="Ingresar", 
                                          width=280, height=50,
                                          corner_radius=25, 
                                          fg_color=COLOR_BOTON, 
                                          hover_color="#1A110D", # Aún más oscuro al pasar el mouse
                                          text_color=COLOR_CREMA,
                                          font=("Roboto", 16, "bold"), 
                                          command=self.validar_acceso)
        self.btn_ingresar.pack(pady=(15, 10))

        # (Se eliminó el texto "¿Olvidó su contraseña?")

    def validar_acceso(self):
        usuario = self.entry_usuario.get().strip()
        password = self.entry_password.get().strip()
        
        try:
            usuarios_db = cargar_usuarios()
            if usuario in usuarios_db and usuarios_db[usuario] == password:
                self.label_mensaje.configure(text="")
                self.withdraw() 
                self.on_login_success()
            else:
                self.label_mensaje.configure(text="❌ Credenciales incorrectas", text_color="#D32F2F")
        except Exception as e:
            self.label_mensaje.configure(text=f"Error BD: {e}", text_color="#D32F2F")