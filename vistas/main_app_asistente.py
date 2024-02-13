import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from vistas.register import Register
from vistas.actualizar import Actualizar
from vistas.consultar import Consultar
from vistas.consultar_pacientes import Consultar_pacientes
from vistas.consultar_usuarios import Consultar_usuarios
from vistas.eliminar import Eliminar
from vistas.registrar_pacientes import Registrar_pacientes
from vistas.actualizar_pacientes import Actualizar_pacientes
from vistas.eliminar_paciente import Eliminar_pacientes
from vistas.recipe_clinica import Recipe
from vistas.constancia_medica import Constancia_medica
from vistas.registrar_usuarios import Registrar_usuarios
from vistas.actualizar_usuarios import Actualizar_usuarios
from vistas.eliminar_usuarios import Eliminar_usuarios
from vistas.imprimiar_historias import Imprimir_historias
from vistas.informe_medico import Informe_medico

class Main_app_asistente(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.letra_label_divisor = ('Century Gothic', 16)
        self.letra_label = ('Century Gothic', 15)
        
        ###########################################
        
        self.register_historial = Register(master)
        self.actualizar_historial = Actualizar(master)
        self.consultar_historial = Consultar(master)
        self.consultar_pacientes = Consultar_pacientes(master)
        self.consultar_usuarios = Consultar_usuarios(master)
        self.eliminar = Eliminar(master)
        self.registrar_pacientes = Registrar_pacientes(master)
        self.actualizar_pacientes = Actualizar_pacientes(master)
        self.eliminar_pacientes = Eliminar_pacientes(master)
        self.generar_recipes = Recipe(master)
        self.constancia_medica = Constancia_medica(master)
        self.registrar_usuarios = Registrar_usuarios(master)
        self.actualizar_usuarios = Actualizar_usuarios(master)
        self.eliminar_usuarios = Eliminar_usuarios(master)
        self.imprimir_historias_todas = Imprimir_historias(master)
        self.imprimir_informe_medico = Informe_medico(master)
        
        ###########################################
        
    def app_window_asistentes(self):
        self.app_view = ctk.CTkToplevel(self)
        self.app_view.title("Vista General | Asistentes")
        self.app_view.resizable(0,0)
        w, h = self.app_view.winfo_screenwidth(), self.app_view.winfo_screenheight()
        x, y = (w / 2) - 475, (h / 2) - 370
        self.app_view.geometry(f"950x650+{int(x)}+{int(y)}")
        self.app_view.protocol("WM_DELETE_WINDOW", self.ask_if_close)
        
        frame_top = ctk.CTkFrame(self.app_view, width=900, height=50)
        frame_top.place(x=475, y=10, anchor="n")
        
        label_divisor = ctk.CTkLabel(frame_top, text="Administración | Gestión General                                                                                                                                                       ", font=self.letra_label_divisor)
        label_divisor.pack(padx=20, pady=10)
        
        #######################################################################
        
        frame_crud_historias = ctk.CTkFrame(self.app_view, width=460, height=500)
        frame_crud_historias.pack(padx=5, pady=10, side="left")
        
        label_crud_historaias = ctk.CTkLabel(frame_crud_historias, text="Historias Clínicas | Administrar", font=self.letra_label)
        label_crud_historaias.pack(padx=(120,120), pady=(20,452))
        
        frame_divisor = ctk.CTkFrame(frame_crud_historias, width=350, height=5)
        frame_divisor.place(x=230, y=220, anchor="n")
        
        ###############################################
        
        button_registra_historia = ctk.CTkButton(frame_crud_historias, text="Registrar",command=self.open_window_register)
        button_registra_historia.place(x=80, y=80, anchor="w")
        
        button_actualizar_historia = ctk.CTkButton(frame_crud_historias, text="Actualizar", command=self.open_window_actualizar)
        button_actualizar_historia.place(x=260, y=80, anchor="w")
        
        button_consultar_historia = ctk.CTkButton(frame_crud_historias, text="Consultar", command=self.open_window_consultar)
        button_consultar_historia.place(x=80, y=120, anchor="w")
        
        button_eliminar_historia = ctk.CTkButton(frame_crud_historias, text="Eliminar", command=self.open_window_eliminar)
        button_eliminar_historia.place(x=260, y=120, anchor="w")
        
        ####################################################
        
        label_crud_pacientes = ctk.CTkLabel(frame_crud_historias, text="Pacientes | Administrar", font=self.letra_label)
        label_crud_pacientes.place(x=230, y=290, anchor="n")
        
        button_registra_paciente = ctk.CTkButton(frame_crud_historias, text="Registrar", command=self.open_window_register_pacientes)
        button_registra_paciente.place(x=80, y=360, anchor="w")
        
        button_actualizar_paciente = ctk.CTkButton(frame_crud_historias, text="Actualizar", command=self.open_window_actualizar_pacientes)
        button_actualizar_paciente.place(x=260, y=360, anchor="w")
        
        button_consultar_paciente = ctk.CTkButton(frame_crud_historias, text="Consultar", command=self.open_window_consultar_pacientes)
        button_consultar_paciente.place(x=80, y=400, anchor="w")
        
        button_eliminar_paciente = ctk.CTkButton(frame_crud_historias, text="Eliminar", command=self.open_window_eliminar_pacientes)
        button_eliminar_paciente.place(x=260, y=400, anchor="w")
        
        ###########################################################################
        
        frame_crud_pacientes = ctk.CTkFrame(self.app_view, width=460, height=500)
        frame_crud_pacientes.pack(padx=5, pady=10, side="right")
        
        label_crud_pacientes = ctk.CTkLabel(frame_crud_pacientes, text="Usuarios | Administrar", font=self.letra_label)
        label_crud_pacientes.pack(padx=(160,160), pady=(20,452))
        
        frame_divisor = ctk.CTkFrame(frame_crud_pacientes, width=350, height=5)
        frame_divisor.place(x=230, y=220, anchor="n")
        
        ###############################################
        
        button_registra_historia = ctk.CTkButton(frame_crud_pacientes, text="Registrar", command=self.open_window_register_usuarios)
        button_registra_historia.place(x=80, y=80, anchor="w")
        
        button_actualizar_historia = ctk.CTkButton(frame_crud_pacientes, text="Actualizar", command=self.open_window_actualizar_usuarios)
        button_actualizar_historia.place(x=260, y=80, anchor="w")
        
        button_consultar_historia = ctk.CTkButton(frame_crud_pacientes, text="Consultar", command=self.open_window_consultar_usuarios)
        button_consultar_historia.place(x=80, y=120, anchor="w")
        
        button_eliminar_historia = ctk.CTkButton(frame_crud_pacientes, text="Eliminar", command=self.open_window_eliminar_usuarios)
        button_eliminar_historia.place(x=260, y=120, anchor="w")
        
        ####################################################
        
        label_crud_pacientes = ctk.CTkLabel(frame_crud_pacientes, text="Impresiones | Administrar", font=self.letra_label)
        label_crud_pacientes.place(x=230, y=290, anchor="n")
        
        button_registra_paciente = ctk.CTkButton(frame_crud_pacientes, text="Récipe", command=self.open_window_recipes)
        button_registra_paciente.place(x=80, y=360, anchor="w")
        
        button_actualizar_paciente = ctk.CTkButton(frame_crud_pacientes, text="Informe médico", command=self.open_window_informe_medico)
        button_actualizar_paciente.place(x=260, y=360, anchor="w")
        
        button_consultar_paciente = ctk.CTkButton(frame_crud_pacientes, text="Constancia médica", command=self.open_window_constancia_medica)
        button_consultar_paciente.place(x=80, y=400, anchor="w")
        
        button_eliminar_paciente = ctk.CTkButton(frame_crud_pacientes, text="Historias", command=self.open_window_print_historias)
        button_eliminar_paciente.place(x=260, y=400, anchor="w")
        
    def open_window_register(self):
        self.register_historial.register_window()
        
    def open_window_actualizar(self):
            CTkMessagebox(title="Administración | Error",
            message="No tienes permisos para realizar está acción!",
            icon="cancel",
            fade_in_duration=35)
        
    def open_window_consultar(self):
        self.consultar_historial.consult_window()
        
    def open_window_consultar_pacientes(self):
        self.consultar_pacientes.consult_window_pacientes()
        
    def open_window_consultar_usuarios(self):
            CTkMessagebox(title="Administración | Error",
            message="No tienes permisos para realizar está acción!",
            icon="cancel",
            fade_in_duration=35)
        
    def open_window_eliminar(self):
        CTkMessagebox(title="Administración | Error",
            message="No tienes permisos para realizar está acción!",
            icon="cancel",
            fade_in_duration=35)
        
    def open_window_register_pacientes(self):
        self.registrar_pacientes.register_pacientes_window()
        
    def open_window_actualizar_pacientes(self):
            CTkMessagebox(title="Administración | Error",
            message="No tienes permisos para realizar está acción!",
            icon="cancel",
            fade_in_duration=35)
        
    def open_window_eliminar_pacientes(self):
        CTkMessagebox(title="Administración | Error",
        message="No tienes permisos para realizar está acción!",
        icon="cancel",
        fade_in_duration=35)
        
        
    def open_window_recipes(self):
        self.generar_recipes.recipe_pacientes_window()
        
    def open_window_constancia_medica(self):
        self.constancia_medica.constancia_pacientes_window()
        
    def open_window_register_usuarios(self):
            CTkMessagebox(title="Administración | Error",
            message="No tienes permisos para realizar está acción!",
            icon="cancel",
            fade_in_duration=35)
        
    def open_window_actualizar_usuarios(self):
            CTkMessagebox(title="Administración | Error",
            message="No tienes permisos para realizar está acción!",
            icon="cancel",
            fade_in_duration=35)
    
    def open_window_eliminar_usuarios(self):
        CTkMessagebox(title="Administración | Error",
                      message="No tienes permisos para realizar está acción!",
                      icon="cancel",
                      fade_in_duration=35)
    
    def open_window_print_historias(self):
        self.imprimir_historias_todas.print_window()
        
    def open_window_informe_medico(self):
        self.imprimir_informe_medico.informe_medico_pacientes_window()
        
    def ask_if_close(self):
        info = CTkMessagebox(title="Clínica Génesis | Cerrar",
                             message="¿Está seguro que desea cerrar está ventana?",
                             option_1="Si",
                             option_2="No",
                             icon="info",
                             fade_in_duration=35)
        if info.get() == "Si":
            self.close_wn()
        else:
            pass
    

    def close_wn(self):
        self.master.quit()
        self.master.destroy()