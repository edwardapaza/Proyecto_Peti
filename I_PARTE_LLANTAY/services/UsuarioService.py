from venv import logger
from database.Modulo_base import BaseDatos
from models.usuario import Usuario



class UserService:
    @classmethod
    def login_user(cls, username, password):
        try:
            query = "SELECT * FROM Usuarios WHERE username = %s AND contrasena = %s"
            resultados = BaseDatos.getDatos_condicion(query, (username, password))

            if resultados:
                usuario = resultados[0]
                authenticated_user = Usuario(*usuario)
                return authenticated_user
            else:
                return None
        except Exception as ex:
            logger.error(str(ex))
            return None

    @classmethod
    def add_user(cls, username, password):
        try:

            query = "INSERT INTO Usuarios (username, contrasena) VALUES (%s, %s)"
            BaseDatos.setDatos(query, (username, password))
            
            query = "SELECT LAST_INSERT_ID()"
            new_user_id = BaseDatos.getDatos(query)[0][0]

            return Usuario(new_user_id, username, password)
        except Exception as ex:
            logger.error(str(ex))
            return None

    @classmethod
    def get_all_users(cls):
        try:
            query = "SELECT * FROM Usuarios"
            resultados = BaseDatos.getDatos(query)

            all_users = [Usuario(*usuario) for usuario in resultados]  
            return all_users
        except Exception as ex:
            logger.error(str(ex))
            return []
