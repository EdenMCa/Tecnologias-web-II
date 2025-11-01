from flask import Blueprint, request, jsonify
from app.models.UsuariosModel import UsuariosModel
from app.service.AuthUsuarioService import AuthUsuarioService as AuthUsuario
from flask_jwt_extended import create_access_token, create_refresh_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    
    auth_usuario = AuthUsuario.authenticate_user(
        nombre_usuario=data.get('nombre_usuario'),
        password=data.get('password')
    )
    
    if auth_usuario:
        nombre_rol = auth_usuario.rol.nombre_rol
        access_token = create_access_token(
            identity=str(auth_usuario.id), 
            # opcional para agregar más información al token o si queremos hacer validaciones en endpoints
            additional_claims={"role": nombre_rol}
        )
        refresh_token = create_refresh_token(identity=str(auth_usuario.id))

    return jsonify({"message": "Login exitoso", "access_token": access_token, "refresh_token": refresh_token}), 200

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    
    return jsonify({"message": "Registro existoso"}), 201