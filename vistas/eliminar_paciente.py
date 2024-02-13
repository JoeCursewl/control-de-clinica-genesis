import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from controlador.controlador import Controlador

class Eliminar_pacientes(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        
        self.db = Controlador()
        
    def eliminar_pacientes_window(self):
        self.app_eliminar_pacientes = ctk.CTkToplevel(self)
        w, h = self.app_eliminar_pacientes.winfo_screenwidth(), self.app_eliminar_pacientes.winfo_screenheight()
        x, y = (w / 2) - 475, (h / 2) - 370
        self.app_eliminar_pacientes.geometry(f"950x660+{int(x)}+{int(y)}")
        self.app_eliminar_pacientes.grab_set()
        self.app_eliminar_pacientes.title("Administración | Eliminación Pacientes")
        self.app_eliminar_pacientes.resizable(0,0)
        
        self.letra_label_divisor = ('Century Gothic', 16)
        self.letra_label = ('Century Gothic', 15)
        
        ###########################################
        
        frame_top = ctk.CTkFrame(self.app_eliminar_pacientes, width=900, height=50)
        frame_top.place(x=475, y=10, anchor="n")
        
        label_divisor = ctk.CTkLabel(frame_top, text="Administración | Eliminación de Pacientes                                                                                                                                        ", font=self.letra_label_divisor)
        label_divisor.pack(padx=20, pady=10)
        
        #####################################################
        
        label_cedula_paciente = ctk.CTkLabel(self.app_eliminar_pacientes, text="Cédula", font=self.letra_label)
        label_cedula_paciente.place(x=300, y=150, anchor="w")
        
        self.entry_cedula_paciente = ctk.CTkEntry(self.app_eliminar_pacientes, width=170)
        self.entry_cedula_paciente.place(x=300, y=190, anchor="w")
        
        #####################################################
        
        label_nombres_paciente = ctk.CTkLabel(self.app_eliminar_pacientes, text="Nombres", font=self.letra_label)
        label_nombres_paciente.place(x=300, y=230, anchor="w")
        
        self.entry_nombres_paciente = ctk.CTkEntry(self.app_eliminar_pacientes, width=170)
        self.entry_nombres_paciente.place(x=300, y=270, anchor="w")
        
        #####################################################
        
        label_apellidos_paciente = ctk.CTkLabel(self.app_eliminar_pacientes, text="Apellidos", font=self.letra_label)
        label_apellidos_paciente.place(x=300, y=310, anchor="w")
        
        self.entry_apellidos_paciente = ctk.CTkEntry(self.app_eliminar_pacientes, width=170)
        self.entry_apellidos_paciente.place(x=300, y=350, anchor="w")
        
        #####################################################
        
        label_dir_paciente = ctk.CTkLabel(self.app_eliminar_pacientes, text="Dirección", font=self.letra_label)
        label_dir_paciente.place(x=300, y=390, anchor="w")
        
        self.entry_dir_paciente = ctk.CTkEntry(self.app_eliminar_pacientes, width=370)
        self.entry_dir_paciente.place(x=300, y=430, anchor="w")
        
        #####################################################
        
        label_fecha_nacimiento_paciente = ctk.CTkLabel(self.app_eliminar_pacientes, text="Fecha de Nacimiento", font=self.letra_label)
        label_fecha_nacimiento_paciente.place(x=300, y=470, anchor="w")
        
        self.entry_fecha_nacimiento_paciente = ctk.CTkEntry(self.app_eliminar_pacientes, width=370)
        self.entry_fecha_nacimiento_paciente.place(x=300, y=510, anchor="w")
        
        ##################################################
        
        label_genero_paciente = ctk.CTkLabel(self.app_eliminar_pacientes, text="Genero", font=self.letra_label)
        label_genero_paciente.place(x=500, y=150, anchor="w")
        
        self.entry_genero_paciente = ctk.CTkEntry(self.app_eliminar_pacientes, width=170)
        self.entry_genero_paciente.place(x=500, y=190, anchor="w")
        
        #################################################
        
        label_telefono_paciente = ctk.CTkLabel(self.app_eliminar_pacientes, text="Teléfono", font=self.letra_label)
        label_telefono_paciente.place(x=500, y=230, anchor="w")
        
        self.entry_telefono_paciente = ctk.CTkEntry(self.app_eliminar_pacientes, width=170)
        self.entry_telefono_paciente.place(x=500, y=270, anchor="w")
        
        #################################################
        
        label_edad_paciente = ctk.CTkLabel(self.app_eliminar_pacientes, text="Edad", font=self.letra_label)
        label_edad_paciente.place(x=500, y=310, anchor="w")
        
        self.entry_edad_paciente = ctk.CTkEntry(self.app_eliminar_pacientes, width=170)
        self.entry_edad_paciente.place(x=500, y=350, anchor="w")
        
        ################################################
        
        button_actualizar_paciente = ctk.CTkButton(self.app_eliminar_pacientes,
                                                 text="Eliminar", 
                                                 command=self.eliminar_paciente)
        button_actualizar_paciente.place(x=315, y=580, anchor="w")
        
        button_consultar_paciente = ctk.CTkButton(self.app_eliminar_pacientes,
                                                 text="Consultar paciente", 
                                                 command=self.consultar_paciente)
        button_consultar_paciente.place(x=515, y=580, anchor="w")
        
        
    def consultar_paciente(self):
        cedula = self.entry_cedula_paciente.get()
        
        if cedula != '':
            if cedula.isdigit():
                if len(cedula) < 11:
                    dato = self.db.existencia_paciente_cedula(cedula=cedula)
                    if dato is not None:
                        c_cedula = dato[0]
                        c_nombres = dato[1]
                        c_apellidos = dato[2]
                        c_direccion = dato[3]
                        c_fecha_nac = dato[4]
                        c_genero = dato[5]
                        c_telefono = dato[6]
                        c_edad = dato[7]
                        
                        self.limpiar_datos()
                        
                        self.entry_cedula_paciente.insert(0, c_cedula)
                        self.entry_nombres_paciente.insert(0, c_nombres)
                        self.entry_apellidos_paciente.insert(0, c_apellidos)
                        self.entry_dir_paciente.insert(0, c_direccion)
                        self.entry_edad_paciente.insert(0, c_edad)
                        self.entry_fecha_nacimiento_paciente.insert(0, c_fecha_nac)
                        self.entry_genero_paciente.insert(0, c_genero)
                        self.entry_telefono_paciente.insert(0, c_telefono)
                    else:
                        CTkMessagebox(title="Consulta | Error",
                        message="Este paciente no existe!",
                        icon="cancel",
                        option_1="Cerrar",
                        fade_in_duration=35)
                        
                    
                else:
                    CTkMessagebox(title="Consulta | Error",
                    message="Ingrese una cédula válida!",
                    icon="cancel",
                    option_1="Cerrar",
                    fade_in_duration=35)
            else:
                CTkMessagebox(title="Consulta | Error",
                message="La cédula no puede contener números!",
                icon="cancel",
                option_1="Cerrar",
                fade_in_duration=35)
        else:
            CTkMessagebox(title="Consulta | Error",
                message="La cédula es necesaria para hacer la consulta!",
                icon="cancel",
                option_1="Cerrar",
                fade_in_duration=35)
            
        
        
    def eliminar_paciente(self):
        cedula = self.entry_cedula_paciente.get()
        nombres = self.entry_nombres_paciente.get()
        apellidos = self.entry_apellidos_paciente.get()
        direccion = self.entry_dir_paciente.get()
        fecha_nac = self.entry_fecha_nacimiento_paciente.get()
        genero = self.entry_genero_paciente.get()
        telefono = self.entry_telefono_paciente.get()
        edad = self.entry_edad_paciente.get()
        
        if cedula and nombres and apellidos != '':
            if cedula.isdigit():
                dato = self.db.existencia_paciente_cedula(cedula=cedula)
                if dato is not None:
                    info = CTkMessagebox(title="Eliminación | Confirmación",
                        message="¿Está seguro que desea eliminar este paciente?",
                        option_1="Si",
                        option_2="No",
                        icon="info",
                        fade_in_duration=35)
                    if info.get() == "Si":
                            self.db.eliminar_paciente(cedula=cedula)
                            self.limpiar_datos()
                            self.app_eliminar_pacientes.destroy()
                            CTkMessagebox(title="Eliminado | Administración",
                            message="El pacienta ha sido eliminado correctamente.",
                            option_1="Cerrar",
                            icon="info",
                            option_2="Cerrar")
                    else:
                        print("0")
                else:
                    CTkMessagebox(title="Eliminación | Error",
                    message="Este paciente no existe!",
                    option_1="Cerrar", 
                    icon="cancel",
                    fade_in_duration=35)
                        
            else:
                CTkMessagebox(title="Eliminación | Error",
                message="La cédula no puede contener números!",
                option_1="Cerrar", 
                icon="cancel",
                fade_in_duration=35)
                
        else:
            CTkMessagebox(title="Eliminación | Error",
                          message="La cédula es necesaria para eliminar",
                          option_1="Cerrar", 
                          icon="cancel",
                          fade_in_duration=35)
            
    def limpiar_datos(self):
        self.entry_genero_paciente.delete(0, ctk.END)
        self.entry_cedula_paciente.delete(0, ctk.END)
        self.entry_nombres_paciente.delete(0, ctk.END)
        self.entry_apellidos_paciente.delete(0, ctk.END)
        self.entry_dir_paciente.delete(0, ctk.END)
        self.entry_edad_paciente.delete(0, ctk.END)
        self.entry_fecha_nacimiento_paciente.delete(0, ctk.END)
        self.entry_telefono_paciente.delete(0, ctk.END)
        
        
        