import logging
from flask import Blueprint, redirect, render_template, request, jsonify, url_for
import traceback
from services.ValoresService import ValoresService

valor = Blueprint('valor', __name__)

@valor.route('/<int:empresa_id>', methods=['GET'])
def show_valor_id_empresa(empresa_id):
    try:
        valores = ValoresService.get_valores_by_empresa_id(empresa_id)
        return render_template('plan.html', valores=valores)
    except Exception as ex:
        logging.error(f"Error al mostrar formulario de valores: {ex}")
        traceback.print_exc()
        return "Error al mostrar formulario de empresa", 500
    

@valor.route('/agregar', methods=['POST'])
def agregar_valor():
    try:
        empresa_id = request.form['empresa_id']
        valor = request.form['valor']
        success = ValoresService.agregar_valor(empresa_id, valor)
        if success:
            return jsonify({"status": "success"}), 200
        else:
            return jsonify({"status": "error"}), 500
    except Exception as ex:
        logging.error(f"Error al agregar el valor: {ex}")
        traceback.print_exc()
        return jsonify({"status": "error"}), 500
    

@valor.route('/eliminar', methods=['POST'])
def eliminar_valor():
    try:
        valor_id = request.form['valor_id']
        success = ValoresService.eliminar_valor(valor_id)
        if success:
            return jsonify({"status": "success"}), 200
        else:
            return jsonify({"status": "error"}), 500
    except Exception as ex:
        logging.error(f"Error al eliminar el valor: {ex}")
        traceback.print_exc()
        return jsonify({"status": "error"}), 500
    

@valor.route('/actualizar', methods=['POST'])
def actualizar_valor():
    try:
        valor_id = request.form['valor_id']
        valor = request.form['valor']
        success = ValoresService.actualizar_valor(valor_id, valor)
        if success:
            return jsonify({"status": "success"}), 200
        else:
            return jsonify({"status": "error"}), 500
    except Exception as ex:
        logging.error(f"Error al actualizar el valor: {ex}")
        traceback.print_exc()
        return jsonify({"status": "error"}), 500
