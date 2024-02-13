import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from controlador.controlador import Controlador

class Registrar_pacientes(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        
        self.db = Controlador()
        
    def register_pacientes_window(self):
        self.app_register_pacientes = ctk.CTkToplevel(self)
        w, h = self.app_register_pacientes.winfo_screenwidth(), self.app_register_pacientes.winfo_screenheight()
        x, y = (w / 2) - 475, (h / 2) - 370
        self.app_register_pacientes.geometry(f"950x660+{int(x)}+{int(y)}")
        self.app_register_pacientes.grab_set()
        self.app_register_pacientes.title("Administración | Registrar Pacientes")
        self.app_register_pacientes.resizable(0,0)
        
        self.letra_label_divisor = ('Century Gothic', 16)
        self.letra_label = ('Century Gothic', 15)
        
        ###########################################
        
        frame_top = ctk.CTkFrame(self.app_register_pacientes, width=900, height=50)
        frame_top.place(x=475, y=10, anchor="n")
        
        label_divisor = ctk.CTkLabel(frame_top, text="Administración | Registro de Pacientes                                                                                                                                        ", font=self.letra_label_divisor)
        label_divisor.pack(padx=20, pady=10)
        
        #####################################################
        
        label_cedula_paciente = ctk.CTkLabel(self.app_register_pacientes, text="Cédula", font=self.letra_label)
        label_cedula_paciente.place(x=300, y=150, anchor="w")
        
        self.entry_cedula_paciente = ctk.CTkEntry(self.app_register_pacientes, width=170)
        self.entry_cedula_paciente.place(x=300, y=190, anchor="w")
        
        #####################################################
        
        label_nombres_paciente = ctk.CTkLabel(self.app_register_pacientes, text="Nombres", font=self.letra_label)
        label_nombres_paciente.place(x=300, y=230, anchor="w")
        
        self.entry_nombres_paciente = ctk.CTkEntry(self.app_register_pacientes, width=170)
        self.entry_nombres_paciente.place(x=300, y=270, anchor="w")
        
        #####################################################
        
        label_apellidos_paciente = ctk.CTkLabel(self.app_register_pacientes, text="Apellidos", font=self.letra_label)
        label_apellidos_paciente.place(x=300, y=310, anchor="w")
        
        self.entry_apellidos_paciente = ctk.CTkEntry(self.app_register_pacientes, width=170)
        self.entry_apellidos_paciente.place(x=300, y=350, anchor="w")
        
        #####################################################
        
        label_dir_paciente = ctk.CTkLabel(self.app_register_pacientes, text="Dirección", font=self.letra_label)
        label_dir_paciente.place(x=300, y=390, anchor="w")
        
        self.entry_dir_paciente = ctk.CTkEntry(self.app_register_pacientes, width=370)
        self.entry_dir_paciente.place(x=300, y=430, anchor="w")
        
        #####################################################
        
        label_fecha_nacimiento_paciente = ctk.CTkLabel(self.app_register_pacientes, text="Fecha de Nacimiento", font=self.letra_label)
        label_fecha_nacimiento_paciente.place(x=300, y=470, anchor="w")
        
        self.entry_fecha_nacimiento_paciente = ctk.CTkEntry(self.app_register_pacientes, width=370)
        self.entry_fecha_nacimiento_paciente.place(x=300, y=510, anchor="w")
        
        ##################################################
        
        label_genero_paciente = ctk.CTkLabel(self.app_register_pacientes, text="Genero", font=self.letra_label)
        label_genero_paciente.place(x=500, y=150, anchor="w")
        
        self.entry_genero_paciente = ctk.CTkEntry(self.app_register_pacientes, width=170)
        self.entry_genero_paciente.place(x=500, y=190, anchor="w")
        
        #################################################
        
        label_telefono_paciente = ctk.CTkLabel(self.app_register_pacientes, text="Teléfono", font=self.letra_label)
        label_telefono_paciente.place(x=500, y=230, anchor="w")
        
        self.entry_telefono_paciente = ctk.CTkEntry(self.app_register_pacientes, width=170)
        self.entry_telefono_paciente.place(x=500, y=270, anchor="w")
        
        #################################################
        
        label_edad_paciente = ctk.CTkLabel(self.app_register_pacientes, text="Edad", font=self.letra_label)
        label_edad_paciente.place(x=500, y=310, anchor="w")
        
        self.entry_edad_paciente = ctk.CTkEntry(self.app_register_pacientes, width=170)
        self.entry_edad_paciente.place(x=500, y=350, anchor="w")
        
        ################################################
        
        button_ingresar_paciente = ctk.CTkButton(self.app_register_pacientes,
                                                 text="Registrar", 
                                                 command=self.registrar_paciente)
        button_ingresar_paciente.place(x=415, y=580, anchor="w")
        
        
    def registrar_paciente(self):
        cedula = self.entry_cedula_paciente.get()
        nombres = self.entry_nombres_paciente.get()
        apellidos = self.entry_apellidos_paciente.get()
        direccion = self.entry_dir_paciente.get()
        fecha_nac = self.entry_fecha_nacimiento_paciente.get()
        genero = self.entry_genero_paciente.get()
        telefono = self.entry_telefono_paciente.get()
        edad = self.entry_edad_paciente.get()
        
        if cedula and nombres and apellidos and direccion and fecha_nac and genero and telefono and edad != '':
            if cedula.isdigit():
                if edad.isdigit():
                    if telefono.isdigit():
                        if len(nombres) > 5:
                            if len(apellidos) > 5:
                                if nombres.isdigit() and apellidos.isdigit():
                                    CTkMessagebox(title="Registro | Error!",
                                    message="Los nombres y apellidos no puede contener números!",
                                    icon="cancel",
                                    option_1="Cerrar",
                                    fade_in_duration=35)
                                else:
                                    dato = self.db.existencia_paciente_cedula(cedula=cedula)
                                    if dato is None:
                                        verified = self.db.registrar_pacientes(cedula=cedula, nombres=nombres, apellidos=apellidos, direccion=direccion, fecha_nam=fecha_nac, genero=genero, telefono=telefono, edad=edad)
                                        if verified == True:
                                            CTkMessagebox(title="Registro | Registrado",
                                            message="Paciente registrado correctamente!",
                                            icon="check",
                                            option_1="Cerrar",
                                            fade_in_duration=35)
                                            self.limpiar_datos()
                                        else:
                                            CTkMessagebox(title="Registro | Error",
                                            message="No se pudo registrar el paciente!",
                                            icon="cancel",
                                            option_1="Cerrar",
                                            fade_in_duration=35)
                                            
                                    else:
                                        CTkMessagebox(title="Registro | Error!",
                                        message="Este paciente ya se encuentra registrado!",
                                        icon="cancel",
                                        option_1="Cerrar",
                                        fade_in_duration=35)
                            else:
                                CTkMessagebox(title="Registro | Error!",
                                message="Ingrese apellidos válidos!",
                                icon="cancel",
                                option_1="Cerrar",
                                fade_in_duration=35)
                        else:
                            CTkMessagebox(title="Registro | Error!",
                            message="Ingrese nombres válidos!",
                            icon="cancel",
                            option_1="Cerrar",
                            fade_in_duration=35)
                    else:
                        CTkMessagebox(title="Registro | Error!",
                          message="El número de Teléfono no puede contener letras!",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
                else:
                    CTkMessagebox(title="Registro | Error!",
                          message="La edad no puede contener letras!",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
            else:
                CTkMessagebox(title="Registro | Error!",
                          message="La cédula no puede contener números!",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
        else:
            CTkMessagebox(title="Registro | Error!",
                          message="Todos los campos son necesarios para el registro!",
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)
            
    def limpiar_datos(self):
        self.entry_cedula_paciente.delete(0, ctk.END)
        self.entry_nombres_paciente.delete(0, ctk.END)
        self.entry_apellidos_paciente.delete(0, ctk.END)
        self.entry_dir_paciente.delete(0, ctk.END)
        self.entry_edad_paciente.delete(0, ctk.END)
        self.entry_fecha_nacimiento_paciente.delete(0, ctk.END)
        self.entry_genero_paciente.delete(0, ctk.END)
        self.entry_telefono_paciente.delete(0, ctk.END)
        
        
        