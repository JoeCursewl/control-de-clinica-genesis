import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from controlador.controlador import Controlador

class Registrar_usuarios(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        
        self.db = Controlador()
        
    def register_usuarios_window(self):
        self.app_register_usuarios = ctk.CTkToplevel(self)
        w, h = self.app_register_usuarios.winfo_screenwidth(), self.app_register_usuarios.winfo_screenheight()
        x, y = (w / 2) - 475, (h / 2) - 370
        self.app_register_usuarios.geometry(f"950x660+{int(x)}+{int(y)}")
        self.app_register_usuarios.grab_set()
        self.app_register_usuarios.title("Administración | Registrar Usuarios")
        self.app_register_usuarios.resizable(0,0)
        
        self.letra_label_divisor = ('Century Gothic', 16)
        self.letra_label = ('Century Gothic', 15)
        
        ###########################################
        
        frame_top = ctk.CTkFrame(self.app_register_usuarios, width=900, height=50)
        frame_top.place(x=475, y=10, anchor="n")
        
        label_divisor = ctk.CTkLabel(frame_top, text="Administración | Registro de Usuarios                                                                                                                                        ", font=self.letra_label_divisor)
        label_divisor.pack(padx=20, pady=10)
        
        #####################################################
        
        label_user_admin = ctk.CTkLabel(self.app_register_usuarios, text="Usuario admin", font=self.letra_label)
        label_user_admin.place(x=80, y=150, anchor="w")
        
        self.entry_user_admin = ctk.CTkEntry(self.app_register_usuarios, width=170)
        self.entry_user_admin.place(x=80, y=190, anchor="w")
        
        #####################################################
        
        label_password_admin = ctk.CTkLabel(self.app_register_usuarios, text="Contraseña", font=self.letra_label)
        label_password_admin.place(x=80, y=230, anchor="w")
        
        self.entry_password_admin = ctk.CTkEntry(self.app_register_usuarios, width=170)
        self.entry_password_admin.place(x=80, y=270, anchor="w")
        
        #####################################################
        
        label_repeat_password_admin = ctk.CTkLabel(self.app_register_usuarios, text="Repita su contraseña", font=self.letra_label)
        label_repeat_password_admin.place(x=80, y=310, anchor="w")
        
        self.entry_repeat_password_admin = ctk.CTkEntry(self.app_register_usuarios, width=170)
        self.entry_repeat_password_admin.place(x=80, y=350, anchor="w")
        
        ######################################
        
        label_correo_admin = ctk.CTkLabel(self.app_register_usuarios, text="Correo", font=self.letra_label)
        label_correo_admin.place(x=80, y=390, anchor="w")
        
        self.entry_correo_admin = ctk.CTkEntry(self.app_register_usuarios, width=170)
        self.entry_correo_admin.place(x=80, y=430, anchor="w")
        
        ######################################
        
        frame_divisor = ctk.CTkFrame(self.app_register_usuarios, width=5, height=200)
        frame_divisor.place(x=325, y=270, anchor="w")
        
        ##################################################
        
        label_usuario_medico = ctk.CTkLabel(self.app_register_usuarios, text="Usuario Médico", font=self.letra_label)
        label_usuario_medico.place(x=395, y=150, anchor="w")
        
        self.entry_usuario_medico = ctk.CTkEntry(self.app_register_usuarios, width=170)
        self.entry_usuario_medico.place(x=395, y=190, anchor="w")
        
        #################################################
        
        label_passentry_password_medico = ctk.CTkLabel(self.app_register_usuarios, text="Contraseña", font=self.letra_label)
        label_passentry_password_medico.place(x=395, y=230, anchor="w")
        
        self.entry_password_medico = ctk.CTkEntry(self.app_register_usuarios, width=170)
        self.entry_password_medico.place(x=395, y=270, anchor="w")
        
        #################################################
        
        label_password_repeat_medico = ctk.CTkLabel(self.app_register_usuarios, text="Repita su contraseña", font=self.letra_label)
        label_password_repeat_medico.place(x=395, y=310, anchor="w")
        
        self.entry_password_repeat_medico = ctk.CTkEntry(self.app_register_usuarios, width=170)
        self.entry_password_repeat_medico.place(x=395, y=350, anchor="w")
        
        ################################################
        
        label_correo_medico = ctk.CTkLabel(self.app_register_usuarios, text="Correo", font=self.letra_label)
        label_correo_medico.place(x=395, y=390, anchor="w")
        
        self.entry_correo_medico = ctk.CTkEntry(self.app_register_usuarios, width=170)
        self.entry_correo_medico.place(x=395, y=430, anchor="w")
        
        ################################################
        
        frame_divisor2 = ctk.CTkFrame(self.app_register_usuarios, width=5, height=200)
        frame_divisor2.place(x=625, y=270, anchor="w")
        
        ###################################################
        
        label_usuario_asistente = ctk.CTkLabel(self.app_register_usuarios, text="Usuario Asistente", font=self.letra_label)
        label_usuario_asistente.place(x=700, y=150, anchor="w")
        
        self.entry_usuario_asistente = ctk.CTkEntry(self.app_register_usuarios, width=170)
        self.entry_usuario_asistente.place(x=700, y=190, anchor="w")
        
        #################################################
        
        label_password_asistente = ctk.CTkLabel(self.app_register_usuarios, text="Contraseña", font=self.letra_label)
        label_password_asistente.place(x=700, y=230, anchor="w")
        
        self.entry_password_asistente = ctk.CTkEntry(self.app_register_usuarios, width=170)
        self.entry_password_asistente.place(x=700, y=270, anchor="w")
        
        #################################################
        
        label_password_repeat_asistente = ctk.CTkLabel(self.app_register_usuarios, text="Repita su contraseña", font=self.letra_label)
        label_password_repeat_asistente.place(x=700, y=310, anchor="w")
        
        self.entry_password_repeat_asistente = ctk.CTkEntry(self.app_register_usuarios, width=170)
        self.entry_password_repeat_asistente.place(x=700, y=350, anchor="w")
        
        #################################################
        
        label_correo_asistente = ctk.CTkLabel(self.app_register_usuarios, text="Correo", font=self.letra_label)
        label_correo_asistente.place(x=700, y=390, anchor="w")
        
        self.entry_correo_asistente = ctk.CTkEntry(self.app_register_usuarios, width=170)
        self.entry_correo_asistente.place(x=700, y=430, anchor="w")
        
        #################################################  
        
        
        button_ingresar_user_admin = ctk.CTkButton(self.app_register_usuarios,
                                                 text="Registrar como Administrador", 
                                                 command=self.registrar_usuario_admin)
        button_ingresar_user_admin.place(x=90, y=580, anchor="w")
        
        button_ingresar_user_médico = ctk.CTkButton(self.app_register_usuarios,
                                                 text="Registrar como Médico", 
                                                 command=self.registrar_usuario_medico)
        button_ingresar_user_médico.place(x=290, y=580, anchor="w")
        
        button_ingresar_user_asistente = ctk.CTkButton(self.app_register_usuarios,
                                                 text="Registrar como Asistente", 
                                                 command=self.registrar_usuario_asistente)
        button_ingresar_user_asistente.place(x=450, y=580, anchor="w")
        
        
        
    def registrar_usuario_admin(self):
        usuario_admin = self.entry_user_admin.get()
        password = self.entry_password_admin.get()
        password_repeat = self.entry_repeat_password_admin.get()
        correo = self.entry_correo_admin.get()
        
        if usuario_admin and password and password_repeat and correo != '':
            if len(usuario_admin) > 5:
                if password == password_repeat:
                    if len(password) > 5:
                        if len(correo) < 31:
                            dato = self.db.verificar_existencia_admin(usuario=usuario_admin)
                            if dato is None:
                                verified = self.db.insertar_usuario_admin(usuario=usuario_admin, password=password_repeat, correo=correo)
                                if verified == True:
                                        CTkMessagebox(title="Administración | Registro de Usuarios",
                                        message="El usuario admin fue registrado correctamente!",
                                        icon="check",
                                        option_1="Cerrar",
                                        fade_in_duration=35)
                                        self.limpiar_datos_admin()
                                else:
                                    CTkMessagebox(title="Administración | Registro de Usuarios",
                                    message="No se pudo registrar el usuario, intentelo más tarde!",
                                    icon="info",
                                    option_1="Cerrar",
                                    fade_in_duration=35)
                            else:
                                CTkMessagebox(title="Administración | Registro de Usuarios",
                                message="Este Usuario admin ya se encuentra registrado!",
                                icon="info",
                                option_1="Cerrar",
                                fade_in_duration=35)
                        else:
                            CTkMessagebox(title="Administración | Registro de Usuarios",
                            message="El correo no puede ser mayor a 30!",
                            icon="cancel",
                            option_1="Cerrar",
                            fade_in_duration=35)
                    else:
                        CTkMessagebox(title="Administración | Registro de Usuarios",
                          message="La contraseña se debe ser mayor a 5!",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
                else:
                    CTkMessagebox(title="Administración | Registro de Usuarios",
                          message="Las contraseñas no coinciden!",
                          icon="info",
                          option_1="Cerrar",
                          fade_in_duration=35)
            else:
                CTkMessagebox(title="Administración | Registro de Usuarios",
                          message="El usuario debe ser mayor a 5!",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
        else:
            CTkMessagebox(title="Administración | Registro de Usuarios",
                          message="Todos los campos son necesarios!",
                          icon="info",
                          option_1="Cerrar",
                          fade_in_duration=35)
            
    def registrar_usuario_medico(self):
        usuario_medico = self.entry_usuario_medico.get()
        password_medico = self.entry_password_medico.get()
        password_repeat_medico = self.entry_password_repeat_medico.get()
        correo_medico = self.entry_correo_medico.get()
        
        if usuario_medico and password_medico and password_repeat_medico and correo_medico != '':
            if len(usuario_medico) > 5:
                if password_medico == password_repeat_medico:
                    if len(password_medico) > 5:
                        if len(correo_medico) < 31:
                            dato = self.db.verificar_existencia_medico(usuario=usuario_medico)
                            if dato is None:
                                verified = self.db.insertar_usuario_medico(usuario=usuario_medico, password=password_repeat_medico, correo=correo_medico)
                                if verified == True:
                                        CTkMessagebox(title="Administración | Registro de Usuarios",
                                        message="El usuario médico fue registrado correctamente!",
                                        icon="check",
                                        option_1="Cerrar",
                                        fade_in_duration=35)
                                        self.limpiar_datos_medico()
                                else:
                                    CTkMessagebox(title="Administración | Registro de Usuarios",
                                    message="No se pudo registrar el usuario, intentelo más tarde!",
                                    icon="info",
                                    option_1="Cerrar",
                                    fade_in_duration=35)
                            else:
                                CTkMessagebox(title="Administración | Registro de Usuarios",
                                message="Este Usuario admin ya se encuentra registrado!",
                                icon="info",
                                option_1="Cerrar",
                                fade_in_duration=35)
                        else:
                            CTkMessagebox(title="Administración | Registro de Usuarios",
                            message="El correo no puede ser mayor a 30!",
                            icon="cancel",
                            option_1="Cerrar",
                            fade_in_duration=35)
                    else:
                        CTkMessagebox(title="Administración | Registro de Usuarios",
                          message="La contraseña se debe ser mayor a 5!",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
                else:
                    CTkMessagebox(title="Administración | Registro de Usuarios",
                          message="Las contraseñas no coinciden!",
                          icon="info",
                          option_1="Cerrar",
                          fade_in_duration=35)
            else:
                CTkMessagebox(title="Administración | Registro de Usuarios",
                          message="El usuario debe ser mayor a 5!",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
        else:
            CTkMessagebox(title="Administración | Registro de Usuarios",
                          message="Todos los campos son necesarios!",
                          icon="info",
                          option_1="Cerrar",
                          fade_in_duration=35)
            
    def registrar_usuario_asistente(self):
        usuario_asistente = self.entry_usuario_asistente.get()
        password_asistente = self.entry_password_asistente.get()
        password_repeat_asistente = self.entry_password_repeat_asistente.get()
        correo_asistente = self.entry_correo_asistente.get()
        
        if usuario_asistente and password_asistente and password_repeat_asistente and correo_asistente != '':
            if len(usuario_asistente) > 5:
                if password_asistente == password_repeat_asistente:
                    if len(password_asistente) > 5:
                        if len(correo_asistente) < 31:
                            dato = self.db.verificar_existencia_asistente(usuario=usuario_asistente)
                            if dato is None:
                                verified = self.db.insertat_usuario_asistente(usuario=usuario_asistente,password=password_repeat_asistente, correo=correo_asistente)
                                if verified == True:
                                        CTkMessagebox(title="Administración | Registro de Usuarios",
                                        message="El usuario asistente fue registrado correctamente!",
                                        icon="check",
                                        option_1="Cerrar",
                                        fade_in_duration=35)
                                        self.limpiar_datos_asistente()
                                else:
                                    CTkMessagebox(title="Administración | Registro de Usuarios",
                                    message="No se pudo registrar el usuario, intentelo más tarde!",
                                    icon="info",
                                    option_1="Cerrar",
                                    fade_in_duration=35)
                            else:
                                CTkMessagebox(title="Administración | Registro de Usuarios",
                                message="Este Usuario admin ya se encuentra registrado!",
                                icon="info",
                                option_1="Cerrar",
                                fade_in_duration=35)
                        else:
                            CTkMessagebox(title="Administración | Registro de Usuarios",
                            message="El correo no puede ser mayor a 30!",
                            icon="cancel",
                            option_1="Cerrar",
                            fade_in_duration=35)
                    else:
                        CTkMessagebox(title="Administración | Registro de Usuarios",
                          message="La contraseña se debe ser mayor a 5!",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
                else:
                    CTkMessagebox(title="Administración | Registro de Usuarios",
                          message="Las contraseñas no coinciden!",
                          icon="info",
                          option_1="Cerrar",
                          fade_in_duration=35)
            else:
                CTkMessagebox(title="Administración | Registro de Usuarios",
                          message="El usuario debe ser mayor a 5!",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
        else:
            CTkMessagebox(title="Administración | Registro de Usuarios",
                          message="Todos los campos son necesarios!",
                          icon="info",
                          option_1="Cerrar",
                          fade_in_duration=35)
            
    def limpiar_datos_admin(self):
        self.entry_user_admin.delete(0, ctk.END)
        self.entry_password_admin.delete(0, ctk.END)
        self.entry_repeat_password_admin.delete(0, ctk.END)
        self.entry_correo_admin.delete(0, ctk.END)
        
    def limpiar_datos_medico(self):
        self.entry_usuario_medico.delete(0, ctk.END)
        self.entry_password_medico.delete(0, ctk.END)
        self.entry_password_repeat_medico.delete(0, ctk.END)
        self.entry_correo_medico.delete(0, ctk.END)
        
    def limpiar_datos_asistente(self):
        self.entry_usuario_asistente.delete(0, ctk.END)
        self.entry_password_asistente.delete(0, ctk.END)
        self.entry_password_repeat_asistente.delete(0, ctk.END)
        self.entry_correo_asistente.delete(0, ctk.END)
        
        
        
        