import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from controlador.controlador import Controlador
import datetime
from fpdf import FPDF
import os
from customtkinter import filedialog

class Constancia_medica(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        
        self.db = Controlador()
        
    def constancia_pacientes_window(self):
        self.app_constancia_medica = ctk.CTkToplevel(self)
        w, h = self.app_constancia_medica.winfo_screenwidth(), self.app_constancia_medica.winfo_screenheight()
        x, y = (w / 2) - 475, (h / 2) - 370
        self.app_constancia_medica.geometry(f"950x660+{int(x)}+{int(y)}")
        self.app_constancia_medica.grab_set()
        self.app_constancia_medica.title("Administración | Generar constancia Médica")
        self.app_constancia_medica.resizable(0,0)
        
        self.letra_label_divisor = ('Century Gothic', 16)
        self.letra_label = ('Century Gothic', 15)
        
        ###########################################
        
        frame_top = ctk.CTkFrame(self.app_constancia_medica, width=900, height=50)
        frame_top.place(x=475, y=10, anchor="n")
        
        label_divisor = ctk.CTkLabel(frame_top, text="Administración | Constancia médica                                                                                                                                        ", font=self.letra_label_divisor)
        label_divisor.pack(padx=20, pady=10)
        
        #####################################################
        
        label_fecha_constancia = ctk.CTkLabel(self.app_constancia_medica, text="Fecha", font=self.letra_label)
        label_fecha_constancia.place(x=100, y=150, anchor="w")
        
        self.entry_fecha_constancia = ctk.CTkEntry(self.app_constancia_medica, width=170)
        self.entry_fecha_constancia.place(x=100, y=190, anchor="w")
        
        #####################################################
        
        label_medico_constancia = ctk.CTkLabel(self.app_constancia_medica, text="Médico", font=self.letra_label)
        label_medico_constancia.place(x=100, y=230, anchor="w")
        
        self.entry_medico_constancia = ctk.CTkEntry(self.app_constancia_medica, width=170)
        self.entry_medico_constancia.place(x=100, y=270, anchor="w")
        
        #####################################################
        
        label_especialidad_constancia = ctk.CTkLabel(self.app_constancia_medica, text="Especialidad", font=self.letra_label)
        label_especialidad_constancia.place(x=100, y=310, anchor="w")
        
        self.entry_especialidad_constancia = ctk.CTkEntry(self.app_constancia_medica, width=170)
        self.entry_especialidad_constancia.place(x=100, y=350, anchor="w")
        
        #####################################################
        
        label_nombres_constancia = ctk.CTkLabel(self.app_constancia_medica, text="Nombres del Paciente", font=self.letra_label)
        label_nombres_constancia.place(x=300, y=230, anchor="w")
        
        self.entry_nombres_constancia = ctk.CTkEntry(self.app_constancia_medica, width=170)
        self.entry_nombres_constancia.place(x=300, y=270, anchor="w")
        
        #####################################################
        
        label_apellidos_constancia = ctk.CTkLabel(self.app_constancia_medica, text="Apellidos del Paciente", font=self.letra_label)
        label_apellidos_constancia.place(x=300, y=310, anchor="w")
        
        self.entry_apellidos_constancia = ctk.CTkEntry(self.app_constancia_medica, width=170)
        self.entry_apellidos_constancia.place(x=300, y=350, anchor="w")
        
        ##################################################
        
        label_cedula_constancia = ctk.CTkLabel(self.app_constancia_medica, text="Cédula", font=self.letra_label)
        label_cedula_constancia.place(x=300, y=150, anchor="w")
        
        self.entry_cedula_constancia = ctk.CTkEntry(self.app_constancia_medica, width=170)
        self.entry_cedula_constancia.place(x=300, y=190, anchor="w")
        
        #####################################################
        
        label_tratamiento_constancia = ctk.CTkLabel(self.app_constancia_medica, text="Tratamiento médico", font=self.letra_label)
        label_tratamiento_constancia.place(x=100, y=405, anchor="w")
        
        self.entry_tratamiento_constancia = ctk.CTkTextbox(self.app_constancia_medica, height=120, width=370)
        self.entry_tratamiento_constancia.place(x=100, y=495, anchor="w")
        
        #########################################################
        
        label_diagnostico_constancia = ctk.CTkLabel(self.app_constancia_medica, text="Diagnóstico", font=self.letra_label)
        label_diagnostico_constancia.place(x=500, y=150, anchor="w")
        
        self.entry_diagnostico_constancia = ctk.CTkTextbox(self.app_constancia_medica, height=120, width=370)
        self.entry_diagnostico_constancia.place(x=500, y=238, anchor="w")
        
        ######################################################
        
        label_reposo_constancia = ctk.CTkLabel(self.app_constancia_medica, text="Reposo médico", font=self.letra_label)
        label_reposo_constancia.place(x=500, y=328, anchor="w")
        
        self.entry_reposo_constancia = ctk.CTkTextbox(self.app_constancia_medica, height=120, width=370)
        self.entry_reposo_constancia.place(x=500, y=416, anchor="w")
        
        ######################################################
        
        label_ruta_constancia = ctk.CTkLabel(self.app_constancia_medica, text="Ruta", font=self.letra_label)
        label_ruta_constancia.place(x=500, y=500, anchor="w")
        
        self.entry_ruta_constancia = ctk.CTkEntry(self.app_constancia_medica, width=370)
        self.entry_ruta_constancia.place(x=500, y=538, anchor="w")
        
        ######################################################
        
        
        
        button_generar_recipe = ctk.CTkButton(self.app_constancia_medica,
                                                 text="Examinar", 
                                                 command=self.ruta_pd_save)
        button_generar_recipe.place(x=320, y=620, anchor="w")
        
        button_generar_recipe2 = ctk.CTkButton(self.app_constancia_medica,
                                                 text="Generar constancia médica", 
                                                 command=self.generar_constancia_medica)
        button_generar_recipe2.place(x=500, y=620, anchor="w")
        
        fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y")
        hora_actual = datetime.datetime.now().strftime("%I:%M%p")
        
        self.entry_fecha_constancia.insert(0, fecha_actual)
        
    def ruta_pd_save(self):
        self.nombre_pdf = filedialog.asksaveasfilename(initialdir=os.getcwd(), defaultextension=".pdf")
        self.entry_ruta_constancia.delete(0, ctk.END)
        self.entry_ruta_constancia.insert(0, self.nombre_pdf)

        
    def generar_constancia_medica(self):
        nombre_pdf_dir = self.entry_ruta_constancia.get()
        fecha = self.entry_fecha_constancia.get()
        nombres = self.entry_nombres_constancia.get()
        apellidos = self.entry_apellidos_constancia.get()
        medico = self.entry_medico_constancia.get()
        especialidad = self.entry_especialidad_constancia.get()
        cedula = self.entry_cedula_constancia.get()
        tratamiento = self.entry_tratamiento_constancia.get("1.0", "end-1c")
        diagnostico = self.entry_diagnostico_constancia.get("1.0", "end-1c")
        reposo_medico = self.entry_reposo_constancia.get("1.0", "end-1c")
        
        if cedula and nombres and apellidos and medico and cedula and especialidad and tratamiento and diagnostico and reposo_medico != '':
            if nombres.isdigit():
                CTkMessagebox(title="Constancias Médicas | Error",
                        message="Los datos no pueden llevar números!", 
                        icon="cancel",
                        option_1="Cerrar",
                        fade_in_duration=35)
                
            else:
                if especialidad.isdigit():
                    CTkMessagebox(title="Constancias Médicas | Error",
                          message="El campo de la Especialidad no puede contener números!", 
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35) 
                else:
                    if apellidos.isdigit():
                        CTkMessagebox(title="Constancias Médicas | Error",
                                      message="El apellido no puede contener números!",
                                      icon="cancel",
                                      fade_in_duration=35,
                                      option_1="Cerrar")
                    else:
                        if cedula.isdigit():
                            if  nombre_pdf_dir:
                                CTkMessagebox(title="Constancias Médicas | Generando /",
                                message="Generando constancia médicL...", 
                                icon="check",
                                option_1="Cerrar",
                                fade_in_duration=35) 
                                pdf = FPDF()
                                pdf.add_page()
                                pdf.image('./img/bg_pdf.jpeg', 10, 8, 33)
                                pdf.set_font("Arial", 'B', size=14)
                                pdf.cell(0, 25, "Constancia Médica", 0, 0, 'C')
                                pdf.ln(40)
                                
                                pdf.set_font("Arial", '', size=12)
                                pdf.cell(200, 10, fecha, 0, 1, align="L")
                                pdf.cell(200, 10, txt=f"Cédula: {cedula}", ln=3, align="L")
                                pdf.cell(200, 10, txt=f"Nombres: {nombres}", ln=4, align="L")
                                pdf.cell(200, 10, txt=f"Apellidos: {apellidos}", ln=5, align="L")
                                pdf.cell(200, 10, txt=f"Especialidad: {especialidad}", ln=6, align="L")
                                pdf.cell(200, 10, txt=f"Médico: {medico}", ln=7 ,align="L")
                                pdf.cell(200, 10, txt=f"Diagnóstico: {diagnostico}", ln=8 ,align="L")
                                pdf.cell(200, 10, txt=f"Tratamiento Médico: {tratamiento}", ln=9,align="L")
                                pdf.cell(200, 10, txt=f"Reposo Médico: {reposo_medico}", ln=10,align="L")
                                nombre_pdf = f"{nombre_pdf_dir}"
    
                                pdf.output(nombre_pdf)
    
                                os.startfile(nombre_pdf)
                            
                                self.app_constancia_medica.destroy()
                                
                            else:
                                CTkMessagebox(title="Constancias Médicas | Error",
                                message="La ruta de guardado es requerida!", 
                                icon="cancel",
                                option_1="Cerrar",
                                fade_in_duration=35)

                        else:
                            CTkMessagebox(title="Constancias Médicas | Error",
                            message="La cédula no puede contener letras!", 
                            icon="cancel",
                            option_1="Cerrar",
                            fade_in_duration=35) 
        else:
            CTkMessagebox(title="Constancias Médicas | Error",
                          message="Todos los campos son necesarios!", 
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)        
        
        
        
        