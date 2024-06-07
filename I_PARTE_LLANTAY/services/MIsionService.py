from venv import logger
from database.Modulo_base import BaseDatos
from models.mision import Mision

class MisionService:

    @classmethod
    def get_mision_by_empresa_id(cls, empresa_id):
        try:
            query = "SELECT * FROM Mision WHERE empresa_id = %s"
            resultados = BaseDatos.getDatos_condicion(query, (empresa_id,))
            misiones = [Mision(*mision) for mision in resultados]
            return misiones
        except Exception as ex:
            logger.error(str(ex))
            return []
