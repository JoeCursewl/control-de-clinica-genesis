import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from controlador.controlador import Controlador


class Consultar_usuarios(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.db = Controlador()
        
        
    def consult_window_usuarios(self):
        self.app_consult = ctk.CTkToplevel(self)
        w, h = self.app_consult.winfo_screenwidth(), self.app_consult.winfo_screenheight()
        x, y = (w / 2) - 475, (h / 2) - 370
        self.app_consult.geometry(f"950x650+{int(x)}+{int(y)}")
        self.app_consult.grab_set()
        self.app_consult.title("Administración | Consultar Usuarios")
        
        self.letra_label_divisor = ('Century Gothic', 16)
        self.letra_label = ('Century Gothic', 15)
        
        #############################
        
        frame_top = ctk.CTkFrame(self.app_consult, width=900, height=50)
        frame_top.place(x=475, y=10, anchor="n")
        
        label_divisor = ctk.CTkLabel(frame_top, text="Administración | Consultar Usuarios registrados                                                                                                                                 ", font=self.letra_label_divisor)
        label_divisor.pack(padx=20, pady=10)
        
        ###############################
        
        label_buscar_historiales = ctk.CTkLabel(self.app_consult, text="Consultas | Consultar todos los Usuarios", font=self.letra_label)
        label_buscar_historiales.place(x=218, y=115, anchor="w")
        
        button_ingreso_consulta_medicos = ctk.CTkButton(self.app_consult, text="Consultar médicos", command=self.consultar_medico_td, width=12)
        button_ingreso_consulta_medicos.place(x=320, y=180, anchor="center")
        
        button_ingreso_consulta_admins = ctk.CTkButton(self.app_consult, text="Consultar Admins", command=self.consultar_admin_td, width=12)
        button_ingreso_consulta_admins.place(x=485, y=180, anchor="center")
        
        button_ingreso_consulta_asistentes = ctk.CTkButton(self.app_consult, text="Consultar Asistentes", command=self.consultar_asistente_td, width=12)
        button_ingreso_consulta_asistentes.place(x=650, y=180, anchor="center")
        
        self.textbox_consulta_historiales = ctk.CTkTextbox(self.app_consult, width=550, height=330, font=('Century Gothic', 14))
        self.textbox_consulta_historiales.place(x=485, y=400, anchor="center")
        
    def consultar_admin_td(self):
        self.textbox_consulta_historiales.delete("1.0", ctk.END)
        dato = self.db.consulta_admin_all()
        if dato is not None:
            for datos in dato:
                texto = f"ID-Usuario: {datos[0]}\nUsuario: {datos[1]}\nContraseña: {datos[2]}\nCorreo: {datos[3]}\n\n"
                self.textbox_consulta_historiales.insert("1.0", texto)
        else:
            CTkMessagebox(title="Consultas | Error de consulta",
                          message="Aún no hay usuarios registrados hasta ahora!",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
            
    def consultar_medico_td(self):
        self.textbox_consulta_historiales.delete("1.0", ctk.END)
        dato = self.db.consulta_medico_all()
        if dato is not None:
            for datos in dato:
                texto = f"ID-Usuario: {datos[0]}\nUsuario: {datos[1]}\nContraseña: {datos[2]}\nCorreo: {datos[3]}\n\n"
                self.textbox_consulta_historiales.insert("1.0", texto)
        else:
            CTkMessagebox(title="Consultas | Error de consulta",
            message="Aún no hay usuarios registrados ahora!",
                icon="cancel",
                option_1="Cerrar",
                fade_in_duration=35)
            
    def consultar_asistente_td(self):
        self.textbox_consulta_historiales.delete("1.0", ctk.END)
        dato = self.db.consultar_asistente_all()
        if dato is not None:
            for datos in dato:
                texto = f"ID-Usuario: {datos[0]}\nUsuario: {datos[1]}\nContraseña: {datos[2]}\nCorreo: {datos[3]}\n\n"
                self.textbox_consulta_historiales.insert("1.0", texto)
        else:
            CTkMessagebox(title="Consultas | Error de consulta",
            message="Aún no hay usuarios registrados ahora!",
                icon="cancel",
                option_1="Cerrar",
                fade_in_duration=35)