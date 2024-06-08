from venv import logger
from database.Modulo_base import BaseDatos
from models.analisis_interno_externo import AnalisisInternoExterno

class AnalisisService:

    @classmethod
    def get_analisisinternoexterno_by_empresa_id(cls, empresa_id):
        try:
            query = "SELECT * FROM AnalisisInternoExterno WHERE empresa_id = %s"
            resultados = BaseDatos.getDatos_condicion(query, (empresa_id,))
            
            resultado = resultados[0] if resultados else None
            
            if resultado:
                analisis = AnalisisInternoExterno(
                    resultado[0],   # Índice del analisis_id
                    resultado[1],   # Índice del empresa_id
                    resultado[2],   # Índice del tipo
                    resultado[3],   # Índice del fortalezas
                    resultado[4],   # Índice del debilidades
                    resultado[5],   # Índice del oportunidades
                    resultado[6]    # Índice del amenazas
                )
            else:
                analisis = None

            return analisis
        except Exception as ex:
            logger.error(str(ex))
            return None


    @classmethod
    def insertar_analisis(cls, empresa_id, tipo, fortalezas, debilidades, oportunidades, amenazas):
        try:
            query = """
                INSERT INTO AnalisisInternoExterno 
                (empresa_id, tipo, fortalezas, debilidades, oportunidades, amenazas) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            valores = (empresa_id, tipo, fortalezas, debilidades, oportunidades, amenazas)
            BaseDatos.setDatos(query, valores)
            return True
        except Exception as ex:
            logger.error(f"Error al insertar el análisis: {ex}")
            return False
