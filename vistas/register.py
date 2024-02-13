import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from controlador.controlador import Controlador
from datetime import datetime

class Register(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.db = Controlador()
        
    def register_window(self):
        self.app_register = ctk.CTkToplevel(self)
        w, h = self.app_register.winfo_screenwidth(), self.app_register.winfo_screenheight()
        x, y = (w / 2) - 475, (h / 2) - 370
        self.app_register.geometry(f"950x660+{int(x)}+{int(y)}")
        self.app_register.grab_set()
        self.app_register.title("Administración | Registrar historia clínica")
        self.app_register.resizable(0,0)
        
        self.letra_label_divisor = ('Century Gothic', 16)
        self.letra_label = ('Century Gothic', 15)
        
        
        frame_top = ctk.CTkFrame(self.app_register, width=900, height=50)
        frame_top.place(x=475, y=10, anchor="n")
        
        label_divisor = ctk.CTkLabel(frame_top, text="Administración | Registrar historia clínica                                                                                                                                             ", font=self.letra_label_divisor)
        label_divisor.pack(padx=20, pady=10)
        
        #######################################################################
        
        frame_datos_paciente = ctk.CTkFrame(self.app_register, width=475, height=500)
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
        
        ###############
        
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
        
        frame_datos_paciente2 = ctk.CTkFrame(self.app_register, width=475, height=500)
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
        
        self.boton_registrar = ctk.CTkButton(self.app_register, text="Registrar Historia clínica", command=self.registrar_historia_clinica)
        self.boton_registrar.place(x=580, y=615, anchor="center")
        
        
    def registrar_historia_clinica(self):
        cedula_paciente = self.entry_cedula_paciente.get()
        fecha = self.entry_fecha_paciente.get()
        peso = self.entry_peso_paciente.get()
        tension = self.entry_tension_paciente.get()
        talla = self.entry_talla_paciente.get()
        exam_fisico = self.entry_examen_paciente.get("1.0", "end-1c")
        sintomas = self.entry_sintomas_paciente.get("1.0", "end-1c")
        diagnostico = self.entry_diagnostico_paciente.get("1.0", "end-1c")
        tratamiento = self.entry_tratamiento_paciente.get("1.0", "end-1c")
        antecedentes = self.entry_antecendentes_paciente.get("1.0", "end-1c")
        ante_family = self.entry_antecendentes_familiar.get("1.0", "end-1c")
        
        fecha_hoy = datetime.now()
        
        if cedula_paciente and fecha and peso and tension and talla and exam_fisico and sintomas and diagnostico and tratamiento and antecedentes and ante_family != '':
            if cedula_paciente.isdigit():
                if tension.isdigit():
                    if talla.isdigit():
                        if peso.isdigit():
                            dato = self.db.existencia_paciente_cedula(cedula=cedula_paciente)
                            if dato is not None:
                                self.db.registrar_historia_clinica(cedula_paciente, fecha, peso, tension, talla, exam_fisico, sintomas, diagnostico, tratamiento, antecedentes, ante_family)
                                CTkMessagebox(title="Clínica | Registrado correctamente",
                                message="La historia ha sido registrada correctamente!",
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
                            else:
                                CTkMessagebox(title="Clínica | Error de Registro!",
                                message="Este paciente no se encuentra registrado!",
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
        