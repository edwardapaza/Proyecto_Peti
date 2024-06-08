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

    @classmethod
    def agregar_valor(cls, empresa_id, valor):
        try:
            query = "INSERT INTO Valores (empresa_id, valor) VALUES (%s, %s)"
            BaseDatos.setDatos(query, (empresa_id, valor))
            return True
        except Exception as ex:
            logger.error(str(ex))
            return False
        

    @classmethod
    def eliminar_valor(cls, valor_id):
        try:
            query = "DELETE FROM Valores WHERE valor_id = %s"
            BaseDatos.deleteDatos(query, (valor_id,))
            return True
        except Exception as ex:
            logger.error(str(ex))
            return False
        

    @classmethod
    def actualizar_valor(cls, valor_id, valor):
        try:
            query = "UPDATE Valores SET valor = %s WHERE valor_id = %s"
            BaseDatos.updateDatos(query, (valor, valor_id))
            return True
        except Exception as ex:
            logger.error(str(ex))
            return False

