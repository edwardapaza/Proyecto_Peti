import logging
from flask import Blueprint, render_template, request, jsonify
import traceback
from services.EmpresaService import EmpresaService

empresa = Blueprint('empresa', __name__)

@empresa.route('/', methods=['GET'])
def show_empresa_form():
    try:
        empresas = EmpresaService.get_all_empresas()
        return render_template('empresa.html', empresas=empresas)
    except Exception as ex:
        logging.error(f"Error al mostrar formulario de empresa: {ex}")
        traceback.print_exc()
        return "Error al mostrar formulario de empresa", 500
