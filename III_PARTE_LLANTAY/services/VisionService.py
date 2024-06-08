from venv import logger
from database.Modulo_base import BaseDatos
from models.vision import Vision

class VisionService:

    @classmethod
    def get_vision_by_empresa_id(cls, empresa_id):
        try:
            query = "SELECT * FROM Vision WHERE empresa_id = %s"
            resultados = BaseDatos.getDatos_condicion(query, (empresa_id,))
            visiones = [Vision(*vision) for vision in resultados]
            return visiones
        except Exception as ex:
            logger.error(str(ex))
            return []

    @classmethod
    def save_vision(cls, empresa_id, vision_text):
        try:
            existing_vision = cls.get_vision_by_empresa_id(empresa_id)
            if existing_vision:
                query = "UPDATE Vision SET vision = %s WHERE empresa_id = %s"
                params = (vision_text, empresa_id)
            else:
                query = "INSERT INTO Vision (empresa_id, vision) VALUES (%s, %s)"
                params = (empresa_id, vision_text)
            
            BaseDatos.setDatos(query, params)
            return True
        except Exception as ex:
            logger.error(str(ex))
            return False