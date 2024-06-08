import logging
from flask import Blueprint, redirect, render_template, request, jsonify, url_for
import traceback
from services.MIsionService import MisionService
from services.VisionService import VisionService
from services.ValoresService import ValoresService
from services.ObjectivoService import ObjetivoService
from services.AnalisisService import AnalisisService

mision = Blueprint('mision', __name__)

@mision.route('/<int:empresa_id>', methods=['GET'])
def show_mision_id_empresa(empresa_id):
    try:
        mision = MisionService.get_mision_by_empresa_id(empresa_id)
        vision = VisionService.get_vision_by_empresa_id(empresa_id)
        valor = ValoresService.get_valores_by_empresa_id(empresa_id)
        objetivos_generales = ObjetivoService.listar_objetivos_generales(empresa_id)
        analisis_data = AnalisisService.get_analisisinternoexterno_by_empresa_id(empresa_id)

        print("ANalisis ", analisis_data)

        for objetivo_general in objetivos_generales:
            objetivo_general.objetivos_especificos = ObjetivoService.listar_objetivos_especificos(objetivo_general.objetivo_general_id)


        return render_template('plan.html', mision=mision,
                                            vision=vision,
                                            valores=valor,
                                            objetivos_generales = objetivos_generales,
                                            analisis_data = analisis_data
                                            )
    except Exception as ex:
        logging.error(f"Error al mostrar formulario de mision: {ex}")
        traceback.print_exc()
        return "Error al mostrar formulario de empresa", 500


@mision.route('/guardar', methods=['POST'])
def save_mision():
    try:
        empresa_id = request.form['empresa_id']
        mision_text = request.form['mision']
        nombre_empresa = request.form['nombre_empresa']

        print("empresa ", empresa_id)
        print('mision ', mision_text)
        print('nombre_empresa' , nombre_empresa)

        
        success = MisionService.save_mision(empresa_id, mision_text, nombre_empresa)
        if success:
            return redirect(url_for('mision.show_mision_id_empresa', empresa_id=empresa_id))
        else:
            return "Error al guardar la misión", 500
    except Exception as ex:
        logging.error(f"Error al guardar la misión: {ex}")
        traceback.print_exc()
        return "Error al guardar la misión", 500