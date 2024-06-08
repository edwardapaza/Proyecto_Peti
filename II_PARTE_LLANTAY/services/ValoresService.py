from venv import logger
from database.Modulo_base import BaseDatos
from models.valor import Valor

class ValoresService:

    @classmethod
    def get_valores_by_empresa_id(cls, empresa_id):
        try:
            query = "SELECT * FROM Valores WHERE empresa_id = %s"
            resultados = BaseDatos.getDatos_condicion(query, (empresa_id,))
            valores = [Valor(*valor) for valor in resultados]
            return valores
        except Exception as ex:
            logger.error(str(ex))
            return []

    # @classmethod
    # def save_vision(cls, empresa_id, vision_text):
    #     try:
    #         existing_vision = cls.get_vision_by_empresa_id(empresa_id)
    #         if existing_vision:
    #             query = "UPDATE Vision SET vision = %s WHERE empresa_id = %s"
    #             params = (vision_text, empresa_id)
    #         else:
    #             query = "INSERT INTO Vision (empresa_id, vision) VALUES (%s, %s)"
    #             params = (empresa_id, vision_text)
            
    #         BaseDatos.setDatos(query, params)
    #         return True
    #     except Exception as ex:
    #         logger.error(str(ex))
    #         return False