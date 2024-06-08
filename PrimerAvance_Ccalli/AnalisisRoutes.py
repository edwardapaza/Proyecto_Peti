import logging
from flask import Blueprint, render_template, request, jsonify
import traceback
from services.AnalisisService import AnalisisService

analisis = Blueprint('analisis', __name__)

@analisis.route('/', methods=['GET'])
def show_empresa_form():
    try:
        empresa_id = request.args.get('empresa_id')  
        analisis_data = AnalisisService.get_analisisinternoexterno_by_empresa_id(empresa_id)
        return render_template('plan.html', analisis=analisis_data)
    except Exception as ex:
        logging.error(f"Error al mostrar formulario de empresa: {ex}")
        traceback.print_exc()
        return "Error al mostrar formulario de empresa", 500

@analisis.route('/guardar_valores', methods=['POST'])
def guardar_valores():
    try:

        fortalezas = request.form.get('fortalezas')
        debilidades = request.form.get('debilidades')
        oportunidades = request.form.get('oportunidades')
        amenazas = request.form.get('amenazas')
        empresa_id = request.form.get('empresa_id')

        AnalisisService.insertar_analisis(empresa_id,"tipointernoexterno", fortalezas, debilidades, oportunidades, amenazas)

        valores_guardados = {
            'fortalezas': fortalezas,
            'debilidades': debilidades,
            'oportunidades': oportunidades,
            'amenazas': amenazas
        }
        return jsonify({'mensaje': 'Valores guardados correctamente', 'valores_guardados': valores_guardados})

    except Exception as ex:
        logging.error(f"Error al guardar los valores: {ex}")
        traceback.print_exc()
        return jsonify({'error': 'Error al guardar los valores'}), 500
