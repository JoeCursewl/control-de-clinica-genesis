import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from controlador.controlador import Controlador


class Consultar_pacientes(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        ################################
        
        self.db = Controlador()
        
        ################################
        
        
    def consult_window_pacientes(self):
        self.app_consult = ctk.CTkToplevel(self)
        w, h = self.app_consult.winfo_screenwidth(), self.app_consult.winfo_screenheight()
        x, y = (w / 2) - 475, (h / 2) - 370
        self.app_consult.geometry(f"950x650+{int(x)}+{int(y)}")
        self.app_consult.grab_set()
        self.app_consult.title("Administración | Consultar pacientes")
        
        self.letra_label_divisor = ('Century Gothic', 16)
        self.letra_label = ('Century Gothic', 15)
        
        #############################
        
        frame_top = ctk.CTkFrame(self.app_consult, width=900, height=50)
        frame_top.place(x=475, y=10, anchor="n")
        
        label_divisor = ctk.CTkLabel(frame_top, text="Administración | Consultar Pacientes                                                                                                                                             ", font=self.letra_label_divisor)
        label_divisor.pack(padx=20, pady=10)
        
        ###############################
        
        label_buscar_historiales = ctk.CTkLabel(self.app_consult, text="Consultas | Consultar todos los Pacientes/Uno solo por cédula paciente", font=self.letra_label)
        label_buscar_historiales.place(x=218, y=115, anchor="w")
        
        self.entry_consulta = ctk.CTkEntry(self.app_consult, width=350)
        self.entry_consulta.place(x=385, y=155, anchor="center")
        
        button_ingreso_consulta = ctk.CTkButton(self.app_consult, text="Consultar", command=self.consultar_paciente, width=12)
        button_ingreso_consulta.place(x=605, y=155, anchor="center")
        
        button_ingreso_consulta_td = ctk.CTkButton(self.app_consult, text="Consultar todos", command=self.consultar_pacientes_todos, width=12)
        button_ingreso_consulta_td.place(x=700, y=155, anchor="center")
        
        self.textbox_consulta_historiales = ctk.CTkTextbox(self.app_consult, width=550, height=330, font=('Century Gothic', 14))
        self.textbox_consulta_historiales.place(x=485, y=400, anchor="center")
        
        
    def consultar_pacientes_todos(self):
        dato = self.db.consultar_pacientes_todos()
        self.textbox_consulta_historiales.delete("1.0", "end")
        if dato:
            for datos in dato:
                texto = f"Cédula: {datos[0]}\nNombres: {datos[1]}\nApellidos: {datos[2]}\nDirección: {datos[3]}\nFecha Nacimiento: {datos[4]}\nGenero: {datos[5]}\nTeléfono: {datos[6]}\nEdad: {datos[7]}\n\n"
                self.textbox_consulta_historiales.insert("1.0", texto)
        else:
            CTkMessagebox(title="Administración | Errro de Consulta",
                          message="Aún no existen pacientes registrados!",
                          option_1="Cerrar",
                          icon="info",
                          fade_in_duration=35)
            
    def consultar_paciente(self):
        cedula = self.entry_consulta.get()
        self.textbox_consulta_historiales.delete("1.0", "end")
        if cedula != '':
            if cedula.isdigit():
                if len(cedula) < 12:
                    dato = self.db.existencia_paciente_cedula(cedula=cedula)
                    if dato is not None:
                        text = f"Cédula: {dato[0]}\nNombres: {dato[1]}\nApellidos: {dato[2]}\nDirección: {dato[3]}\nFecha Nacimiento: {dato[4]}\nGenero: {dato[5]}\nTeléfono: {dato[6]}\nEdad: {dato[7]}\n\n"
                        self.textbox_consulta_historiales.insert("1.0", text)
                    else:
                        CTkMessagebox(title="Administración | Errro de Consulta",
                          message="Este paciente no existe!",
                          option_1="Cerrar",
                          icon="info",
                          fade_in_duration=35)
                        self.textbox_consulta_historiales.delete("1.0", "end")
                    
                else:
                    CTkMessagebox(title="Administración | Errro de Consulta",
                          message="Ingrese una cédula válida!",
                          option_1="Cerrar",
                          icon="info",
                          fade_in_duration=35)
            else:
                CTkMessagebox(title="Administración | Errro de Consulta",
                    message="La cédula no puede contener letras!",
                    option_1="Cerrar",
                    icon="info",
                    fade_in_duration=35)
                self.entry_consulta.delete(0, ctk.END)
                self.textbox_consulta_historiales.delete("1.0", ctk.END)
        else:
            self.textbox_consulta_historiales.delete("1.0", "end")
            CTkMessagebox(title="Administración | Errro de Consulta",
                message="La cédula es necesaría para hacer la consulta!",
                option_1="Cerrar",
                icon="info",
                fade_in_duration=35)
            