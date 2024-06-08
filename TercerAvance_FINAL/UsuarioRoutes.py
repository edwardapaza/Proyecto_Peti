import logging
from flask import Blueprint, render_template, request, jsonify
import traceback
from services.UsuarioService import UserService

user = Blueprint('user', __name__)

@user.route('/', methods=['GET'])
def show_login_form():
    return render_template('login.html')

@user.route('/validar', methods=['POST'])
def login():
    try:
        username = request.form['username']
        password = request.form['password']
        
        authenticated_user = UserService.login_user(username, password)
        if authenticated_user:
            return jsonify({'success': True, 'message': 'Login successful', 'username': authenticated_user.username})
        else:
            return jsonify({'success': False, 'error': 'Usuario o Contraseña incorrecto'})
    except Exception as ex:
        logging.error(str(ex))
        logging.error(traceback.format_exc())
        return jsonify({'success': False, 'error': 'An error occurred while processing your request'})
