from flask import Blueprint, request, jsonify
from app.models.UsuariosModel import UsuariosModel
from app.service.AuthUsuarioService import AuthUsuarioService
from flask_jwt_extended import create_access_token, create_refresh_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    nombre_usuario = data.get('nombre_usuario')
    password = data.get('password')
    
    auth_usuario = AuthUsuarioService.authenticateUser(
        nombre_usuario = nombre_usuario,
        password = password
    )
    
    if auth_usuario:
        nombre_rol = auth_usuario.rol.nombre_rol
        access_token = create_access_token(
            identity=str(auth_usuario.id), 
            # opcional para agregar más información al token o si queremos hacer validaciones en endpoints
            additional_claims={
                "rol": nombre_rol
            }
        )
        refresh_token = create_refresh_token(identity=str(auth_usuario.id))

        return jsonify({
            "message": "Login exitoso",
            'data':{
                "access_token": access_token,
                "refresh_token": refresh_token
            }
        }), 200
    else:
        return jsonify({"message": "Credenciales inválidas"})