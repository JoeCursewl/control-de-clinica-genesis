import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from controlador.controlador import Controlador
from vistas.main_app import Main_app
from vistas.main_app_medico import Main_app_medico
from vistas.main_app_asistente import Main_app_asistente


class Acceso_cl(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.letra_labels = ('Century Gothic', 16)
        self.letra_entry = ('Century Gothic', 12)
        self.letra_inicio = ('Century Gothic', 18)
        
        #########################################
        
        self.db = Controlador()
        self.main_app = Main_app(master)
        self.main_app_medico = Main_app_medico(master)
        self.main_app_asistente = Main_app_asistente(master)
        
        #########################################
        
        frame_acceso = ctk.CTkFrame(master)
        frame_acceso.place(relx=0.5, rely=0.5, anchor="center")
        
        label_acceso = ctk.CTkLabel(frame_acceso, text="        Clínica | Iniciar Sesión        ", font=self.letra_inicio)
        label_acceso.pack(padx=10, pady=(25,40))
        
        boton_admin = ctk.CTkButton(frame_acceso, text="Iniciar Sesión | Admin", command=self.acesso_login_admin)
        boton_admin.pack(padx=28, pady=10)
        
        boton_medico = ctk.CTkButton(frame_acceso, text="Iniciar Sesión | Médico", command=self.acesso_login_medico)
        boton_medico.pack(padx=28, pady=10)
        
        boton_asistente = ctk.CTkButton(frame_acceso, text="Iniciar Sesión | Asistente", command=self.acesso_login_asistente)
        boton_asistente.pack(padx=28, pady=(10,50))
        

        
    def acesso_login_admin(self):
        self.app_login_redirect = ctk.CTkToplevel(self)
        self.app_login_redirect.geometry("400x600")
        self.app_login_redirect.title("Iniciar Sesión | Admin")
        self.app_login_redirect.grab_set()
        w, h = self.app_login_redirect.winfo_screenwidth(), self.app_login_redirect.winfo_screenheight()
        x, y = (w / 2) - 200, (h / 2) - 325
        self.app_login_redirect.geometry(f"400x600+{int(x)}+{int(y)}")
        self.app_login_redirect.resizable(0,0)
        
        frame_todo = ctk.CTkFrame(self.app_login_redirect)
        frame_todo.place(relx=0.5, rely=0.5, anchor="center")
        
        logo_clinica = ctk.CTkLabel(frame_todo, text="Clínica Génesis C.A", font=('Century Gotchi', 16))
        logo_clinica.pack(padx=25, pady=25)
        
        label_usuario = ctk.CTkLabel(frame_todo, text="Usuario", font=self.letra_labels)
        label_usuario.pack(padx=25, pady=10)
        
        self.entry_usuario = ctk.CTkEntry(frame_todo, font=self.letra_entry, placeholder_text="Ingrese su usuario", width=200)
        self.entry_usuario.pack(padx=25, pady=5)
        
        label_password = ctk.CTkLabel(frame_todo, text="Contraseña", font=self.letra_labels)
        label_password.pack(padx=25, pady=10)
        
        self.entry_password = ctk.CTkEntry(frame_todo, font=self.letra_entry, placeholder_text="Ingrese su contraseña", width=200)
        self.entry_password.pack(padx=25, pady=5)
        
        botton_ingreso = ctk.CTkButton(frame_todo, text="Iniciar Sesión", command=self.validar_login_admin)
        botton_ingreso.pack(padx=25, pady=35)
        
        
    def validar_login_admin(self):
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()
        if usuario and password != '':
            if len(usuario) > 5:
                if len(password) > 5:
                    dato = self.db.validar_login_admin(usuario=usuario, password=password)
                    if dato is not None:
                        CTkMessagebox(title="Clínica | Inicio de Sesión",
                            message="Sesión Iniciada correctamente!",
                            icon="check",
                            option_1="Cerrar",
                            fade_in_duration=35)
                        self.entry_password.delete(0, ctk.END)
                        self.entry_usuario.delete(0, ctk.END)
                        self.app_login_redirect.destroy()
                        self.master.withdraw()
                        self.main_app.app_window()
                    else:                    
                        CTkMessagebox(title="Clínica | Error de Inicio de Sesión",
                          message="Credenciales inválidas! Revise sus credenciales!",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
                else:
                    CTkMessagebox(title="Clínica | Error de Inicio de Sesión",
                          message="Ingrese una contraseña válida!",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
            else:
                CTkMessagebox(title="Clínica | Error de Inicio de Sesión",
                    message="Ingrese un usuario válido!",
                    icon="cancel",
                    option_1="Cerrar",
                    fade_in_duration=35)
                
        else:
            CTkMessagebox(title="Clínica | Error de Inicio de Sesión",
                          message="Todos los campos son necesarios!",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
            
        
    def acesso_login_medico(self):
        self.app_login_redirect = ctk.CTkToplevel(self)
        self.app_login_redirect.geometry("400x600")
        self.app_login_redirect.title("Iniciar Sesión | Médico")
        self.app_login_redirect.grab_set()
        w, h = self.app_login_redirect.winfo_screenwidth(), self.app_login_redirect.winfo_screenheight()
        x, y = (w / 2) - 200, (h / 2) - 325
        self.app_login_redirect.geometry(f"400x600+{int(x)}+{int(y)}")
        
        frame_todo = ctk.CTkFrame(self.app_login_redirect)
        frame_todo.place(relx=0.5, rely=0.5, anchor="center")
        
        logo_clinica = ctk.CTkLabel(frame_todo, text="Clínica Génesis C.A", font=('Century Gotchi', 16))
        logo_clinica.pack(padx=25, pady=30)
        
        label_usuario = ctk.CTkLabel(frame_todo, text="Usuario", font=self.letra_labels)
        label_usuario.pack(padx=25, pady=10)
        
        self.entry_usuario_medico = ctk.CTkEntry(frame_todo, font=self.letra_entry, placeholder_text="Ingrese su usuario", width=200)
        self.entry_usuario_medico.pack(padx=25, pady=5)
        
        label_password = ctk.CTkLabel(frame_todo, text="Contraseña", font=self.letra_labels)
        label_password.pack(padx=25, pady=10)
        
        self.entry_password_medico = ctk.CTkEntry(frame_todo, font=self.letra_entry, placeholder_text="Ingrese su contraseña", width=200)
        self.entry_password_medico.pack(padx=25, pady=5)
        
        botton_ingreso = ctk.CTkButton(frame_todo, text="Iniciar Sesión", command=self.validar_login_medico)
        botton_ingreso.pack(padx=25, pady=35)
        
    def validar_login_medico(self):
        usuario_medico = self.entry_usuario_medico.get()
        password_medico = self.entry_password_medico.get()
        if usuario_medico and password_medico != '':
            dato = self.db.validar_login_medico(usuario=usuario_medico, password=password_medico)
            if dato is not None:
                CTkMessagebox(title="Clínica | Inicio de Sesión",
                    message="Sesión Iniciada correctamente!",
                    icon="check",
                    option_1="Cerrar",
                    fade_in_duration=35)
                self.entry_password_medico.delete(0, ctk.END)
                self.entry_usuario_medico.delete(0, ctk.END)
                
                self.master.withdraw()
                self.app_login_redirect.destroy()
                self.main_app_medico.app_window_medico()
            else:
                CTkMessagebox(title="Clínica | Error",
                    message="Credenciales inválidas! revise sus credenciales!",
                    icon="cancel",
                    option_1="Cerrar",
                    fade_in_duration=35)
                
        else:
            CTkMessagebox(title="Clínica | Error de Inicio de Sesión",
                          message="Todos los campos son necesarios!",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
            
            
    def acesso_login_asistente(self):
        self.app_login_redirect = ctk.CTkToplevel(self)
        self.app_login_redirect.geometry("400x600")
        self.app_login_redirect.title("Iniciar Sesión | Asistente")
        self.app_login_redirect.grab_set()
        w, h = self.app_login_redirect.winfo_screenwidth(), self.app_login_redirect.winfo_screenheight()
        x, y = (w / 2) - 200, (h / 2) - 325
        self.app_login_redirect.geometry(f"400x600+{int(x)}+{int(y)}")
        
        frame_todo = ctk.CTkFrame(self.app_login_redirect)
        frame_todo.place(relx=0.5, rely=0.5, anchor="center")
        
        logo_clinica = ctk.CTkLabel(frame_todo, text="Clínica Génesis C.A", font=('Century Gotchi', 16))
        logo_clinica.pack(padx=25, pady=30)
        
        label_usuario = ctk.CTkLabel(frame_todo, text="Usuario", font=self.letra_labels)
        label_usuario.pack(padx=25, pady=10)
        
        self.entry_usuario_asistente = ctk.CTkEntry(frame_todo, font=self.letra_entry, placeholder_text="Ingrese su usuario", width=200)
        self.entry_usuario_asistente.pack(padx=25, pady=5)
        
        label_password = ctk.CTkLabel(frame_todo, text="Contraseña", font=self.letra_labels)
        label_password.pack(padx=25, pady=10)
        
        self.entry_password_asistente = ctk.CTkEntry(frame_todo, font=self.letra_entry, placeholder_text="Ingrese su contraseña", width=200)
        self.entry_password_asistente.pack(padx=25, pady=5)
        
        botton_ingreso = ctk.CTkButton(frame_todo, text="Iniciar Sesión", command=self.validar_login_asistente)
        botton_ingreso.pack(padx=25, pady=35)
        
    def validar_login_asistente(self):
        usuario_asistente = self.entry_usuario_asistente.get()
        password_asistente = self.entry_password_asistente.get()
        if usuario_asistente and password_asistente != '':
            dato = self.db.validar_login_asistente(usuario=usuario_asistente, password=password_asistente)
            if dato is not None:
                CTkMessagebox(title="Clínica | Inicio de Sesión",
                    message="Sesión Iniciada correctamente!",
                    icon="check",
                    option_1="Cerrar",
                    fade_in_duration=35)
                self.entry_usuario_asistente.delete(0, ctk.END)
                self.entry_password_asistente.delete(0, ctk.END)
                
                self.master.withdraw()
                self.app_login_redirect.destroy()
                self.main_app_asistente.app_window_asistentes()
            else:
                CTkMessagebox(title="Clínica | Error",
                    message="Credenciales inválidas! revise sus credenciales!",
                    icon="cancel",
                    option_1="Cerrar",
                    fade_in_duration=35)
                
        else:
            CTkMessagebox(title="Clínica | Error de Inicio de Sesión",
                          message="Todos los campos son necesarios!",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)