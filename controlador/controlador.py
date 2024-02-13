from modelo.modelo import Modelo

class Controlador():
    def __init__(self):
        
        self.controlador = Modelo()
        
        
    def validar_login_admin(self, usuario, password):
        dato = self.controlador.validar_login_admin(usuario=usuario, password=password)
        return dato
    
    def validar_login_medico(self, usuario, password):
        dato = self.controlador.validar_login_medico(usuario=usuario, password=password)
        return dato
    
    def validar_login_asistente(self, usuario, password):
        dato = self.controlador.validar_login_asistente(usuario=usuario, password=password)
        return dato
    
    def existencia_paciente_cedula(self, cedula):
        dato = self.controlador.existencia_paciente_cedula(cedula=cedula)
        return dato
    
    def registrar_historia_clinica(self, cedula, fecha, peso, tension, talla, exam_fisico, sintomas, diagnostico, tratamiento, antecedentes, ante_family):
        dato = self.controlador.registrar_historia_clinica(cedula, fecha, peso, tension, talla, exam_fisico, sintomas, diagnostico, tratamiento, antecedentes, ante_family)
        if dato == 1:
            return True
        else:
            return False
        
    def existencia_historia(self, id_numero_hist):
        dato = self.controlador.existencia_historia_id(cl_id_hist=id_numero_hist)
        return dato
    
    def actualizar_historia_clinica(self, id_historia, peso, tension, talla, exam_fisico, sintomas, diagnostico, tratamiento, antecedentes, ante_family):
        dato = self.controlador.actualizar_historia_clinica(id_historia, peso, tension, talla, exam_fisico, sintomas, diagnostico, tratamiento, antecedentes, ante_family)
        return dato
    
    def consultar_histo_todas(self):
        dato = self.controlador.consultar_historias_todas()
        return dato
    
    def consultar_histo_cedula(self, cedula):
        dato = self.controlador.consultar_historia_cedula(cedula=cedula)
        return dato
    
    def eliminar_historia_id(self, cl_id_hist):
        dato = self.controlador.eliminar_historia_clinica_id(cl_id_hist=cl_id_hist)
        if dato == 1:
            return True
        else:
            return False
        
    def registrar_pacientes(self, cedula, nombres, apellidos, direccion, fecha_nam, genero, telefono, edad):
        dato = self.controlador.registrar_paciente(cedula, nombres, apellidos, direccion, fecha_nam, genero, telefono, edad)
        if dato == 1:
            return True
        else:
            return False
        
    def actualizar_pacientes(self, cedula, nombres, apellidos, direccion, fecha_nam, genero, telefono, edad):
        dato = self.controlador.actualizar_paciente(cedula, nombres, apellidos, direccion, fecha_nam, genero, telefono, edad)
        if dato == 1:
            return True
        else:
            return False
        
    def eliminar_paciente(self, cedula):
        dato = self.controlador.eliminar_pacientes(cedula=cedula)
        if dato == 1:
            return True
        else:
            return False
        
    def eliminar_historias_todas(self, cedula):
        dato = self.controlador.eliminar_historias_todas_paciente(cedula=cedula)
        return dato
    
    def consultar_pacientes_todos(self):
        dato = self.controlador.consultar_pacientes_all()
        return dato
    
    def verificar_existencia_admin(self, usuario):
        dato = self.controlador.verificar_existencia_usuario_admin(usuario=usuario)
        return dato
    
    def insertar_usuario_admin(self, usuario, password, correo):
        dato = self.controlador.registrar_usuario_admin(usuario=usuario, password=password, correo=correo)
        if dato == 1:
            return True
        else:
            return False
        
    def verificar_existencia_medico(self, usuario):
        dato = self.controlador.verificar_existencia_usuario_medico(usuario=usuario)
        return dato
    
    def insertar_usuario_medico(self, usuario, password, correo):
        dato = self.controlador.registrar_usuario_medico(usuario=usuario, password=password, correo=correo)
        if dato == 1:
            return True
        else:
            return False
        
    def verificar_existencia_asistente(self, usuario):
        dato = self.controlador.verificar_existencia_usuario_asistente(usuario=usuario)
        return dato
    
    def insertat_usuario_asistente(self, usuario, password, correo):
        dato = self.controlador.registrar_usuario_asistente(usuario=usuario, password=password, correo=correo)
        if dato == 1:
            return True
        else:
            return False
        
    def consulta_admin(self, id_user):
        dato = self.controlador.consultar_usuario_admin(id_user=id_user)
        return dato
        
    def consulta_medico(self, id_user):
        dato = self.controlador.consultar_usuario_medico(id_user=id_user)
        return dato
    
    def consulta_asistente(self, id_user):
        dato = self.controlador.consultar_usuario_asistente(id_user=id_user)
        return dato
    
    def verificar_id_admin(self, id_user):
        dato = self.controlador.verificar_existencia_id_admin(id_user=id_user)
        return dato
    
    def verificar_medico(self, id_user):
        dato = self.controlador.verificar_existencia_id_medico(id_user=id_user)
        return dato
    
    def verificar_asistente(self, id_user):
        dato = self.controlador.verificar_existencia_id_asistente(id_user=id_user)
        return dato
    
    def actualizar_admins(self, id_user, usuario, password, correo):
        dato = self.controlador.actualizar_admins_id(id_user=id_user, usuario=usuario, password=password, correo=correo)
        if dato == 1:
            return True
        else:
            return False
    
    def actualizar_medicos(self, id_user, usuario, password, correo):
        dato = self.controlador.actualizar_medicos_id(id_user=id_user, usuario=usuario, password=password, correo=correo)
        if dato == 1:
            return True
        else:
            return False
        
    def actualizar_asistentes(self, id_user, usuario, password, correo):
        dato = self.controlador.actualizar_asistentes_id(id_user=id_user, usuario=usuario, password=password, correo=correo)
        if dato == 1:
            return True
        else:
            return False
        
    def consulta_admin_all(self):
        dato = self.controlador.consultar_usuarios_admins_todos()
        return dato
    
    def consulta_medico_all(self):
        dato = self.controlador.consultar_usuarios_medicos_todos()
        return dato
    
    def consultar_asistente_all(self):
        dato = self.controlador.consultar_usuarios_asistentes_todos()
        return dato
    
    def delete_admin(self, id_user):
        dato = self.controlador.eliminar_usuarios_admins(id_user=id_user)
        if dato == 1:
            return True
        else:
            return False
        
    def delete_medico(self, id_user):
        dato = self.controlador.eliminar_usuarios_medicos(id_user=id_user)
        if dato == 1:
            return True
        else:
            return False
        
    def delete_asistente(self, id_user):
        dato = self.controlador.eliminar_usuarios_asistentes(id_user=id_user)
        if dato == 1:
            return True
        else:
            return False    