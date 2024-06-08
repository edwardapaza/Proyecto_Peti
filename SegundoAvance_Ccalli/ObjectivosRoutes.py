import logging
from flask import Blueprint, redirect, render_template, request, jsonify, url_for
import traceback
from services.ObjectivoService import ObjetivoService

objectivo = Blueprint('objectivo', __name__)

@objectivo.route('/<int:empresa_id>', methods=['GET'])
def show_objectivo_id_empresa(empresa_id):
    try:

        objetivos_generales = ObjetivoService.listar_objetivos_generales(empresa_id)
        
        primer_objetivo_general_id = objetivos_generales[0].objetivo_general_id
        objetivos_especificos = ObjetivoService.listar_objetivos_especificos(primer_objetivo_general_id)

        return render_template('plan.html', objetivos_generales=objetivos_generales, objetivos_especificos=objetivos_especificos)
    except Exception as ex:
        logging.error(f"Error al mostrar formulario de valores: {ex}")
        traceback.print_exc()
        return "Error al mostrar formulario de empresa", 500
    

@objectivo.route('/actualizar_objectivo_general', methods=['POST'])
def actualizar_objetivo_general():
    try:

        empresa_id = request.form.get('empresa_id')
        objetivo_id = request.form.get('objetivo_id')
        descripcion = request.form.get('descripcion')

        ObjetivoService.actualizar_objetivo_general_servicio(empresa_id, objetivo_id, descripcion)

        return jsonify({'message': 'Objetivo general actualizado exitosamente'}), 200
    except Exception as ex:
        logging.error(f"Error al actualizar objetivo general: {ex}")
        traceback.print_exc()
        return jsonify({'error': 'Error al actualizar objetivo general'}), 500


@objectivo.route('/eliminar_objetivo_general', methods=['POST'])
def eliminar_objetivo_general():
    try:
        empresa_id = request.form.get('empresa_id')
        objetivo_id = request.form.get('objetivo_id')

        ObjetivoService.eliminar_objetivo_general_servicio(empresa_id, objetivo_id)
        return jsonify({'message': 'Objetivo general eliminado exitosamente'}), 200
    except Exception as ex:
        logging.error(f"Error al eliminar objetivo general: {ex}")
        traceback.print_exc()
        return jsonify({'error': 'Error al eliminar objetivo general'}), 500
    

@objectivo.route('/guardar_objetivo_general', methods=['POST'])
def guardar_objetivo_general():
    try:
        empresa_id = request.form.get('empresa_id')
        descripcion = request.form.get('descripcion')

        ObjetivoService.guardar_objetivo_general_servicio(empresa_id, descripcion)

        return jsonify({'message': 'Objetivo general guardado exitosamente'}), 200
    except Exception as ex:
        logging.error(f"Error al guardar objetivo general: {ex}")
        traceback.print_exc()
        return jsonify({'error': 'Error al guardar objetivo general'}), 500
    


@objectivo.route('/agregar_objetivo_especifico', methods=['POST'])
def guardar_objetivo_especificos():
    try:

        objetivo_general_id = request.form.get('objetivo_general_id')
        descripcion = request.form.get('descripcion')

        ObjetivoService.agregar_objetivo_especifico_servicio(objetivo_general_id, descripcion)
        return jsonify({'status': 'success', 'message': 'Objetivo especifico guardado exitosamente'}), 200
    except Exception as ex:
        logging.error(f"Error al guardar objetivo especifico: {ex}")
        traceback.print_exc()
        return jsonify({'status': 'error', 'error': 'Error al guardar objetivo especifico'}), 500
    

@objectivo.route('/actualizar_objetivo_especifico', methods=['POST'])
def actualizar_objetivo_especifico():
    try:
        objetivo_especifico_id = request.form.get('objetivo_especifico_id')
        descripcion = request.form.get('descripcion')
        ObjetivoService.actualizar_objetivo_especifico_servicio(objetivo_especifico_id, descripcion)
        return jsonify({'status': 'success', 'message': 'Objetivo especifico actualizado exitosamente'}), 200
    except Exception as ex:
        logging.error(f"Error al actualizar objetivo especifico: {ex}")
        traceback.print_exc()
        return jsonify({'status': 'error', 'error': 'Error al actualizar objetivo especifico'}), 500

    

@objectivo.route('/eliminar_objetivo_especifico', methods=['POST'])
def eliminar_objetivo_especifico():
    try:
        objetivo_especifico_id = request.form.get('objetivo_especifico_id')
        ObjetivoService.eliminar_objetivo_especifico_servicio(objetivo_especifico_id)
        return jsonify({'message': 'Objetivo especifico eliminado exitosamente'}), 200
    except Exception as ex:
        logging.error(f"Error al eliminar objetivo especifico: {ex}")
        traceback.print_exc()
        return jsonify({'error': 'Error al eliminar objetivo especifico'}), 500