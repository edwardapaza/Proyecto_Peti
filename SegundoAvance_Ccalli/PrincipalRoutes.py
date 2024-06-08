import logging
from flask import Blueprint, render_template, request, jsonify
import traceback

from services.EmpresaService import EmpresaService

principal = Blueprint('principal', __name__)

# /principal
@principal.route('/', methods=['GET'])
def show_principal_form():
    try:
        empresas = EmpresaService.get_all_empresas()
        return render_template('index.html', empresas=empresas)
    except Exception as ex:
        logging.error(f"Error al mostrar formulario de index: {ex}")
        traceback.print_exc()
        return "Error al mostrar formulario de empresa", 500