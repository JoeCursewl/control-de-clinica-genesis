import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from controlador.controlador import Controlador


class Consultar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        
    ###################################
    #                                 #
        self.db = Controlador()
    #                                 #
    ###################################
        
    def consult_window(self):
        self.app_consult = ctk.CTkToplevel(self)
        w, h = self.app_consult.winfo_screenwidth(), self.app_consult.winfo_screenheight()
        x, y = (w / 2) - 475, (h / 2) - 370
        self.app_consult.geometry(f"950x650+{int(x)}+{int(y)}")
        self.app_consult.grab_set()
        self.app_consult.title("Administración | Consultar historia clínica")
        
        self.letra_label_divisor = ('Century Gothic', 16)
        self.letra_label = ('Century Gothic', 15)
        
        #############################
        
        frame_top = ctk.CTkFrame(self.app_consult, width=900, height=50)
        frame_top.place(x=475, y=10, anchor="n")
        
        label_divisor = ctk.CTkLabel(frame_top, text="Administración | Consultar historia clínica                                                                                                                                             ", font=self.letra_label_divisor)
        label_divisor.pack(padx=20, pady=10)
        
        ###############################
        
        label_buscar_historiales = ctk.CTkLabel(self.app_consult, text="Consultas | Consultar todos los Historiales/Uno solo por cédula paciente", font=self.letra_label)
        label_buscar_historiales.place(x=218, y=115, anchor="w")
        
        self.entry_consulta = ctk.CTkEntry(self.app_consult, width=350)
        self.entry_consulta.place(x=385, y=155, anchor="center")
        
        button_ingreso_consulta = ctk.CTkButton(self.app_consult, text="Consultar", command=self.consultar_histo_cedula, width=12)
        button_ingreso_consulta.place(x=605, y=155, anchor="center")
        
        button_ingreso_consulta_td = ctk.CTkButton(self.app_consult, text="Consultar todos", command=self.consultar_todas, width=12)
        button_ingreso_consulta_td.place(x=700, y=155, anchor="center")
        
        self.textbox_consulta_historiales = ctk.CTkTextbox(self.app_consult, width=550, height=330, font=('Century Gothic', 14))
        self.textbox_consulta_historiales.place(x=485, y=400, anchor="center")
        
    def consultar_todas(self):
        dato = self.db.consultar_histo_todas()
        self.textbox_consulta_historiales.delete("1.0", ctk.END)
        if dato is not None:
            for datos in dato:
                texto = f"ID-HistoriaClínica: {datos[0]}\nCédula del Paciente: {datos[1]}\nFecha: {datos[2]}\nPeso: {datos[3]}\nTensión: {datos[4]}\nTalla: {datos[5]}\nExamen físico: {datos[6]}\nSíntomas: {datos[7]}\nDiagnóstico: {datos[8]}\nTratamiento: {datos[9]}\nAntecedentes: {datos[10]}\nAntecedentes Fam: {datos[11]}\n\n"
                self.textbox_consulta_historiales.insert("1.0", texto)
        else:
            CTkMessagebox(title="Consultas | Error",
                          message="No hay ningúna Historia clínica registrada!",
                          option_1="Cerrar",
                          fade_in_duration=35)
            
    def consultar_histo_cedula(self):
        cedula = self.entry_consulta.get()
        self.textbox_consulta_historiales.delete("1.0", "end")
        if cedula != '':
            if cedula.isdigit():
                dato = self.db.consultar_histo_cedula(cedula=cedula)
                if dato:
                    for datos in dato:
                        texto = f"ID-HistoriaClínica: {datos[0]}\nCédula del Paciente: {datos[1]}\nFecha: {datos[2]}\nPeso: {datos[3]}\nTensión: {datos[4]}\nTalla: {datos[5]}\nExamen físico: {datos[6]}\nSíntomas: {datos[7]}\nDiagnóstico: {datos[8]}\nTratamiento: {datos[9]}\nAntecedentes: {datos[10]}\nAntecedentes Fam: {datos[11]}\n\n"
                        self.textbox_consulta_historiales.insert("1.0", texto)
                else:
                    CTkMessagebox(title="Consultas | Error",
                    message="Este paciente no tiene historías clínicas!",
                    option_1="Cerrar",
                    icon="cancel",
                    fade_in_duration=35)
                    self.entry_consulta.delete(0, ctk.END)
                    
            else:
                CTkMessagebox(title="Consultas | Error",
                    message="La cédula no puede contener números!",
                    option_1="Cerrar",
                    icon="cancel",
                    fade_in_duration=35)
                self.entry_consulta.delete(0, ctk.END)
        else:
            CTkMessagebox(title="Consultas | Error",
                          message="La cédula es requerida para consultar las historias clínicas!",
                          option_1="Cerrar",
                          icon="cancel",
                          fade_in_duration=35)
            