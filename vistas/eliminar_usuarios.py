import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from controlador.controlador import Controlador

class Eliminar_usuarios(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        
        self.db = Controlador()
        
    def eliminar_usuarios_window(self):
        self.app_eliminar_usuarios = ctk.CTkToplevel(self)
        w, h = self.app_eliminar_usuarios.winfo_screenwidth(), self.app_eliminar_usuarios.winfo_screenheight()
        x, y = (w / 2) - 475, (h / 2) - 370
        self.app_eliminar_usuarios.geometry(f"950x660+{int(x)}+{int(y)}")
        self.app_eliminar_usuarios.grab_set()
        self.app_eliminar_usuarios.title("Administración | Eliminar Usuarios")
        self.app_eliminar_usuarios.resizable(0,0)
        
        self.letra_label_divisor = ('Century Gothic', 16)
        self.letra_label = ('Century Gothic', 15)
        
        ###########################################
        
        frame_top = ctk.CTkFrame(self.app_eliminar_usuarios, width=900, height=50)
        frame_top.place(x=475, y=10, anchor="n")
        
        label_divisor = ctk.CTkLabel(frame_top, text="Administración | Eliminación de Usuarios                                                                                                                                        ", font=self.letra_label_divisor)
        label_divisor.pack(padx=20, pady=10)
        
        #####################################################
        
        label_user_admin = ctk.CTkLabel(self.app_eliminar_usuarios, text="Usuario admin", font=self.letra_label)
        label_user_admin.place(x=80, y=150, anchor="w")
        
        self.entry_user_admin = ctk.CTkEntry(self.app_eliminar_usuarios, width=170)
        self.entry_user_admin.place(x=80, y=190, anchor="w")
        
        #####################################################
        
        label_password_admin = ctk.CTkLabel(self.app_eliminar_usuarios, text="Contraseña", font=self.letra_label)
        label_password_admin.place(x=80, y=230, anchor="w")
        
        self.entry_password_admin = ctk.CTkEntry(self.app_eliminar_usuarios, width=170)
        self.entry_password_admin.place(x=80, y=270, anchor="w")
        
        #####################################################
        
        label_repeat_password_admin = ctk.CTkLabel(self.app_eliminar_usuarios, text="Repita su contraseña", font=self.letra_label)
        label_repeat_password_admin.place(x=80, y=310, anchor="w")
        
        self.entry_repeat_password_admin = ctk.CTkEntry(self.app_eliminar_usuarios, width=170)
        self.entry_repeat_password_admin.place(x=80, y=350, anchor="w")
        
        ######################################
        
        label_correo_admin = ctk.CTkLabel(self.app_eliminar_usuarios, text="Correo", font=self.letra_label)
        label_correo_admin.place(x=80, y=390, anchor="w")
        
        self.entry_correo_admin = ctk.CTkEntry(self.app_eliminar_usuarios, width=170)
        self.entry_correo_admin.place(x=80, y=430, anchor="w")
        
        ######################################
        
        label_id_admin = ctk.CTkLabel(self.app_eliminar_usuarios, text="ID-Usuario", font=self.letra_label)
        label_id_admin.place(x=80, y=470, anchor="w")
        
        self.entry_id_admin = ctk.CTkEntry(self.app_eliminar_usuarios, width=170)
        self.entry_id_admin.place(x=80, y=510, anchor="w")
        
        ######################################
        
        frame_divisor = ctk.CTkFrame(self.app_eliminar_usuarios, width=5, height=200)
        frame_divisor.place(x=325, y=270, anchor="w")
        
        ##################################################
        
        label_usuario_medico = ctk.CTkLabel(self.app_eliminar_usuarios, text="Usuario Médico", font=self.letra_label)
        label_usuario_medico.place(x=395, y=150, anchor="w")
        
        self.entry_usuario_medico = ctk.CTkEntry(self.app_eliminar_usuarios, width=170)
        self.entry_usuario_medico.place(x=395, y=190, anchor="w")
        
        #################################################
        
        label_passentry_password_medico = ctk.CTkLabel(self.app_eliminar_usuarios, text="Contraseña", font=self.letra_label)
        label_passentry_password_medico.place(x=395, y=230, anchor="w")
        
        self.entry_password_medico = ctk.CTkEntry(self.app_eliminar_usuarios, width=170)
        self.entry_password_medico.place(x=395, y=270, anchor="w")
        
        #################################################
        
        label_password_repeat_medico = ctk.CTkLabel(self.app_eliminar_usuarios, text="Repita su contraseña", font=self.letra_label)
        label_password_repeat_medico.place(x=395, y=310, anchor="w")
        
        self.entry_password_repeat_medico = ctk.CTkEntry(self.app_eliminar_usuarios, width=170)
        self.entry_password_repeat_medico.place(x=395, y=350, anchor="w")
        
        ################################################
        
        label_correo_medico = ctk.CTkLabel(self.app_eliminar_usuarios, text="Correo", font=self.letra_label)
        label_correo_medico.place(x=395, y=390, anchor="w")
        
        self.entry_correo_medico = ctk.CTkEntry(self.app_eliminar_usuarios, width=170)
        self.entry_correo_medico.place(x=395, y=430, anchor="w")
        
        ################################################
        
        label_id_medico = ctk.CTkLabel(self.app_eliminar_usuarios, text="ID-Usuario", font=self.letra_label)
        label_id_medico.place(x=395, y=470, anchor="w")
        
        self.entry_id_medico = ctk.CTkEntry(self.app_eliminar_usuarios, width=170)
        self.entry_id_medico.place(x=395, y=510, anchor="w")
        
        ################################################
        
        frame_divisor2 = ctk.CTkFrame(self.app_eliminar_usuarios, width=5, height=200)
        frame_divisor2.place(x=625, y=270, anchor="w")
        
        ###################################################
        
        label_usuario_asistente = ctk.CTkLabel(self.app_eliminar_usuarios, text="Usuario Asistente", font=self.letra_label)
        label_usuario_asistente.place(x=700, y=150, anchor="w")
        
        self.entry_usuario_asistente = ctk.CTkEntry(self.app_eliminar_usuarios, width=170)
        self.entry_usuario_asistente.place(x=700, y=190, anchor="w")
        
        #################################################
        
        label_password_asistente = ctk.CTkLabel(self.app_eliminar_usuarios, text="Contraseña", font=self.letra_label)
        label_password_asistente.place(x=700, y=230, anchor="w")
        
        self.entry_password_asistente = ctk.CTkEntry(self.app_eliminar_usuarios, width=170)
        self.entry_password_asistente.place(x=700, y=270, anchor="w")
        
        #################################################
        
        label_password_repeat_asistente = ctk.CTkLabel(self.app_eliminar_usuarios, text="Repita su contraseña", font=self.letra_label)
        label_password_repeat_asistente.place(x=700, y=310, anchor="w")
        
        self.entry_password_repeat_asistente = ctk.CTkEntry(self.app_eliminar_usuarios, width=170)
        self.entry_password_repeat_asistente.place(x=700, y=350, anchor="w")
        
        #################################################
        
        label_correo_asistente = ctk.CTkLabel(self.app_eliminar_usuarios, text="Correo", font=self.letra_label)
        label_correo_asistente.place(x=700, y=390, anchor="w")
        
        self.entry_correo_asistente = ctk.CTkEntry(self.app_eliminar_usuarios, width=170)
        self.entry_correo_asistente.place(x=700, y=430, anchor="w")
        
        ################################################
        
        label_id_asistente = ctk.CTkLabel(self.app_eliminar_usuarios, text="ID-Usuario", font=self.letra_label)
        label_id_asistente.place(x=700, y=470, anchor="w")
        
        self.entry_id_asistente = ctk.CTkEntry(self.app_eliminar_usuarios, width=170)
        self.entry_id_asistente.place(x=700, y=510, anchor="w")
        
        #################################################  
        
        
        button_ingresar_user_admin = ctk.CTkButton(self.app_eliminar_usuarios,
                                                 text="Eliminar",
                                                 width=12, 
                                                 command=self.eliminar_usuario_admin)
        button_ingresar_user_admin.place(x=80, y=600, anchor="w")
        
        button_consultar_admin = ctk.CTkButton(self.app_eliminar_usuarios, 
                                               text="Consultar",
                                               width=12,
                                               command=self.consulta_usuario_admin)
        button_consultar_admin.place(x=160, y=600, anchor="w")
        
        ###################################################################
        
        button_actualizar_user_medico = ctk.CTkButton(self.app_eliminar_usuarios,
                                                 text="Eliminar",
                                                 width=12, 
                                                 command=self.eliminar_usuario_medico)
        button_actualizar_user_medico.place(x=395, y=600, anchor="w")
        
        button_consultar_medico = ctk.CTkButton(self.app_eliminar_usuarios,
                                                 text="Consultar",
                                                 width=12, 
                                                 command=self.consultar_usuario_medico)
        button_consultar_medico.place(x=475, y=600, anchor="w")
        
        ###################################################################
        
        button_actualizar_user_asistente = ctk.CTkButton(self.app_eliminar_usuarios,
                                                 text="Eliminar",
                                                 width=12, 
                                                 command=self.eliminar_usuario_asistente)
        button_actualizar_user_asistente.place(x=700, y=600, anchor="w")
        
        button_consultar_asistente = ctk.CTkButton(self.app_eliminar_usuarios,
                                                 text="Consultar",
                                                 width=12, 
                                                 command=self.consultar_usuario_asistente)
        button_consultar_asistente.place(x=780, y=600, anchor="w")
        
    def consulta_usuario_admin(self):
        id_user = self.entry_id_admin.get()
        
        if id_user != '':
            if id_user.isdigit():
                if len(id_user) < 12:
                    dato = self.db.consulta_admin(id_user=id_user)
                    if dato is not None:
                        c_id_admin = dato[0]
                        c_usuario_admin = dato[1]
                        c_password_admin = dato[2]
                        c_correo_admin = dato[3]
                        
                        self.limpiar_datos_admin()
                        
                        self.entry_id_admin.insert(0, c_id_admin)
                        self.entry_user_admin.insert(0, c_usuario_admin)
                        self.entry_password_admin.insert(0, c_password_admin)
                        self.entry_repeat_password_admin.insert(0, c_password_admin)
                        self.entry_correo_admin.insert(0, c_correo_admin)
                    else:
                        CTkMessagebox(title="Administración | Error de consulta",
                          message="Ese ID-Usuario no existe!",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
                        self.limpiar_datos_admin()
                        
                else:
                    CTkMessagebox(title="Administración | Error de consulta",
                          message="Ingrese un ID-Usuario válido!",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
            else:
                CTkMessagebox(title="Administración | Error de consulta",
                message="El ID-Usuario no puede contener números!",
                icon="cancel",
                option_1="Cerrar",
                fade_in_duration=35)
                
        else:
            CTkMessagebox(title="Administración | Error de consulta",
                          message="El ID-Usuario es requerido para consultar",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
            
        
        
        
    def eliminar_usuario_admin(self):
        usuario_admin = self.entry_user_admin.get()
        password = self.entry_password_admin.get()
        password_repeat = self.entry_repeat_password_admin.get()
        correo = self.entry_correo_admin.get()
        id_user = self.entry_id_admin.get()
        
        if usuario_admin and password and password_repeat and correo and id_user != '':
            if len(usuario_admin) > 5:
                if password == password_repeat:
                    if len(password) > 5:
                        if len(correo) < 31:
                            dato = self.db.verificar_existencia_admin(usuario=usuario_admin)
                            if dato is not None:
                                info = CTkMessagebox(title="Adminmistración | Eliminación",
                                                     message="¿Está seguro que desea eliminar este usuario Admin?",
                                                     option_1="Si",
                                                     option_2="No",
                                                     fade_in_duration=35)
                                if info.get() == "Si":
                                    verified = self.db.delete_admin(id_user=id_user)
                                    if verified == True:
                                        CTkMessagebox(title="Administración | Eliminación de Usuarios",
                                        message="El usuario admin fue eliminado correctamente!",
                                        icon="check",
                                        option_1="Cerrar",
                                        fade_in_duration=35)
                                        self.limpiar_datos_admin()
                                    else:
                                        CTkMessagebox(title="Administración | Eliminación de Usuarios",
                                        message="No se pudo eliminar el usuario, intentelo más tarde!",
                                        icon="info",
                                        option_1="Cerrar",
                                        fade_in_duration=35)
                                else:
                                    pass
                            else:
                                CTkMessagebox(title="Administración | Eliminación de Usuarios",
                                message="Este Usuario admin ya se encuentra registrado!",
                                icon="info",
                                option_1="Cerrar",
                                fade_in_duration=35)
                        else:
                            CTkMessagebox(title="Administración | Eliminación de Usuarios",
                            message="El correo no puede ser mayor a 30!",
                            icon="cancel",
                            option_1="Cerrar",
                            fade_in_duration=35)
                    else:
                        CTkMessagebox(title="Administración | Eliminación de Usuarios",
                          message="La contraseña se debe ser mayor a 5!",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
                else:
                    CTkMessagebox(title="Administración | Eliminación de Usuarios",
                          message="Las contraseñas no coinciden!",
                          icon="info",
                          option_1="Cerrar",
                          fade_in_duration=35)
            else:
                CTkMessagebox(title="Administración | Eliminación de Usuarios",
                          message="El usuario debe ser mayor a 5!",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
        else:
            CTkMessagebox(title="Administración | Eliminación de Usuarios",
                          message="Todos los campos son necesarios!",
                          icon="info",
                          option_1="Cerrar",
                          fade_in_duration=35)
            
    def consultar_usuario_medico(self):
        id_user = self.entry_id_medico.get()
        
        if id_user != '':
            if id_user.isdigit():
                if len(id_user) < 12:
                    dato = self.db.consulta_medico(id_user=id_user)
                    if dato is not None:
                        c_id_medico = dato[0]
                        c_usuario_medico = dato[1]
                        c_password_medico = dato[2]
                        c_correo_medico = dato[3]
                        
                        self.limpiar_datos_medico()
                        
                        self.entry_id_medico.insert(0, c_id_medico)
                        self.entry_usuario_medico.insert(0, c_usuario_medico)
                        self.entry_password_medico.insert(0, c_password_medico)
                        self.entry_password_repeat_medico.insert(0, c_password_medico)
                        self.entry_correo_medico.insert(0, c_correo_medico)
                    else:
                        CTkMessagebox(title="Administración | Error de consulta",
                          message="Ese ID-Usuario no existe!",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
                        self.limpiar_datos_admin()
                        
                else:
                    CTkMessagebox(title="Administración | Error de consulta",
                          message="Ingrese un ID-Usuario válido!",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
            else:
                CTkMessagebox(title="Administración | Error de consulta",
                message="El ID-Usuario no puede contener números!",
                icon="cancel",
                option_1="Cerrar",
                fade_in_duration=35)
                
        else:
            CTkMessagebox(title="Administración | Error de consulta",
                          message="El ID-Usuario es requerido para consultar",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
        
            
    def eliminar_usuario_medico(self):
        usuario_medico = self.entry_usuario_medico.get()
        password_medico = self.entry_password_medico.get()
        password_repeat_medico = self.entry_password_repeat_medico.get()
        correo_medico = self.entry_correo_medico.get()
        id_user = self.entry_id_medico.get()
        
        if usuario_medico and password_medico and password_repeat_medico and correo_medico and id_user != '':
            if len(usuario_medico) > 5:
                if password_medico == password_repeat_medico:
                    if len(password_medico) > 5:
                        if len(correo_medico) < 31:
                            dato = self.db.verificar_existencia_medico(usuario=usuario_medico)
                            if dato is not None:
                                info = CTkMessagebox(title="Administración | Eliminación",
                                                     message="¿Estpa seguro que desea eliminar este usuario Médico?",
                                                     option_1="Si",
                                                     option_2="No",
                                                     fade_in_duration=35)
                                if info.get() == "Si":
                                    verified = self.db.delete_medico(id_user=id_user)
                                    if verified == True:
                                        CTkMessagebox(title="Administración | Eliminar de Usuarios",
                                        message="El usuario médico fue eliminado correctamente!",
                                        icon="check",
                                        option_1="Cerrar",
                                        fade_in_duration=35)
                                        self.limpiar_datos_medico()
                                    else:
                                        CTkMessagebox(title="Administración | Eliminación de Usuarios",
                                        message="No se pudo eliminar el usuario, intentelo más tarde!",
                                        icon="info",
                                        option_1="Cerrar",
                                        fade_in_duration=35)
                                else:
                                    pass
                            else:
                                CTkMessagebox(title="Administración | Eliminación de Usuarios",
                                message="Este Usuario admin ya se encuentra registrado!",
                                icon="info",
                                option_1="Cerrar",
                                fade_in_duration=35)
                        else:
                            CTkMessagebox(title="Administración | Eliminación de Usuarios",
                            message="El correo no puede ser mayor a 30!",
                            icon="cancel",
                            option_1="Cerrar",
                            fade_in_duration=35)
                    else:
                        CTkMessagebox(title="Administración | Eliminación de Usuarios",
                          message="La contraseña se debe ser mayor a 5!",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
                else:
                    CTkMessagebox(title="Administración | Eliminación de Usuarios",
                          message="Las contraseñas no coinciden!",
                          icon="info",
                          option_1="Cerrar",
                          fade_in_duration=35)
            else:
                CTkMessagebox(title="Administración | Eliminación de Usuarios",
                          message="El usuario debe ser mayor a 5!",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
        else:
            CTkMessagebox(title="Administración | Eliminación de Usuarios",
                          message="Todos los campos son necesarios!",
                          icon="info",
                          option_1="Cerrar",
                          fade_in_duration=35)
            
    def consultar_usuario_asistente(self):
        id_user = self.entry_id_asistente.get()
        
        if id_user != '':
            if id_user.isdigit():
                if len(id_user) < 12:
                    dato = self.db.consulta_asistente(id_user=id_user)
                    if dato is not None:
                        c_id_asistente = dato[0]
                        c_usuario_asistente = dato[1]
                        c_password_asistente = dato[2]
                        c_correo_asistente = dato[3]
                        
                        self.limpiar_datos_asistente()
                        
                        self.entry_id_asistente.insert(0, c_id_asistente)
                        self.entry_usuario_asistente.insert(0, c_usuario_asistente)
                        self.entry_password_asistente.insert(0, c_password_asistente)
                        self.entry_password_repeat_asistente.insert(0, c_password_asistente)
                        self.entry_correo_asistente.insert(0, c_correo_asistente)
                    else:
                        CTkMessagebox(title="Administración | Error de consulta",
                          message="Ese ID-Usuario no existe!",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
                        self.limpiar_datos_admin()
                        
                else:
                    CTkMessagebox(title="Administración | Error de consulta",
                          message="Ingrese un ID-Usuario válido!",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
            else:
                CTkMessagebox(title="Administración | Error de consulta",
                message="El ID-Usuario no puede contener números!",
                icon="cancel",
                option_1="Cerrar",
                fade_in_duration=35)
                
        else:
            CTkMessagebox(title="Administración | Error de consulta",
                          message="El ID-Usuario es requerido para consultar",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
            
    def eliminar_usuario_asistente(self):
        usuario_asistente = self.entry_usuario_asistente.get()
        password_asistente = self.entry_password_asistente.get()
        password_repeat_asistente = self.entry_password_repeat_asistente.get()
        correo_asistente = self.entry_correo_asistente.get()
        id_user = self.entry_id_asistente.get()
        
        if usuario_asistente and id_user and password_asistente and password_repeat_asistente and correo_asistente != '':
            if len(usuario_asistente) > 5:
                if password_asistente == password_repeat_asistente:
                    if len(password_asistente) > 5:
                        if len(correo_asistente) < 31:
                            dato = self.db.verificar_existencia_asistente(usuario=usuario_asistente)
                            if dato is not None:
                                info = CTkMessagebox(title="Administración | Eliminación",
                                                    message="¿Está seguro que desea eliminar este usuario Asistente?",
                                                    option_1="Si",
                                                    option_2="No",
                                                     fade_in_duration=35)
                                if info.get() == "Si":
                                    verified = self.db.delete_asistente(id_user=id_user)
                                    if verified == True:
                                        CTkMessagebox(title="Administración | Eliminación de Usuarios",
                                        message="El usuario asistente fue eliminado correctamente!",
                                        icon="check",
                                        option_1="Cerrar",
                                        fade_in_duration=35)
                                        self.limpiar_datos_asistente()
                                    else:
                                        CTkMessagebox(title="Administración | Eliminación de Usuarios",
                                        message="No se pudo registrar el usuario, intentelo más tarde!",
                                        icon="info",
                                        option_1="Cerrar",
                                        fade_in_duration=35)
                                else:
                                    pass

                            else:
                                CTkMessagebox(title="Administración | Eliminación de Usuarios",
                                message="Este Usuario admin ya se encuentra registrado!",
                                icon="info",
                                option_1="Cerrar",
                                fade_in_duration=35)
                        else:
                            CTkMessagebox(title="Administración | Eliminación de Usuarios",
                            message="El correo no puede ser mayor a 30!",
                            icon="cancel",
                            option_1="Cerrar",
                            fade_in_duration=35)
                    else:
                        CTkMessagebox(title="Administración | Eliminación de Usuarios",
                          message="La contraseña se debe ser mayor a 5!",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
                else:
                    CTkMessagebox(title="Administración | Eliminación de Usuarios",
                          message="Las contraseñas no coinciden!",
                          icon="info",
                          option_1="Cerrar",
                          fade_in_duration=35)
            else:
                CTkMessagebox(title="Administración | Eliminación de Usuarios",
                          message="El usuario debe ser mayor a 5!",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
        else:
            CTkMessagebox(title="Administración | Eliminación de Usuarios",
                          message="Todos los campos son necesarios!",
                          icon="info",
                          option_1="Cerrar",
                          fade_in_duration=35)
            
    def limpiar_datos_admin(self):
        self.entry_user_admin.delete(0, ctk.END)
        self.entry_password_admin.delete(0, ctk.END)
        self.entry_repeat_password_admin.delete(0, ctk.END)
        self.entry_correo_admin.delete(0, ctk.END)
        self.entry_id_admin.delete(0, ctk.END)
        
    def limpiar_datos_medico(self):
        self.entry_usuario_medico.delete(0, ctk.END)
        self.entry_password_medico.delete(0, ctk.END)
        self.entry_password_repeat_medico.delete(0, ctk.END)
        self.entry_correo_medico.delete(0, ctk.END)
        self.entry_id_medico.delete(0, ctk.END)
        
    def limpiar_datos_asistente(self):
        self.entry_usuario_asistente.delete(0, ctk.END)
        self.entry_password_asistente.delete(0, ctk.END)
        self.entry_password_repeat_asistente.delete(0, ctk.END)
        self.entry_correo_asistente.delete(0, ctk.END)
        self.entry_id_asistente.delete(0, ctk.END)
        
        
        
        