import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from controlador.controlador import Controlador
from fpdf import FPDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
import os



class Imprimir_historias(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        
    ###################################
    #                                 #
        self.db = Controlador()
    #                                 #
    ###################################
        
    def print_window(self):
        self.app_consult = ctk.CTkToplevel(self)
        w, h = self.app_consult.winfo_screenwidth(), self.app_consult.winfo_screenheight()
        x, y = (w / 2) - 475, (h / 2) - 370
        self.app_consult.geometry(f"950x650+{int(x)}+{int(y)}")
        self.app_consult.grab_set()
        self.app_consult.title("Administración | Imprimir historia clínica")
        
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
        
        self.botton_imprimir_todas = ctk.CTkButton(self.app_consult,
                                                   text="Imprimir todas",
                                                   command=self.generar_pdf)
        self.botton_imprimir_todas.place(x=385, y=610, anchor="center")
        
        self.botton_imprimir_todas = ctk.CTkButton(self.app_consult,
                                                   text="Imprimir por CI",
                                                   command=self.generar_pdf_histo_cedula)
        self.botton_imprimir_todas.place(x=585, y=610, anchor="center")
        
    def consultar_todas(self):
        dato = self.db.consultar_histo_todas()
        self.textbox_consulta_historiales.delete("1.0", ctk.END)
        if dato:
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
            
    def imprimir_todas_historias(self):
        dato = self.db.consultar_histo_todas()
        self.textbox_consulta_historiales.delete("1.0", ctk.END)
        if dato:
            for datos in dato:
                texto = f"ID-HistoriaClínica: {datos[0]}\nCédula del Paciente: {datos[1]}\nFecha: {datos[2]}\nPeso: {datos[3]}\nTensión: {datos[4]}\nTalla: {datos[5]}\nExamen físico: {datos[6]}\nSíntomas: {datos[7]}\nDiagnóstico: {datos[8]}\nTratamiento: {datos[9]}\nAntecedentes: {datos[10]}\nAntecedentes Fam: {datos[11]}\n\n"
                self.textbox_consulta_historiales.insert("1.0", texto)
                
                
        else:
            CTkMessagebox(title="Consultas | Error",
                          message="No hay ningúna Historia clínica registrada!",
                          option_1="Cerrar",
                          fade_in_duration=35)
            
    def generar_pdf(self):

        data = self.db.consultar_histo_todas()


        pdf = MyPDF()
        pdf.generate_pdf(data)
        pdf_path = 'report.pdf'
        pdf.output(pdf_path)
        os.startfile(pdf_path)
        
    def generar_pdf_histo_cedula(self):
        cedula = self.entry_consulta.get()
        if cedula != '':
            if cedula.isdigit():
                if len(cedula) < 12:
                    dato = self.db.consultar_histo_cedula(cedula=cedula)
                    if dato is not None:
                        pdf = MyPDF()
                        pdf.generate_pdf_cedula(dato)
                        path_pdf = f"historías_clínicas_{cedula}"
                        pdf.output(path_pdf)
                        os.startfile(path_pdf)
                        CTkMessagebox(title="Récipes | Generando /",
                                      message=f"Generando historías clínicas de {cedula}",
                                      icon="check",
                                      fade_in_duration=35,
                                      option_1="Cerrar")

                    else:
                        CTkMessagebox(title="Impresiones | Error",
                          message="Este paciente aún no tiene historías clínicas registradas!",
                          option_1="Cerrar",
                          icon="cancel",
                          fade_in_duration=35)
                            
                else:
                    CTkMessagebox(title="Impresiones | Error",
                        message="Ingrese una cédula válida!",
                        option_1="Cerrar",
                        icon="cancel",
                        fade_in_duration=35)
                
            else:
                CTkMessagebox(title="Impresiones | Error",
                    message="La cédula no puede contener números!",
                    option_1="Cerrar",
                    icon="cancel",
                    fade_in_duration=35)
                
        else:
            CTkMessagebox(title="Impresiones | Error",
                          message="Para imprimar las historias de un paciente se requiera la cédula!",
                          option_1="Cerrar",
                          icon="cancel",
                          fade_in_duration=35)



class MyPDF(FPDF):
    
    def __init__(self):
        super().__init__()
        self.WIDTH = 210
        self.HEIGHT = 297
    
    def header(self):
        # Add image to the left
        self.image("./img/bg_pdf.jpeg", 10, 8, 33)
        
        # Add title to center
        self.set_font('Arial', 'B', 16)
        self.cell(0, 25, "Historías clínicas", 0, 0, 'C')
        self.ln(20)
        
    def footer(self):
        # Posición vertical a 1.5 cm del final
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Número de página
        self.cell(0, 10, 'Página ' + str(self.page_no()), 0, 0, 'C')


    def generate_pdf(self, data):
        self.set_font('Arial', '', 12)
   
        for datos in data:
            self.add_page()
            text = f"ID-Histora: {datos[0]}"
            text2 = f"Cédula: {datos[1]}"
            text3 = f"Fecha: {datos[2]}"
            text4 = f"Peso: {datos[3]}"
            text5 = f"Tensión: {datos[4]}"
            text6 = f"Talla: {datos[5]}"
            text7 = f"Examen físico: {datos[6]}"
            text8 = f"Síntomas: {datos[7]}"
            text9 = f"Diagnóstico: {datos[8]}"
            text10 = f"Tratamiento: {datos[9]}"
            text11 = f"Antecedentes: {datos[10]}"
            text12 = f"Antecedentes Familiares: {datos[11]}"
            
            self.cell(0, 10, text, 0, 1, 'L')
            self.cell(0, 10, text2, 0, 1, 'L')
            self.cell(0, 10, text3, 0, 1, 'L')
            self.cell(0, 10, text4, 0, 1, 'L')
            self.cell(0, 10, text5, 0, 1, 'L')
            self.cell(0, 10, text6, 0, 1, 'L')
            self.cell(0, 10, text7, 0, 1, 'L')
            self.cell(0, 10, text8, 0, 1, 'L')
            self.cell(0, 10, text9, 0, 1, 'L')
            self.cell(0, 10, text10, 0, 1, 'L')
            self.cell(0, 10, text11, 0, 1, 'L')
            self.cell(0, 10, text12, 0, 1, 'L')
            self.ln()
            
    def generate_pdf_cedula(self, dato):
        self.set_font('Arial', '', 12)
   
        for datos in dato:
            self.add_page()
            text = f"ID-Histora: {datos[0]}"
            text2 = f"Cédula: {datos[1]}"
            text3 = f"Fecha: {datos[2]}"
            text4 = f"Peso: {datos[3]}"
            text5 = f"Tensión: {datos[4]}"
            text6 = f"Talla: {datos[5]}"
            text7 = f"Examen físico: {datos[6]}"
            text8 = f"Síntomas: {datos[7]}"
            text9 = f"Diagnóstico: {datos[8]}"
            text10 = f"Tratamiento: {datos[9]}"
            text11 = f"Antecedentes: {datos[10]}"
            text12 = f"Antecedentes Familiares: {datos[11]}"
            
            self.cell(0, 10, text, 0, 1, 'L')
            self.cell(0, 10, text2, 0, 1, 'L')
            self.cell(0, 10, text3, 0, 1, 'L')
            self.cell(0, 10, text4, 0, 1, 'L')
            self.cell(0, 10, text5, 0, 1, 'L')
            self.cell(0, 10, text6, 0, 1, 'L')
            self.cell(0, 10, text7, 0, 1, 'L')
            self.cell(0, 10, text8, 0, 1, 'L')
            self.cell(0, 10, text9, 0, 1, 'L')
            self.cell(0, 10, text10, 0, 1, 'L')
            self.cell(0, 10, text11, 0, 1, 'L')
            self.cell(0, 10, text12, 0, 1, 'L')
            self.ln()
            
            
















        
        






        
            