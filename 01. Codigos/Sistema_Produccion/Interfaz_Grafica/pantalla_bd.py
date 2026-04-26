import customtkinter as ctk
import os
from PIL import Image
from tkinter import ttk 
import random

# Importación de la base de datos
try:
    from Base_Datos.gestor_produccion import obtener_registros, registrar_botella
except ImportError:
    print("⚠️ Advertencia: No se encontró gestor_produccion. Modo simulador local activado.")
    def obtener_registros(): return [("26/03-2023", "Botella Tipo B", 36, 6), ("28/03-2023", "Botella Tipo D", 60, 3)]
    def registrar_botella(f, e): pass

class PantallaBaseDatos(ctk.CTkToplevel):
    def __init__(self, on_volver, formato_actual):
        super().__init__()
        self.on_volver = on_volver
        self.formato_actual = formato_actual 
        
        self.title("Reporte de Producción - Milcast Corp")
        self.geometry("800x550") # Un poco más ancho para que la tabla respire
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)

        # ==========================================
        # 🎨 PALETA DE COLORES ARANJUEZ
        # ==========================================
        self.COLOR_FONDO = "#F5EFE7"    # Crema Muy Claro
        self.COLOR_HEADER = "#279A51"   # Verde Esmeralda Vibrante (Según referencia)
        self.COLOR_TEXTO_HD = "#FFFFFF" # Letras blancas para la cabecera
        self.COLOR_TEXTO = "#212121"    # Texto oscuro para la tabla
        self.COLOR_CAFE = "#2B1D15"     # Marrón Chocolate para botones
        
        self.configure(fg_color=self.COLOR_FONDO)

        # ==========================================
        # 🌿 CABECERA (Verde Esmeralda)
        # ==========================================
        self.header_frame = ctk.CTkFrame(self, fg_color=self.COLOR_HEADER, corner_radius=0, height=140)
        self.header_frame.pack(side="top", fill="x")
        self.header_frame.pack_propagate(False)

        # Contenedor central invisible para centrar Logo y Título
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

        # --- Título (Solo "BASE DE DATOS") ---
        self.label_titulo = ctk.CTkLabel(self.frame_titulos, text="BASE DE DATOS", 
                                         font=("Roboto", 26, "bold"), text_color=self.COLOR_TEXTO_HD)
        self.label_titulo.pack(pady=(5, 5))

        # --- Botón Volver (Flotando a la derecha) ---
        self.btn_volver = ctk.CTkButton(self.header_frame, text="Volver al Menú", width=120, height=35,
                                        corner_radius=8, fg_color=self.COLOR_CAFE, text_color=self.COLOR_TEXTO_HD, 
                                        hover_color="#452e22", font=("Roboto", 14), command=self.cerrar_ventana)
        self.btn_volver.place(relx=0.96, rely=0.5, anchor="e")

        # ==========================================
        # 📊 TABLA DE DATOS (Integrada al fondo crema)
        # ==========================================
        estilo = ttk.Style()
        estilo.theme_use("default")
        
        # Configuramos la tabla para que parezca "flotar" sobre el fondo crema
        estilo.configure("Treeview", 
                         background=self.COLOR_FONDO, 
                         foreground=self.COLOR_TEXTO, 
                         rowheight=35, 
                         fieldbackground=self.COLOR_FONDO,
                         font=("Roboto", 13),
                         borderwidth=0)
        
        # Color al seleccionar una fila
        estilo.map('Treeview', background=[('selected', '#D1CCC0')], foreground=[('selected', self.COLOR_TEXTO)])
        
        # Configuración de los encabezados (Textos en negrita)
        estilo.configure("Treeview.Heading", 
                         background=self.COLOR_FONDO, 
                         foreground=self.COLOR_TEXTO, 
                         font=('Roboto', 14, 'bold'),
                         borderwidth=0)

        self.frame_tabla = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_tabla.pack(fill="both", expand=True, padx=30, pady=20)

        columnas = ("Fecha", "Formato", "Buenas", "Malas")
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show="headings", height=8)
        
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, anchor="center", width=150)
            
        self.tabla.pack(fill="both", expand=True, pady=10)

        # ==========================================
        # ⚙️ PANEL DE SIMULACIÓN Y CONTROL
        # ==========================================
        self.frame_controles = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_controles.pack(fill="x", padx=30, pady=(0, 20))

        # Botón Actualizar (Azul estándar, como en la imagen)
        self.btn_actualizar = ctk.CTkButton(self.frame_controles, text="🔄 Actualizar Tabla", 
                                            width=160, height=40, corner_radius=8, font=("Roboto", 14, "bold"),
                                            fg_color="#1F618D", hover_color="#154360", command=self.cargar_datos)
        self.btn_actualizar.pack(side="left")

        # Botón Simular (Café Oscuro)
        texto_boton = f"⚙️ Simular 10 ({self.formato_actual})"
        self.btn_simular = ctk.CTkButton(self.frame_controles, text=texto_boton, 
                                         width=180, height=40, corner_radius=8, font=("Roboto", 14, "bold"),
                                         fg_color=self.COLOR_CAFE, hover_color="#452e22", command=self.simular_ingreso)
        self.btn_simular.pack(side="right")

        self.cargar_datos()

    # ==========================================
    # 🔗 FUNCIONES INTERNAS
    # ==========================================
    def cargar_datos(self):
        # Limpiamos la tabla primero
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        
        try:
            registros = obtener_registros()
            for registro in registros:
                self.tabla.insert("", "end", values=registro)
        except Exception as e:
            print("Error al cargar la BD:", e)

    def simular_ingreso(self):
        estados = ["BUENA", "BUENA", "BUENA", "BUENA", "MALA"] 
        
        try:
            for _ in range(10):
                estado_elegido = random.choice(estados)
                registrar_botella(self.formato_actual, estado_elegido)
                
            print(f"Simuladas 10 unidades de {self.formato_actual}")
            self.cargar_datos() 
        except Exception as e:
            print("Error al simular:", e)

    def cerrar_ventana(self):
        self.destroy()
        self.on_volver()

# --- MODO DE PRUEBA INDEPENDIENTE ---
if __name__ == "__main__":
    app = PantallaBaseDatos(on_volver=lambda: print("Volviendo..."), formato_actual="Botella Tipo A")
    app.mainloop()