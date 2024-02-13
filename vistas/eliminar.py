import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from controlador.controlador import Controlador


class Eliminar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
    ###################################
    #                                 #
        self.db = Controlador()
    #                                 #
    ###################################
        
        
    def delete_window(self):
        self.app_eliminar = ctk.CTkToplevel(self)
        w, h = self.app_eliminar.winfo_screenwidth(), self.app_eliminar.winfo_screenheight()
        x, y = (w / 2) - 475, (h / 2) - 370
        self.app_eliminar.geometry(f"950x660+{int(x)}+{int(y)}")
        self.app_eliminar.grab_set()
        self.app_eliminar.title("Administración | Actualizar historia clínica")
        self.app_eliminar.resizable(0,0)
        
        self.letra_label_divisor = ('Century Gothic', 16)
        self.letra_label = ('Century Gothic', 15)
        
        
        frame_top = ctk.CTkFrame(self.app_eliminar, width=900, height=50)
        frame_top.place(x=475, y=10, anchor="n")
        
        label_divisor = ctk.CTkLabel(frame_top, text="Administración | Eliminar historia clínica                                                                                                                                             ", font=self.letra_label_divisor)
        label_divisor.pack(padx=20, pady=10)
        
        #######################################################################
        
        frame_datos_paciente = ctk.CTkFrame(self.app_eliminar, width=475, height=500)
        frame_datos_paciente.pack(padx=5, pady=(65, 0), side="left")
        
        ####################
        
        label_cedula_paciente = ctk.CTkLabel(frame_datos_paciente, text="Cédula del Paciente", font=self.letra_label)
        label_cedula_paciente.pack(padx=(20,250), pady=(10,555))
        
        self.entry_cedula_paciente = ctk.CTkEntry(frame_datos_paciente, width=150)
        self.entry_cedula_paciente.place(x=20, y=60, anchor="w")
        
        ####################
        
        label_fecha_paciente = ctk.CTkLabel(frame_datos_paciente, text="Fecha", font=self.letra_label)
        label_fecha_paciente.place(x=20, y=90)
        
        self.entry_fecha_paciente = ctk.CTkEntry(frame_datos_paciente, width=150)
        self.entry_fecha_paciente.place(x=20, y=140, anchor="w")
        
        ###############
        
        label_peso_paciente = ctk.CTkLabel(frame_datos_paciente, text="Peso", font=self.letra_label)
        label_peso_paciente.place(x=20, y=180, anchor="w")
        
        self.entry_peso_paciente = ctk.CTkEntry(frame_datos_paciente, width=150)
        self.entry_peso_paciente.place(x=20, y=210, anchor="w")
        
        ##############################
        
        label_tension_paciente = ctk.CTkLabel(frame_datos_paciente, text="Tensión", font=self.letra_label)
        label_tension_paciente.place(x=210, y=100, anchor="w")
        
        self.entry_tension_paciente = ctk.CTkEntry(frame_datos_paciente, width=150)
        self.entry_tension_paciente.place(x=210, y=140, anchor="w")
        
        #######################################
        
        label_id_historia = ctk.CTkLabel(frame_datos_paciente, text="ID-Historia", font=self.letra_label)
        label_id_historia.place(x=210, y=180, anchor="w")
        
        self.entry_id_historia = ctk.CTkEntry(frame_datos_paciente, width=150)
        self.entry_id_historia.place(x=210, y=220, anchor="w")
        
        
        ###########################################
        
        label_talla_paciente = ctk.CTkLabel(frame_datos_paciente, text="Talla", font=self.letra_label)
        label_talla_paciente.place(x=210, y=20, anchor="w")
        
        self.entry_talla_paciente = ctk.CTkEntry(frame_datos_paciente, width=150)
        self.entry_talla_paciente.place(x=210, y=60, anchor="w")
        
        ###############
        
        label_examen_paciente = ctk.CTkLabel(frame_datos_paciente, text="Examen físico", font=self.letra_label)
        label_examen_paciente.place(x=20, y=250, anchor="w")
        
        self.entry_examen_paciente = ctk.CTkTextbox(frame_datos_paciente, width=370, height=70, corner_radius=15)
        self.entry_examen_paciente.place(x=20, y=305, anchor="w")
        
        ###############
        
        label_sintomas_paciente = ctk.CTkLabel(frame_datos_paciente, text="Síntomas", font=self.letra_label)
        label_sintomas_paciente.place(x=20, y=365, anchor="w")
        
        self.entry_sintomas_paciente = ctk.CTkTextbox(frame_datos_paciente, width=370, height=70, corner_radius=15)
        self.entry_sintomas_paciente.place(x=20, y=420, anchor="w")
        
        ###############
        
        label_diagnostico_paciente = ctk.CTkLabel(frame_datos_paciente, text="Diagnóstico", font=self.letra_label)
        label_diagnostico_paciente.place(x=20, y=485, anchor="w")
        
        self.entry_diagnostico_paciente = ctk.CTkTextbox(frame_datos_paciente, width=370, height=70, corner_radius=15)
        self.entry_diagnostico_paciente.place(x=20, y=545, anchor="w")
    
        #######################################################################
        
        frame_datos_paciente2 = ctk.CTkFrame(self.app_eliminar, width=475, height=500)
        frame_datos_paciente2.pack(padx=5, pady=5, side="right")
        
        label_tratamiento_paciente = ctk.CTkLabel(frame_datos_paciente2, text="Tratamiento médico", font=self.letra_label)
        label_tratamiento_paciente.pack(padx=(20,250), pady=(10,470))
        
        self.entry_tratamiento_paciente = ctk.CTkTextbox(frame_datos_paciente2, width=370, height=100, corner_radius=15)
        self.entry_tratamiento_paciente.place(x=20, y=100, anchor="w")
        
        ###################
        
        label_antecendentes_familiar = ctk.CTkLabel(frame_datos_paciente2, text="Antecedentes familiares", font=self.letra_label)
        label_antecendentes_familiar.place(x=20, y=170, anchor="w")
        
        self.entry_antecendentes_familiar = ctk.CTkTextbox(frame_datos_paciente2, width=370, height=120, corner_radius=15)
        self.entry_antecendentes_familiar.place(x=20, y=255, anchor="w")
        
        ########################
        
        label_antecendentes_paciente = ctk.CTkLabel(frame_datos_paciente2, text="Antecendes del Paciente", font=self.letra_label)
        label_antecendentes_paciente.place(x=20, y=335, anchor="w")
        
        self.entry_antecendentes_paciente = ctk.CTkTextbox(frame_datos_paciente2, width=370, height=120, corner_radius=15)
        self.entry_antecendentes_paciente.place(x=20, y=420, anchor="w")
        
        ###############################
        
        self.boton_registrar = ctk.CTkButton(self.app_eliminar, text="Eliminar Historia clínica", command=self.eliminar_historia_clinica)
        self.boton_registrar.place(x=580, y=618, anchor="center")
        
        self.boton_registrar = ctk.CTkButton(self.app_eliminar, text="Consultar Historia clínica", command=self.consultar_historia_clinica)
        self.boton_registrar.place(x=770, y=618, anchor="center")
        
        
    def eliminar_historia_clinica(self):
        cedula_paciente = self.entry_cedula_paciente.get()
        fecha = self.entry_fecha_paciente.get()
        peso = self.entry_peso_paciente.get()
        tension = self.entry_tension_paciente.get()
        talla = self.entry_talla_paciente.get()
        exam_fisico = self.entry_examen_paciente.get("1.0", "end")
        sintomas = self.entry_sintomas_paciente.get("1.0", "end")
        diagnostico = self.entry_diagnostico_paciente.get("1.0", "end")
        tratamiento = self.entry_tratamiento_paciente.get("1.0", "end")
        antecedentes = self.entry_antecendentes_paciente.get("1.0", "end")
        ante_family = self.entry_antecendentes_familiar.get("1.0", "end")
        id_numero_hist = self.entry_id_historia.get()
    
        
        if peso and tension and talla and exam_fisico and sintomas and diagnostico and tratamiento and antecedentes and ante_family != '':
            if cedula_paciente.isdigit():
                if tension.isdigit():
                    if talla.isdigit():
                        if peso.isdigit():
                            dato = self.db.existencia_historia(id_numero_hist=id_numero_hist)
                            if dato is not None:
                                info = CTkMessagebox(title="Eliminar | Confirmación",
                                                     message="¿Está seguro que desea eliminar esta Historia Clínica?",
                                                     option_1="Si",
                                                     option_2="No",
                                                     icon="info",
                                                     fade_in_duration=35)
                                if info.get() == "Si":
                                    
                                    verified = self.db.eliminar_historia_id(cl_id_hist=id_numero_hist)
                                    if verified == True:
                                        CTkMessagebox(title="Clínica | eliminada correctamente",
                                        message="La historia ha sido eliminada correctamente.",
                                        icon="check",
                                        fade_in_duration=35, option_1="Cerrar")
                                        self.entry_cedula_paciente.delete(0, ctk.END)
                                        self.entry_fecha_paciente.delete(0, ctk.END)
                                        self.entry_peso_paciente.delete(0, ctk.END)
                                        self.entry_tension_paciente.delete(0, ctk.END)
                                        self.entry_talla_paciente.delete(0, ctk.END)
                                        self.entry_examen_paciente.delete("1.0", ctk.END)
                                        self.entry_sintomas_paciente.delete("1.0", ctk.END)
                                        self.entry_diagnostico_paciente.delete("1.0", ctk.END)
                                        self.entry_tratamiento_paciente.delete("1.0", ctk.END)
                                        self.entry_antecendentes_paciente.delete("1.0", ctk.END)
                                        self.entry_antecendentes_familiar.delete("1.0", ctk.END)
                                        self.entry_id_historia.delete(0, ctk.END)
                                        self.app_eliminar.destroy()
                                    else:
                                        CTkMessagebox(title="Clínica | Error",
                                        message="No se pudo eliminar la Historía clínica, intente de nuevo.",
                                        icon="cancel",
                                        fade_in_duration=35, option_1="Cerrar")
                                        
                                else:
                                    print("o")
                            else:
                                self.entry_id_historia.delete(0, ctk.END)
                                CTkMessagebox(title="Clínica | Error de Actualización!",
                                message="Ese ID-Historia no existe!",
                                icon="cancel",
                                fade_in_duration=35, option_1="Cerrar")
                        else:
                            CTkMessagebox(title="Clínica | Error",
                            message="El campo del Peso no puede contener letras!",
                            icon="cancel",
                            fade_in_duration=35, option_1="Cerrar")
                    else:
                        CTkMessagebox(title="Clínica | Error",
                          message="El campo de la Talla no puede contener letras!",
                          icon="cancel",
                          fade_in_duration=35, option_1="Cerrar")
                else:
                    CTkMessagebox(title="Clínica | Error",
                          message="El campo de Tensión no puede contener letras!",
                          icon="cancel",
                          fade_in_duration=35, option_1="Cerrar")
            else:
                CTkMessagebox(title="Clínica | Error",
                          message="La cédula no puede contener letras",
                          icon="cancel",
                          fade_in_duration=35, option_1="Cerrar")
        else:
            CTkMessagebox(title="Clínica | Error",
                          message="Todos los campos son necesarios!",
                          icon="cancel",
                          fade_in_duration=35, option_1="Cerrar")
            
            
    def consultar_historia_clinica(self):
        id_numero_hist = self.entry_id_historia.get()
        cedula_paciente = self.entry_cedula_paciente.get()
        fecha = self.entry_fecha_paciente.get()
        peso = self.entry_peso_paciente.get()
        tension = self.entry_tension_paciente.get()
        talla = self.entry_talla_paciente.get()
        exam_fisico = self.entry_examen_paciente.get("1.0", "end")
        sintomas = self.entry_sintomas_paciente.get("1.0", "end")
        diagnostico = self.entry_diagnostico_paciente.get("1.0", "end")
        tratamiento = self.entry_tratamiento_paciente.get("1.0", "end")
        antecedentes = self.entry_antecendentes_paciente.get("1.0", "end")
        ante_family = self.entry_antecendentes_familiar.get("1.0", "end")
        
        
        if  id_numero_hist != '':
            if id_numero_hist.isdigit():
                dato = self.db.existencia_historia(id_numero_hist=id_numero_hist)
                if dato is not None:
                                self.entry_id_historia.delete(0, ctk.END)
                                self.entry_cedula_paciente.delete(0, ctk.END)
                                self.entry_fecha_paciente.delete(0, ctk.END)
                                self.entry_peso_paciente.delete(0, ctk.END)
                                self.entry_tension_paciente.delete(0, ctk.END)
                                self.entry_talla_paciente.delete(0, ctk.END)
                                self.entry_examen_paciente.delete("1.0", ctk.END)
                                self.entry_sintomas_paciente.delete("1.0", ctk.END)
                                self.entry_diagnostico_paciente.delete("1.0", ctk.END)
                                self.entry_tratamiento_paciente.delete("1.0", ctk.END)
                                self.entry_antecendentes_paciente.delete("1.0", ctk.END)
                                self.entry_antecendentes_familiar.delete("1.0", ctk.END)
                
                                c_id_historia = dato[0]
                                c_cedula_paciente = dato[1]
                                c_fecha = dato[2]
                                c_peso = dato[3]
                                c_tension = dato[4]
                                c_talla = dato[5]
                                c_exam_fisico = dato[6]
                                c_sintomas = dato[7]
                                c_diagnostico = dato[8]
                                c_tramiento = dato[9]
                                c_antecedentes = dato[10]
                                c_ante_family = dato[11]
                                    
                                self.entry_id_historia.insert(0, c_id_historia)
                                self.entry_cedula_paciente.insert(0, c_cedula_paciente)
                                self.entry_fecha_paciente.insert(0, c_fecha)
                                self.entry_peso_paciente.insert(0, c_peso)
                                self.entry_tension_paciente.insert(0, c_tension)
                                self.entry_talla_paciente.insert(0, c_talla)
                                self.entry_examen_paciente.insert("1.0", c_exam_fisico)
                                self.entry_sintomas_paciente.insert("1.0", c_sintomas)
                                self.entry_diagnostico_paciente.insert("1.0", c_diagnostico)
                                self.entry_tratamiento_paciente.insert("1.0", c_tramiento)
                                self.entry_antecendentes_paciente.insert("1.0", c_antecedentes)
                                self.entry_antecendentes_familiar.insert("1.0", c_ante_family)
                else:
                    CTkMessagebox(title="Clínica | Error",
                    message="Ese ID-Historia Clínica no existe!",
                    icon="cancel",
                    fade_in_duration=35, option_1="Cerrar")
                    self.entry_id_historia.delete(0, ctk.END)
                    
            else:
                CTkMessagebox(title="Clínica | Error",
                    message="El ID-Historia Clínica solo puede contener números!",
                    icon="cancel",
                    fade_in_duration=35, option_1="Cerrar")
        else:
            CTkMessagebox(title="Clínica | Error",
                                message="El ID-Historia Clínica es requerido para hacer la consulta!",
                                icon="cancel",
                                fade_in_duration=35, option_1="Cerrar")
            
                         
            