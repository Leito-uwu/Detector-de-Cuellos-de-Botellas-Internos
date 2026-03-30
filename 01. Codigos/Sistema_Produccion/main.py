import customtkinter as ctk
from Interfaz_Grafica.login import PantallaLogin
# Aquí importaremos las otras pantallas cuando las separemos
# from Interfaz_Grafica.dashboard import PantallaMenuPrincipal 

class AplicacionPrincipal:
    def __init__(self):
        self.mostrar_login()

    def mostrar_login(self):
        self.login_vnt = PantallaLogin(on_login_success=self.abrir_menu_principal)
        self.login_vnt.mainloop()

    def abrir_menu_principal(self):
        print("🚀 Login exitoso. Iniciando Dashboard...")
        # Aquí instanciaremos la PantallaMenuPrincipal más adelante
        # self.menu_vnt = PantallaMenuPrincipal()
        # self.menu_vnt.mainloop()

if __name__ == "__main__":
    app = AplicacionPrincipal()