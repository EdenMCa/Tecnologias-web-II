# En este archivo iran las rutas o EndPoints que tengan que ver con el CRUD de usuarios.

from flask import Blueprint, jsonify, request
from app.service.UsuarioService import UsuarioService

# Se crea el Blueprint
usuarios_bp = Blueprint('usuarios', __name__)


# Listar usuarios
@usuarios_bp.route('/', methods=['GET'])

def obtener_todos():
    usuarios = UsuarioService.obtener_usuarios()
    
    # Verificar si hay usuarios, si no hay, retornar un mensaje adecuado.
    if not usuarios:
        return jsonify({'mensaje': 'No hay usuarios registrados'}), 404
    
    return jsonify(usuarios), 200

# Crear usuarios
@usuarios_bp.route('/', methods=['POST'])
def crear_usuario():
    nuevo = request.get_json() or {}
    respuesta, status = UsuarioService.crear_usuario(
        nombre_usuario = nuevo.get('nombre_usuario'),
        password = nuevo.get('password'),
        rol_id = nuevo.get('rol_id')
    )
    return jsonify(respuesta), status

# Obtener un usuario por su id
@usuarios_bp.route('/<int:usuario_id>', methods=['GET'])
def obtener_usuario_por_id(usuario_id):
    resultado, status = UsuarioService.obtener_usuario_por_id(usuario_id)
    return jsonify(resultado), status

# Actualizar informacion de un usuario
@usuarios_bp.route('/<int:usuario_id>', methods=['PUT'])
def actualizar_usuario(usuario_id):
    datos_actualizados = request.get_json() or {}
    resultado, status = UsuarioService.actualizar_usuario(usuario_id, datos_actualizados)
    return jsonify(resultado), status

# Eliminar un usuario por su id
@usuarios_bp.route('/<int:usuario_id>', methods=['DELETE'])
def eliminar_usuario(usuario_id):
    resultado, status = UsuarioService.eliminar_usuario(usuario_id)
    return jsonify(resultado), status