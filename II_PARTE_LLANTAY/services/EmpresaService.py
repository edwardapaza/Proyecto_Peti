from venv import logger
from database.Modulo_base import BaseDatos
from models.empresas import Empresa


class EmpresaService:

    @classmethod
    def get_all_empresas(cls):
        try:
            query = "SELECT * FROM Empresas"
            resultados = BaseDatos.getDatos(query)
            all_users = [Empresa(*empresa) for empresa in resultados]  
            return all_users
        except Exception as ex:
            logger.error(str(ex))
            return []

