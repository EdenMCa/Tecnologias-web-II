from flask import Blueprint, request, jsonify
from app.service.RolService import RolService

roles_bp = Blueprint('roles', __name__)

@roles_bp.route('/', methods=['GET'])
def obtener_roles():
    roles = RolService.obtener_roles()
    # si roles son objetos ORM:
    return jsonify(roles), 200

@roles_bp.route('/', methods=['POST'])
def crear_rol():
    datos = request.get_json() or {}
    nombre_rol = datos.get('nombre_rol')
    if not nombre_rol:
        return jsonify({'error': 'Faltan campos obligatorios'}), 400
    resultado, status = RolService.crear_rol(nombre_rol)
    return jsonify(resultado), status
