from venv import logger
from database.Modulo_base import BaseDatos
from models.objectivos_generales import ObjetivoGeneral
from models.objetivos_especifico import ObjetivosEspecificos

class ObjetivoService:


    @classmethod
    def listar_objetivos_generales(cls, empresa_id):
        try:
            query = "SELECT * FROM ObjetivosGenerales WHERE empresa_id = %s"
            resultados = BaseDatos.getDatos_condicion(query, (empresa_id,))
            objetivos_generales = [ObjetivoGeneral(*resultado) for resultado in resultados]
            for objetivo_general in objetivos_generales:
                objetivo_general.objetivos_especificos = cls.listar_objetivos_especificos(objetivo_general.objetivo_general_id)
            return objetivos_generales
        except Exception as ex:
            logger.error(str(ex))
            return []

    @classmethod
    def listar_objetivos_especificos(cls, objetivo_general_id):
        try:
            query = "SELECT * FROM ObjetivosEspecificos WHERE objetivo_general_id = %s"
            resultados = BaseDatos.getDatos_condicion(query, (objetivo_general_id,))
            objetivos_especificos = [ObjetivosEspecificos(*resultado) for resultado in resultados]
            return objetivos_especificos
        except Exception as ex:
            logger.error(str(ex))
            return []

    @classmethod
    def actualizar_objetivo_general_servicio(cls, empresa_id, objetivo_id, descripcion):
        try:
            query = "UPDATE ObjetivosGenerales SET descripcion = %s WHERE objetivo_general_id = %s AND empresa_id = %s"
            parametros = (descripcion, objetivo_id, empresa_id)
            BaseDatos.updateDatos(query, parametros)
        except Exception as ex:
            logger.error(f"Error al actualizar objetivo general en la base de datos: {ex}")
            raise

    @classmethod
    def eliminar_objetivo_general_servicio(cls, empresa_id, objetivo_id):
        try:
            query = "DELETE FROM ObjetivosGenerales WHERE objetivo_general_id = %s AND empresa_id = %s"
            parametros = (objetivo_id, empresa_id)
            
            BaseDatos.deleteDatos(query, parametros)
        except Exception as ex:
            logger.error(f"Error al eliminar objetivo general en la base de datos: {ex}")
            raise


    @classmethod
    def guardar_objetivo_general_servicio(cls, empresa_id, descripcion):
        try:
            query = "INSERT INTO ObjetivosGenerales (empresa_id, descripcion) VALUES (%s, %s)"
            parametros = (empresa_id, descripcion)
            BaseDatos.setDatos(query, parametros)
        except Exception as ex:
            logger.error(f"Error al guardar objetivo general en la base de datos: {ex}")
            raise


    @classmethod
    def agregar_objetivo_especifico_servicio(cls, objetivo_general_id, descripcion):
        try:
            query = "INSERT INTO ObjetivosEspecificos (objetivo_general_id, descripcion) VALUES (%s, %s)"
            parametros = (objetivo_general_id, descripcion)
            BaseDatos.setDatos(query, parametros)
        except Exception as ex:
            logger.error(f"Error al agregar objetivo específico en la base de datos: {ex}")
            raise

    @classmethod
    def eliminar_objetivo_especifico_servicio(cls, objetivo_especifico_id):
        try:
            query = "DELETE FROM ObjetivosEspecificos WHERE objetivo_especifico_id = %s"
            parametros = (objetivo_especifico_id,)
            BaseDatos.deleteDatos(query, parametros)
        except Exception as ex:
            logger.error(f"Error al eliminar objetivo específico en la base de datos: {ex}")
            raise

    @classmethod
    def actualizar_objetivo_especifico_servicio(cls, objetivo_especifico_id, descripcion):
        try:
            query = "UPDATE ObjetivosEspecificos SET descripcion = %s WHERE objetivo_especifico_id = %s"
            parametros = (descripcion, objetivo_especifico_id)
            BaseDatos.updateDatos(query, parametros)
        except Exception as ex:
            logger.error(f"Error al actualizar objetivo específico en la base de datos: {ex}")
            raise