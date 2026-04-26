import customtkinter as ctk
import os
from PIL import Image

class PantallaInspeccion(ctk.CTkToplevel):
    def __init__(self, on_volver, formato_actual, on_cambio_formato):
        super().__init__()
        self.on_volver = on_volver 
        self.on_cambio_formato = on_cambio_formato
        
        self.title("Configuración de Botellas - Milcast Corp")
        self.geometry("750x500")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.cerrar_ventana) 

        # ==========================================
        # 🎨 PALETA DE COLORES ARANJUEZ
        # ==========================================
        self.COLOR_FONDO = "#F5EFE7"    # Crema Muy Claro
        self.COLOR_HEADER = "#721B35"   # Rojo Vino Profundo (Según la referencia)
        self.COLOR_TEXTO_HD = "#F5EFE7" # Letras claras para el header
        self.COLOR_TEXTO = "#212121"    # Texto oscuro general
        self.COLOR_VERDE = "#279A51"    # Verde Esmeralda Vibrante
        self.COLOR_BLANCO = "#FFFFFF"   # Fondo de inputs
        
        self.configure(fg_color=self.COLOR_FONDO)

        # ==========================================
        # 🍷 CABECERA (Rojo Vino Profundo)
        # ==========================================
        self.header_frame = ctk.CTkFrame(self, fg_color=self.COLOR_HEADER, corner_radius=0, height=140)
        self.header_frame.pack(side="top", fill="x")
        self.header_frame.pack_propagate(False)

        # Contenedor central invisible para que el Logo y el Título queden perfectamente al medio
        self.frame_titulos = ctk.CTkFrame(self.header_frame, fg_color="transparent")
        self.frame_titulos.pack(expand=True)

        # --- Logo ---
        ruta_logo = os.path.join(os.path.dirname(__file__), "..", "Assets","Aranjuez_logo_1.png")
             
        try:
            pil_image = Image.open(ruta_logo)
            self.ctk_logo = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(80, 70))
            self.label_logo = ctk.CTkLabel(self.frame_titulos, text="", image=self.ctk_logo)
        except:
            self.label_logo = ctk.CTkLabel(self.frame_titulos, text="[ LOGO ]", text_color=self.COLOR_TEXTO_HD)
        
        self.label_logo.pack(pady=(5, 0))

        # --- Título ---
        self.label_titulo = ctk.CTkLabel(self.frame_titulos, text="CONFIGURACIÓN DE LÍNEA", 
                                         font=("Roboto", 24, "bold"), text_color=self.COLOR_TEXTO_HD)
        self.label_titulo.pack(pady=(5, 5))

        # --- Botón Volver (Flotando a la derecha mediante "place") ---
        self.btn_volver = ctk.CTkButton(self.header_frame, text="Volver al Menú", width=120, height=35,
                                        corner_radius=8, fg_color="#5A152A", text_color=self.COLOR_TEXTO_HD, 
                                        hover_color="#4A1121", font=("Roboto", 14), command=self.cerrar_ventana)
        # relx=0.96 lo ancla casi al borde derecho
        self.btn_volver.place(relx=0.96, rely=0.5, anchor="e")

        # ==========================================
        # 📦 CUERPO (Fondo Crema)
        # ==========================================
        self.label_instruccion = ctk.CTkLabel(self, text="Seleccione el formato a inspeccionar:", 
                                              font=("Roboto", 16), text_color=self.COLOR_TEXTO)
        self.label_instruccion.pack(pady=(40, 10))

        opciones_botellas = ["Botella Tipo A", "Botella Tipo B", "Botella Tipo C", "Botella Tipo D", "Botella Tipo E"]
        
        # 🟢 IMPORTANTE: Sin border_color ni border_width para que no se "rompa" la pantalla
        self.selector_formato = ctk.CTkOptionMenu(self, values=opciones_botellas, command=self.al_cambiar_formato, 
                                                  width=300, height=45, font=("Roboto", 15), corner_radius=8,
                                                  fg_color=self.COLOR_BLANCO, text_color=self.COLOR_TEXTO,
                                                  button_color="#E0E0E0", button_hover_color="#CCCCCC",
                                                  dropdown_fg_color=self.COLOR_BLANCO, dropdown_text_color=self.COLOR_TEXTO)
        self.selector_formato.pack(pady=10)
        
        # Seleccionamos el formato que esté guardado actualmente en memoria
        self.selector_formato.set(formato_actual)

        self.label_estado = ctk.CTkLabel(self, text=f"Formato actual: {formato_actual}", 
                                         font=("Roboto", 16, "bold"), text_color=self.COLOR_TEXTO)
        self.label_estado.pack(pady=20)

        # 🟢 BOTÓN ARRANCAR (Verde Esmeralda Vibrante)
        self.btn_arrancar = ctk.CTkButton(self, text="ARRANCAR INSPECCIÓN", width=300, height=55, 
                                          font=("Roboto", 16, "bold"), corner_radius=12,
                                          fg_color=self.COLOR_VERDE, text_color=self.COLOR_BLANCO, 
                                          hover_color="#1E7B40")
        self.btn_arrancar.pack(pady=30)

    # ==========================================
    # ⚙️ LÓGICA DE CONEXIÓN
    # ==========================================
    def al_cambiar_formato(self, eleccion):
        # Se actualiza el texto visual
        self.label_estado.configure(text=f"Formato actual: {eleccion}")
        # Le avisa al main.py que hubo un cambio para guardarlo en la variable global
        self.on_cambio_formato(eleccion)

    def cerrar_ventana(self):
        self.destroy()
        self.on_volver()

# --- MODO DE PRUEBA INDEPENDIENTE ---
if __name__ == "__main__":
    app = PantallaInspeccion(on_volver=lambda: print("Volviendo..."), 
                             formato_actual="Botella Tipo A", 
                             on_cambio_formato=lambda x: print(f"Cambiado a {x}"))
    app.mainloop()