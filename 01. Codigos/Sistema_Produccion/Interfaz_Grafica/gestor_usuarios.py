import customtkinter as ctk
import os
from PIL import Image

try:
    from Base_Datos.gestor_usuarios import cargar_usuarios, guardar_usuarios
except ImportError:
    print("⚠️ Advertencia: No se encontró Base_Datos.gestor_usuarios.")
    def cargar_usuarios(): return {"admin": "1234"}
    def guardar_usuarios(db): pass

class PantallaUsuarios(ctk.CTkToplevel):
    def __init__(self, on_volver):
        super().__init__()
        self.on_volver = on_volver
        
        self.title("Gestión de Usuarios - Milcast Corp")
        self.geometry("750x450") 
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)

        # ==========================================
        # 🎨 PALETA DE COLORES ARANJUEZ
        # ==========================================
        self.COLOR_FONDO = "#F5EFE7"    
        self.COLOR_HEADER = "#2B1D15"   
        self.COLOR_TEXTO_HD = "#F5EFE7" 
        self.COLOR_TEXTO = "#212121"    
        self.COLOR_VERDE = "#279A51"    
        self.COLOR_ROJO = "#D03A2E"     
        self.COLOR_BLANCO = "#FFFFFF"   
        self.COLOR_BORDE = "#333333"    

        self.configure(fg_color=self.COLOR_FONDO)

        # ==========================================
        # 🍫 CABECERA (Marrón Chocolate)
        # ==========================================
        self.header_frame = ctk.CTkFrame(self, fg_color=self.COLOR_HEADER, corner_radius=0, height=100)
        self.header_frame.pack(side="top", fill="x")
        self.header_frame.pack_propagate(False)

        ruta_logo = os.path.join(os.path.dirname(__file__), "..", "Assets","Aranjuez_logo_1.png")
        try:
            pil_image = Image.open(ruta_logo)
            self.ctk_logo = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(80, 70))
            self.label_logo = ctk.CTkLabel(self.header_frame, text="", image=self.ctk_logo)
        except:
            self.label_logo = ctk.CTkLabel(self.header_frame, text="[ LOGO ]", text_color=self.COLOR_TEXTO_HD)
        self.label_logo.pack(side="left", padx=(30, 20), pady=15)

        self.label_titulo = ctk.CTkLabel(self.header_frame, text="GESTIÓN DE USUARIOS", 
                                         font=("Roboto", 28, "bold"), text_color=self.COLOR_TEXTO_HD)
        self.label_titulo.pack(side="left")

        self.btn_volver = ctk.CTkButton(self.header_frame, text="Volver al Menú", width=120, height=35,
                                        corner_radius=8, fg_color=self.COLOR_FONDO, text_color=self.COLOR_HEADER, 
                                        hover_color="#D1CCC0", font=("Roboto", 14, "bold"), command=self.cerrar_ventana)
        self.btn_volver.pack(side="right", padx=30)

        # ==========================================
        # 📦 CUERPO DIVIDIDO
        # ==========================================
        self.frame_izq = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_izq.pack(side="left", fill="both", expand=True, padx=(30, 15), pady=20)
        
        self.frame_der = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_der.pack(side="right", fill="both", expand=True, padx=(15, 30), pady=20)

        # ------------------------------------------
        # ➕ COLUMNA IZQUIERDA: CREAR USUARIO
        # ------------------------------------------
        self.lbl_crear = ctk.CTkLabel(self.frame_izq, text="➕ Crear Nuevo Operador", 
                                      font=("Roboto", 18, "bold"), text_color=self.COLOR_VERDE)
        self.lbl_crear.pack(pady=(10, 20))
        
        self.entry_nuevo_id = ctk.CTkEntry(self.frame_izq, placeholder_text="Nuevo ID de Operador", 
                                           width=250, height=40, corner_radius=8,
                                           fg_color=self.COLOR_BLANCO, text_color=self.COLOR_TEXTO,
                                           border_color=self.COLOR_BORDE, border_width=1)
        self.entry_nuevo_id.pack(pady=10)
        
        self.entry_nueva_pass = ctk.CTkEntry(self.frame_izq, placeholder_text="Contraseña", 
                                             width=250, height=40, corner_radius=8,
                                             fg_color=self.COLOR_BLANCO, text_color=self.COLOR_TEXTO,
                                             border_color=self.COLOR_BORDE, border_width=1)
        self.entry_nueva_pass.pack(pady=10)
        
        self.btn_crear = ctk.CTkButton(self.frame_izq, text="Guardar Usuario", 
                                       width=160, height=40, corner_radius=8, font=("Roboto", 15, "bold"),
                                       fg_color=self.COLOR_VERDE, text_color=self.COLOR_BLANCO, 
                                       hover_color="#1E7B40", command=self.crear_usuario)
        self.btn_crear.pack(pady=20)

        # ------------------------------------------
        # 🗑️ COLUMNA DERECHA: ELIMINAR USUARIO
        # ------------------------------------------
        self.lbl_eliminar = ctk.CTkLabel(self.frame_der, text="🗑️ Eliminar Operador", 
                                         font=("Roboto", 18, "bold"), text_color=self.COLOR_ROJO)
        self.lbl_eliminar.pack(pady=(10, 20))
        
        self.lbl_instruccion = ctk.CTkLabel(self.frame_der, text="Seleccione el ID a eliminar:", 
                                            font=("Roboto", 14), text_color=self.COLOR_TEXTO)
        self.lbl_instruccion.pack(pady=(0, 5))
        
        # 🟢 AQUÍ ESTABA EL ERROR: Se eliminó border_color y border_width
        self.selector_eliminar = ctk.CTkOptionMenu(self.frame_der, values=["Cargando..."], 
                                                   width=250, height=40, corner_radius=8,
                                                   fg_color=self.COLOR_BLANCO, text_color=self.COLOR_TEXTO,
                                                   button_color="#E0E0E0", button_hover_color="#CCCCCC",
                                                   dropdown_fg_color=self.COLOR_BLANCO, dropdown_text_color=self.COLOR_TEXTO)
        self.selector_eliminar.pack(pady=10)
        
        self.btn_eliminar = ctk.CTkButton(self.frame_der, text="Eliminar Usuario", 
                                          width=160, height=40, corner_radius=8, font=("Roboto", 15, "bold"),
                                          fg_color=self.COLOR_ROJO, text_color=self.COLOR_BLANCO, 
                                          hover_color="#A62E25", command=self.eliminar_usuario)
        self.btn_eliminar.pack(pady=20)

        # ------------------------------------------
        # 📢 MENSAJES DE ESTADO
        # ------------------------------------------
        self.lbl_mensaje = ctk.CTkLabel(self, text="", font=("Roboto", 14, "bold"))
        self.lbl_mensaje.pack(side="bottom", pady=15)

        self.actualizar_lista_desplegable()

    # ==========================================
    # ⚙️ LÓGICA DE BASE DE DATOS
    # ==========================================
    def actualizar_lista_desplegable(self):
        usuarios_db = cargar_usuarios()
        lista_ids = list(usuarios_db.keys())
        self.selector_eliminar.configure(values=lista_ids)
        self.selector_eliminar.set(lista_ids[0] if lista_ids else "")

    def crear_usuario(self):
        nuevo_id = self.entry_nuevo_id.get().strip()
        nueva_pass = self.entry_nueva_pass.get().strip()
        if not nuevo_id or not nueva_pass:
            self.lbl_mensaje.configure(text="⚠️ Complete ambos campos", text_color="#D03A2E")
            return
        usuarios_db = cargar_usuarios()
        if nuevo_id in usuarios_db:
            self.lbl_mensaje.configure(text="❌ El usuario ya existe", text_color="#D03A2E")
        else:
            usuarios_db[nuevo_id] = nueva_pass
            guardar_usuarios(usuarios_db)
            self.actualizar_lista_desplegable()
            self.entry_nuevo_id.delete(0, 'end')
            self.entry_nueva_pass.delete(0, 'end')
            self.lbl_mensaje.configure(text=f"✅ Usuario '{nuevo_id}' creado exitosamente", text_color=self.COLOR_VERDE)

    def eliminar_usuario(self):
        id_a_eliminar = self.selector_eliminar.get()
        if id_a_eliminar == "admin":
            self.lbl_mensaje.configure(text="⛔ No puedes eliminar al administrador maestro", text_color="#D03A2E")
            return
        usuarios_db = cargar_usuarios()
        if id_a_eliminar in usuarios_db:
            del usuarios_db[id_a_eliminar]
            guardar_usuarios(usuarios_db)
            self.actualizar_lista_desplegable()
            self.lbl_mensaje.configure(text=f"🗑️ Usuario '{id_a_eliminar}' eliminado", text_color=self.COLOR_HEADER)

    def cerrar_ventana(self):
        self.destroy()
        self.on_volver()