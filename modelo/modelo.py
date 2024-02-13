import mysql.connector 

class Modelo():
    def __init__(self):
        
        # conexión a la db

        self.con = mysql.connector.connect(host="address",
                                           database="database",
                                           user="root",
                                        password="")
        
    def registrar_medico(self, usuario, password, correo):
        conexion = self.con
        try:
            cl_cursor = self.con.cursor()
            sql = "INSERT INTO cl_users (cl_usuario, cl_password, cl_correo) VALUES (%s, %s, %s)"
            values = (usuario, password, correo)
            cl_cursor.execute(sql, values)
            conexion.commit()
            conexion.close()
            return True
            
        except mysql.connector.errors.Error as asd:
            print(f"Ha ocurrido un error al insertar el usuario: {asd}")
            return False
        
    def validar_login_admin(self, usuario, password):
        conexion = self.con
        try:
            cl_cursor = self.con.cursor()
            sql = f"SELECT * FROM cl_users WHERE cl_usuario = '{usuario}' AND cl_password = '{password}'"
            cl_cursor.execute(sql)
            
            resultado = cl_cursor.fetchone()
            if resultado is None:
                return resultado
            else:
                conexion.close()
                return resultado
        except mysql.connector.errors.Error as asd:
            print(f"Login inválido: {asd}")
            
    def validar_login_medico(self, usuario, password):
        conexion = self.con
        try:
            cl_cursor = self.con.cursor()
            sql = f"SELECT * FROM cl_users_medicos WHERE cl_usuario = '{usuario}' AND cl_password = '{password}'"
            cl_cursor.execute(sql)
            
            resultado = cl_cursor.fetchone()
            if resultado is None:
                return resultado
            else:
                conexion.close()
                return resultado
        except mysql.connector.errors.Error as asd:
            print(f"Login inválido: {asd}")
            
    def validar_login_asistente(self, usuario, password):
        conexion = self.con
        try:
            cl_cusor = conexion.cursor()
            sql = f"SELECT * FROM cl_users_asistentes WHERE cl_usuario = '{usuario}' AND cl_password = '{password}'"
            cl_cusor.execute(sql)
            
            resultado = cl_cusor.fetchone()
            return resultado
        except mysql.connector.errors.Error as cl:
            print(f"No se ha podio validar el login: {cl}")
            
    def registrar_historia_clinica(self, cedula, fecha, peso, tension, talla, exam_fisico, sintomas, diagnostico, tratamiento, antecedentes, ante_family):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = "INSERT INTO cl_historias (cl_cedula, cl_fecha, cl_peso, cl_tension, cl_talla, cl_exam_fisico, cl_sintomas, cl_diagnostico, cl_tratamiento, cl_antecedentes, cl_ante_family) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (cedula, fecha, peso, tension, talla, exam_fisico, sintomas, diagnostico, tratamiento, antecedentes, ante_family)
            cl_cursor.execute(sql, values)
            conexion.commit()
            
            result = cl_cursor.rowcount
            return result
        except mysql.connector.errors.Error as cl:
            print(f"Error al insertar historia clínica: {cl}")
            
    def existencia_paciente_cedula(self, cedula):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = f"SELECT * FROM cl_pacientes WHERE cl_cedula = {cedula}"
            cl_cursor.execute(sql)
            
            resultado = cl_cursor.fetchone()
            return resultado

        except mysql.connector.errors.Error as cl:
            print(f"Error en la base de datos al verificar existencia: {cl}")
            
    def existencia_historia_id(self, cl_id_hist):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = f"SELECT * FROM cl_historias WHERE cl_id_hist = {cl_id_hist}"
            cl_cursor.execute(sql)
            
            resultado = cl_cursor.fetchone()
            return resultado
        except mysql.connector.errors.Error as cl:
            print(f"Un error encontrado al verificar existencia historia: {cl}")
            
    def actualizar_historia_clinica(self, id_historia, peso, tension, talla, exam_fisico, sintomas, diagnostico, tratamiento, antecedentes, ante_family):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = f"UPDATE cl_historias SET cl_peso = '{peso}', cl_tension = {tension}, cl_talla = {talla}, cl_exam_fisico = '{exam_fisico}', cl_sintomas = '{sintomas}', cl_diagnostico = '{diagnostico}', cl_tratamiento = '{tratamiento}', cl_antecedentes = '{antecedentes}', cl_ante_family = '{ante_family}' WHERE cl_id_hist = {id_historia}"
            cl_cursor.execute(sql)
            conexion.commit()
            
            return cl_cursor.rowcount
        except mysql.connector.errors.Error as cl:
            print(f"Error al actualizar en la tabla historias: {cl}")
            
    def consultar_historias_todas(self):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = "SELECT * FROM cl_historias"
            cl_cursor.execute(sql)
            
            resultado = cl_cursor.fetchall()
            return resultado
        except mysql.connector.errors.Error as cl:
            print(f"Ha ocurrido un error al consultar: {cl}")
            
    def consultar_historia_cedula(self, cedula):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = f"SELECT * FROM cl_historias WHERE cl_cedula = {cedula}"
            cl_cursor.execute(sql)
            
            resultado = cl_cursor.fetchall()
            return resultado
        except mysql.connector.errors.Error as cl:
            print(f"Ha ocurrido un error en la consulta historias por cedula: {cl}")
            
    def eliminar_historia_clinica_id(self, cl_id_hist):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = f"DELETE FROM cl_historias WHERE cl_id_hist = {cl_id_hist}"
            cl_cursor.execute(sql)
            conexion.commit()
            
            return cl_cursor.rowcount
            
        except mysql.connector.errors.Error as cl:
            print(f"Ha ocurrido un error al eliminar: {cl}")
            
    def registrar_paciente(self, cedula, nombres, apellidos, direccion, fecha_nam, genero, telefono, edad):
        conexion = self.con
        try:
            cl_cusor = conexion.cursor()
            sql = "INSERT INTO cl_pacientes (cl_cedula, cl_nombres, cl_apellidos, cl_dir, cl_fecha_nac, cl_genero, cl_telefono, cl_edad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (cedula, nombres, apellidos, direccion, fecha_nam, genero, telefono, edad)
            cl_cusor.execute(sql, values)
            conexion.commit()
            
            return cl_cusor.rowcount
        except mysql.connector.errors.Error as cl:
            print(f"Ha ocurrido un error al insertar al paciente: {cl}")
            
    def actualizar_paciente(self, cedula, nombres, apellidos, direccion, fecha_nam, genero, telefono, edad):
        conexion = self.con
        try: 
            cl_cursor = conexion.cursor()
            sql = f"UPDATE cl_pacientes SET cl_nombres = '{nombres}', cl_apellidos = '{apellidos}', cl_dir = '{direccion}', cl_fecha_nac = '{fecha_nam}', cl_genero = '{genero}', cl_telefono = {telefono}, cl_edad = {edad} WHERE cl_cedula = {cedula}"
            cl_cursor.execute(sql)
            
            resultado = cl_cursor.rowcount
            conexion.commit()
            return resultado
        except mysql.connector.errors.Error as cl:
            print(f"Ha ocurrido un error al actualizar paciente: {cl}")
            
    def eliminar_pacientes(self, cedula):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = f"DELETE FROM cl_pacientes WHERE cl_cedula = {cedula}"
            cl_cursor.execute(sql)
            
            conexion.commit()
            
            datico = cl_cursor.rowcount
            return datico
        except mysql.connector.errors.Error as cl:
            print(f"No se pudo borrar el paciente con cédula: {cl}")
            
    def eliminar_historias_todas_paciente(self, cedula):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = f"DELETE * FROM cl_historias WHERE cl_cedula = {cedula}"
            cl_cursor.execute(sql)
            
            conexion.commit()
            
            return True
        except mysql.connector.errors.Error as cl:
            print(f"No se pudo borrar el paciente con cédula: {cl}")
            return False
        
    def consultar_pacientes_all(self):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = "SELECT * FROM cl_pacientes"
            cl_cursor.execute(sql)
            
            resultado = cl_cursor.fetchall()
            return resultado
        except mysql.connector.errors.Error as cl:
            print(f"Ha ocurrido un error al tratar de consultar todos los pacientes: {cl}")
            
    def verificar_existencia_usuario_admin(self, usuario):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = f"SELECT * FROM cl_users WHERE cl_usuario = '{usuario}'"
            cl_cursor.execute(sql)
            
            resultado = cl_cursor.fetchone()
            return resultado
        
        except mysql.connector.errors.Error as cl:
            print(f"Ha ocurrido un error al verificar existencia: {cl}")
            
    def registrar_usuario_admin(self, usuario, password, correo):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = "INSERT INTO cl_users (cl_usuario, cl_password, cl_correo) VALUES (%s, %s, %s)"
            values = (usuario, password, correo)
            cl_cursor.execute(sql, values)
            
            conexion.commit()
            
            resultado = cl_cursor.rowcount
            return resultado
        except mysql.connector.errors.Error as cl:
            print(f"Ha ocurrido un error al insertar: {cl}")
            
    def verificar_existencia_usuario_medico(self, usuario):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = f"SELECT * FROM cl_users_medicos WHERE cl_usuario = '{usuario}'"
            cl_cursor.execute(sql)
            
            resultado = cl_cursor.fetchone()
            return resultado
        
        except mysql.connector.errors.Error as cl:
            print(f"Ha ocurrido un error al verificar existencia: {cl}")
            
    def registrar_usuario_medico(self, usuario, password, correo):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = "INSERT INTO cl_users_medicos (cl_usuario, cl_password, cl_correo) VALUES (%s, %s, %s)"
            values = (usuario, password, correo)
            cl_cursor.execute(sql, values)
            
            conexion.commit()
            
            resultado = cl_cursor.rowcount
            return resultado
        except mysql.connector.errors.Error as cl:
            print(f"Ha ocurrido un error al insertar MEDICO: {cl}")
            
    
    def verificar_existencia_usuario_asistente(self, usuario):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = f"SELECT * FROM cl_users_asistentes WHERE cl_usuario = '{usuario}'"
            cl_cursor.execute(sql)
            
            resultado = cl_cursor.fetchone()
            return resultado
        
        except mysql.connector.errors.Error as cl:
            print(f"Ha ocurrido un error al verificar existencia ASISTENTE: {cl}")
            
    def registrar_usuario_asistente(self, usuario, password, correo):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = "INSERT INTO cl_users_asistentes (cl_usuario, cl_password, cl_correo) VALUES (%s, %s, %s)"
            values = (usuario, password, correo)
            cl_cursor.execute(sql, values)
            
            conexion.commit()
            
            resultado = cl_cursor.rowcount
            return resultado
        except mysql.connector.errors.Error as cl:
            print(f"Ha ocurrido un error al insertar ASISTENTE: {cl}")  
            
    def consultar_usuario_admin(self, id_user):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = f"SELECT * FROM cl_users WHERE id_user = {id_user}"
            cl_cursor.execute(sql)
            
            resultado = cl_cursor.fetchone()
            return resultado
            
        except mysql.connector.errors.Error as cl:
            print(f"Ha ocurrido un error en la consulta ADMIN: {cl}")
            
    def consultar_usuario_medico(self, id_user):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = f"SELECT * FROM cl_users_medicos WHERE id_user = {id_user}"
            cl_cursor.execute(sql)
            
            resultado = cl_cursor.fetchone()
            return resultado
            
        except mysql.connector.errors.Error as cl:
            print(f"Ha ocurrido un error en la consulta MEDICO: {cl}")  
    
    def consultar_usuario_asistente(self, id_user):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = f"SELECT * FROM cl_users_asistentes WHERE id_user = {id_user}"
            cl_cursor.execute(sql)
            
            resultado = cl_cursor.fetchone()
            return resultado
            
        except mysql.connector.errors.Error as cl:
            print(f"Ha ocurrido un error en la consulta ASISTENTE: {cl}")
            
    def verificar_existencia_id_admin(self, id_user):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = f"SELECT * FROM cl_users WHERE id_user = {id_user}"
            cl_cursor.execute(sql)
            
            resultado = cl_cursor.fetchone()
            return resultado
        except mysql.connector.errors.Error as cl:
            print(f"No se pudo consultar id admin: {cl}")
            
    def verificar_existencia_id_medico(self, id_user):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = f"SELECT * FROM cl_users_medicos WHERE id_user = {id_user}"
            cl_cursor.execute(sql)
            
            resultado = cl_cursor.fetchone()
            return resultado
        except mysql.connector.errors.Error as cl:
            print(f"No se pudo consultar id medico: {cl}")
            
    def verificar_existencia_id_asistente(self, id_user):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = f"SELECT * FROM cl_users_asistentes WHERE id_user = {id_user}"
            cl_cursor.execute(sql)
            
            resultado = cl_cursor.fetchone()
            return resultado
        except mysql.connector.errors.Error as cl:
            print(f"No se pudo consultar id asistente: {cl}")
            
    def actualizar_medicos_id(self, id_user, usuario, password, correo):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = f"UPDATE cl_users_medicos SET cl_usuario = '{usuario}', cl_password = '{password}', cl_correo = '{correo}' WHERE id_user = {id_user}"
            cl_cursor.execute(sql)
            
            conexion.commit()
            
            resultado = cl_cursor.rowcount
            return resultado
        except mysql.connector.errors.Error as cl:
            print(f"Ha ocurrido un error al actualziar medicos: {cl}")
            
    def actualizar_admins_id(self, id_user, usuario, password, correo):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = f"UPDATE cl_users SET cl_usuario = '{usuario}', cl_password = '{password}', cl_correo = '{correo}' WHERE id_user = {id_user}"
            cl_cursor.execute(sql)
            
            conexion.commit()
            
            resultado = cl_cursor.rowcount
            return resultado
        except mysql.connector.errors.Error as cl:
            print(f"Ha ocurrido un error al actualziar admins: {cl}")
            
    def actualizar_asistentes_id(self, id_user, usuario, password, correo):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = f"UPDATE cl_users_asistentes SET cl_usuario = '{usuario}', cl_password = '{password}', cl_correo = '{correo}' WHERE id_user = {id_user}"
            cl_cursor.execute(sql)
            
            conexion.commit()
            
            resultado = cl_cursor.rowcount
            return resultado
        except mysql.connector.errors.Error as cl:
            print(f"Ha ocurrido un error al actualziar asistentes: {cl}")
            
    def consultar_usuarios_admins_todos(self):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = "SELECT * FROM cl_users"
            cl_cursor.execute(sql)
            
            resultado = cl_cursor.fetchall()
            return resultado
        except mysql.connector.errors.Error as cl:
            print(f"Ha ocurrido un error al consultar todos los usuarios admins!: {cl}")
            
    def consultar_usuarios_medicos_todos(self):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = "SELECT * FROM cl_users_medicos"
            cl_cursor.execute(sql)
            
            resultado = cl_cursor.fetchall()
            return resultado
        except mysql.connector.errors.Error as cl:
            print(f"Ha ocurrido un error al consultar todos los usuarios medicos: {cl}")
            
    def consultar_usuarios_asistentes_todos(self):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = "SELECT * FROM cl_users_asistentes"
            cl_cursor.execute(sql)
            
            resultado = cl_cursor.fetchall()
            return resultado
        except mysql.connector.errors.Error as cl:
            print(f"Ha ocurrido un error al consultar todos los usuarios asistentes: {cl}")
            
    def eliminar_usuarios_admins(self, id_user):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = f"DELETE FROM cl_users WHERE id_user = {id_user}"
            cl_cursor.execute(sql)
            
            conexion.commit()
            
            resultado = cl_cursor.rowcount
            return resultado
            
        except mysql.connector.errors.Error as cl:
            print(f"Ha ocurrido un error al eliminar admins: {cl}")
            
    def eliminar_usuarios_medicos(self, id_user):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = f"DELETE FROM cl_users_medicos WHERE id_user = {id_user}"
            cl_cursor.execute(sql)
            
            conexion.commit()
            
            resultado = cl_cursor.rowcount
            return resultado
            
        except mysql.connector.errors.Error as cl:
            print(f"Ha ocurrido un error al eliminar medicos: {cl}")
            
            
    def eliminar_usuarios_asistentes(self, id_user):
        conexion = self.con
        try:
            cl_cursor = conexion.cursor()
            sql = f"DELETE FROM cl_users_asistentes WHERE id_user = {id_user}"
            cl_cursor.execute(sql)
            
            conexion.commit()
            
            resultado = cl_cursor.rowcount
            return resultado
            
        except mysql.connector.errors.Error as cl:
            print(f"Ha ocurrido un error al eliminar asistentes: {cl}")
    
        