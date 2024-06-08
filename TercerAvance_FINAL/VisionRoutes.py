import logging
from flask import Blueprint, redirect, render_template, request, jsonify, url_for
import traceback
from services.VisionService import VisionService

vision = Blueprint('vision', __name__)

@vision.route('/<int:empresa_id>', methods=['GET'])
def show_vision_id_empresa(empresa_id):
    try:
        vision = VisionService.get_vision_by_empresa_id(empresa_id)
        return render_template('plan.html', vision=vision)
    except Exception as ex:
        logging.error(f"Error al mostrar formulario de vision: {ex}")
        traceback.print_exc()
        return "Error al mostrar formulario de empresa", 500


@vision.route('/guardar', methods=['POST'])
def save_vision():
    try:
        empresa_id = request.form['empresa_id']
        vision_text = request.form['vision']


        print("empresa ", empresa_id)
        print('mision ', vision_text)

        success = VisionService.save_vision(empresa_id, vision_text)
        if success:
            return redirect(url_for('vision.show_vision_id_empresa', empresa_id=empresa_id))
        else:
            return "Error al guardar la vision", 500
    except Exception as ex:
        logging.error(f"Error al guardar la vision: {ex}")
        traceback.print_exc()
        return "Error al guardar la vision", 500