import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from controlador.controlador import Controlador
import datetime
from fpdf import FPDF
import os
from customtkinter import filedialog

class Recipe(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        
        self.db = Controlador()
        
    def recipe_pacientes_window(self):
        self.app_recipes = ctk.CTkToplevel(self)
        w, h = self.app_recipes.winfo_screenwidth(), self.app_recipes.winfo_screenheight()
        x, y = (w / 2) - 475, (h / 2) - 370
        self.app_recipes.geometry(f"950x660+{int(x)}+{int(y)}")
        self.app_recipes.grab_set()
        self.app_recipes.title("Administración | Generar Récipes")
        self.app_recipes.resizable(0,0)
        
        self.letra_label_divisor = ('Century Gothic', 16)
        self.letra_label = ('Century Gothic', 15)
        
        ###########################################
        
        frame_top = ctk.CTkFrame(self.app_recipes, width=900, height=50)
        frame_top.place(x=475, y=10, anchor="n")
        
        label_divisor = ctk.CTkLabel(frame_top, text="Administración | Generar Récipes                                                                                                                                        ", font=self.letra_label_divisor)
        label_divisor.pack(padx=20, pady=10)
        
        #####################################################
        
        label_fecha_recipe = ctk.CTkLabel(self.app_recipes, text="Fecha", font=self.letra_label)
        label_fecha_recipe.place(x=300, y=150, anchor="w")
        
        self.entry_fecha_recipe = ctk.CTkEntry(self.app_recipes, width=170)
        self.entry_fecha_recipe.place(x=300, y=190, anchor="w")
        
        #####################################################
        
        label_nombres_recipe = ctk.CTkLabel(self.app_recipes, text="Nombres del Paciente", font=self.letra_label)
        label_nombres_recipe.place(x=300, y=230, anchor="w")
        
        self.entry_nombres_recipe = ctk.CTkEntry(self.app_recipes, width=170)
        self.entry_nombres_recipe.place(x=300, y=270, anchor="w")
        
        #####################################################
        
        label_apellidos_recipe = ctk.CTkLabel(self.app_recipes, text="Apellidos del Paciente", font=self.letra_label)
        label_apellidos_recipe.place(x=300, y=310, anchor="w")
        
        self.entry_apellidos_recipe = ctk.CTkEntry(self.app_recipes, width=170)
        self.entry_apellidos_recipe.place(x=300, y=350, anchor="w")
        
        #####################################################
        
        label_cedula_recipe = ctk.CTkLabel(self.app_recipes, text="Cédula", font=self.letra_label)
        label_cedula_recipe.place(x=500, y=230, anchor="w")
        
        self.entry_cedula_recipe = ctk.CTkEntry(self.app_recipes, width=170)
        self.entry_cedula_recipe.place(x=500, y=270, anchor="w")
        
        #####################################################
        
        label_medico_nacimiento_recipe = ctk.CTkLabel(self.app_recipes, text="Médico", font=self.letra_label)
        label_medico_nacimiento_recipe.place(x=500, y=310, anchor="w")
        
        self.entry_medico_nacimiento_recipe = ctk.CTkEntry(self.app_recipes, width=170)
        self.entry_medico_nacimiento_recipe.place(x=500, y=350, anchor="w")
        
        ##################################################
        
        label_especialidad_recipe = ctk.CTkLabel(self.app_recipes, text="Especialidad", font=self.letra_label)
        label_especialidad_recipe.place(x=500, y=150, anchor="w")
        
        self.entry_especialidad_recipe = ctk.CTkEntry(self.app_recipes, width=170)
        self.entry_especialidad_recipe.place(x=500, y=190, anchor="w")
        
        #####################################################
        
        label_ruta_recipe = ctk.CTkLabel(self.app_recipes, text="Ruta", font=self.letra_label)
        label_ruta_recipe.place(x=300, y=390, anchor="w")
        
        self.entry_ruta_recipe = ctk.CTkEntry(self.app_recipes, width=370)
        self.entry_ruta_recipe.place(x=300, y=430, anchor="w")
        
        #########################################################
        
        button_generar_recipe = ctk.CTkButton(self.app_recipes,
                                                 text="Ruta de Guardado", 
                                                 command=self.ruta_pd_save)
        button_generar_recipe.place(x=320, y=480, anchor="w")
        
        button_generar_recipe2 = ctk.CTkButton(self.app_recipes,
                                                 text="Generar récipe", 
                                                 command=self.generar_recipe)
        button_generar_recipe2.place(x=500, y=480, anchor="w")
        
        fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y")
        hora_actual = datetime.datetime.now().strftime("%I:%M%p")
        
        self.entry_fecha_recipe.insert(0, fecha_actual)
        
    def ruta_pd_save(self):
        self.nombre_pdf = filedialog.asksaveasfilename(initialdir=os.getcwd(), defaultextension=".pdf")
        self.entry_ruta_recipe.delete(0, ctk.END)
        self.entry_ruta_recipe.insert(0, self.nombre_pdf)

        
    def generar_recipe(self):
        nombre_pdf_dir = self.entry_ruta_recipe.get()
        fecha = self.entry_fecha_recipe.get()
        nombres = self.entry_nombres_recipe.get()
        apellidos = self.entry_apellidos_recipe.get()
        medico = self.entry_medico_nacimiento_recipe.get()
        especialidad = self.entry_especialidad_recipe.get()
        cedula = self.entry_cedula_recipe.get()
        
        if cedula and nombres and apellidos and medico and cedula and especialidad != '':
            if nombres.isdigit():
                CTkMessagebox(title="Recipes | Error",
                        message="Los datos no pueden llevar números!", 
                        icon="cancel",
                        option_1="Cerrar",
                        fade_in_duration=35)
                
            else:
                if especialidad.isdigit():
                    CTkMessagebox(title="Recipes | Error",
                          message="El campo de la Especialidad no puede contener números!", 
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35) 
                else:
                    if apellidos.isdigit():
                        CTkMessagebox(title="Recipes | Error",
                                      message="El apellido no puede contener números!",
                                      icon="cancel",
                                      fade_in_duration=35,
                                      option_1="Cerrar")
                    else:
                        if cedula.isdigit():
                            if  nombre_pdf_dir:
                                CTkMessagebox(title="Recipes | Generando /",
                                message="Generando recipe...", 
                                icon="check",
                                option_1="Cerrar",
                                fade_in_duration=35) 
                                pdf = FPDF()
                                pdf.add_page()
                                
                                pdf.image('./img/bg_pdf.jpeg', 10, 8, 33)
                                
                                pdf.set_font('Arial', 'B', 16)
                                pdf.cell(0, 25, "Récipe Médico", 0, 0, 'C')
                                pdf.ln(40)
                                pdf.set_font("Arial", size=12)
                                pdf.cell(200, 10, fecha, 0, 1, align="L")
                                pdf.cell(200, 10, txt=f"Cédula: {cedula}",ln=1, align="L")
                                pdf.cell(200, 10, txt=f"Nombres: {nombres}",ln=2, align="L")
                                pdf.cell(200, 10, txt=f"Apellidos: {apellidos}",ln=3, align="L")
                                pdf.cell(200, 10, txt=f"Especialidad: {especialidad}",ln=4, align="L")
                                pdf.cell(200, 10, txt=f"Médico: {medico}",ln=5, align="L")
                                nombre_pdf = f"{nombre_pdf_dir}"
    
                                pdf.output(nombre_pdf)
    
                                os.startfile(nombre_pdf)
                            
                                self.app_recipes.destroy()
                                
                            else:
                                CTkMessagebox(title="Recipes | Error",
                                message="La ruta de guardado es requerida!", 
                                icon="cancel",
                                option_1="Cerrar",
                                fade_in_duration=35)

                        else:
                            CTkMessagebox(title="Recipes | Error",
                            message="La cédula no puede contener letras!", 
                            icon="cancel",
                            option_1="Cerrar",
                            fade_in_duration=35) 
        else:
            CTkMessagebox(title="Recipes | Error",
                          message="Todos los campos son necesarios!", 
                          icon="cancel",
                          option_1="Cerrar",
                          fade_in_duration=35)        
        
        
        
        