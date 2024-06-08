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

    @classmethod
    def save_mision(cls, empresa_id, mision_text, nombre_empresa):
        try:
            existing_mision = cls.get_mision_by_empresa_id(empresa_id)
            if existing_mision:
                query = "UPDATE Mision SET mision = %s, nombre_empresa = %s WHERE empresa_id = %s"
                params = (mision_text, nombre_empresa, empresa_id)
            else:
                query = "INSERT INTO Mision (empresa_id, mision, nombre_empresa) VALUES (%s, %s, %s)"
                params = (empresa_id, mision_text, nombre_empresa)
            
            BaseDatos.setDatos(query, params)
            return True
        except Exception as ex:
            logger.error(str(ex))
            return False