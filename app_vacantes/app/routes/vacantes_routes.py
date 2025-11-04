from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from app.service.VacanteService import VacanteService

vacantes_bp = Blueprint('vacantes', __name__)

# Crear vacante 
@vacantes_bp.route('/crear', methods=['POST'])
@jwt_required()
def crear_vacante():
    claims = get_jwt()
    rol = claims.get('rol')
    if rol != 'Reclutador':
        return jsonify({'error': 'No autorizado: se requiere rol Reclutador'}), 403

    datos = request.get_json() or {}
    usuario_id = int(get_jwt_identity())  
    nombre_vacante = datos.get('nombre_vacante') 
    descripcion = datos.get('descripcion')
    detalles = datos.get('detalles')

    resultado, status = VacanteService.crear_vacante(
        usuario_id, 
        nombre_vacante, 
        descripcion, 
        detalles)
    return jsonify(resultado), status

# Editar vacante
@vacantes_bp.route('/<int:vacante_id>', methods=['PUT'])
@jwt_required()
def editar_vacante(vacante_id):
    claims = get_jwt()
    rol = claims.get('rol') 
    if rol != 'Reclutador':
        return jsonify({'error': 'Acceso denegado. No autorizado xc'}), 403

    datos = request.get_json() or {}
    usuario_actual_id = int(get_jwt_identity())
    resultado, status = VacanteService.editar_vacante(vacante_id, usuario_actual_id, datos)
    return jsonify(resultado), status

# Listar vacantes del reclutador autenticado (mis vacantes)
@vacantes_bp.route('/mis_vacantes', methods=['GET'])
@jwt_required()
def obtener_mis_vacantes():
    claims = get_jwt()
    rol = claims.get('rol')
    if rol != 'Reclutador':
        return jsonify({'error': 'No autorizado'}), 403

    usuario_id = int(get_jwt_identity())
    resultado, status = VacanteService.listar_por_creador(usuario_id)
    return jsonify(resultado), status

# Listar vacantes disponibles (público o postulante)
@vacantes_bp.route('/disponibles', methods=['GET'])
def listar_vacantes_disponibles():
    resultado, status = VacanteService.obtener_vacantes_disponibles()
    return jsonify(resultado), status

# Ultimas 3 disponibles
@vacantes_bp.route('/ultimas', methods=['GET'])
def ultimas_tres():
    resultado, status = VacanteService.obtener_ultimas_tres_disponibles()
    return jsonify(resultado), status

# Obtener detalle vacante (postulante puede ver si disponible; reclutador puede ver si es creador)
@vacantes_bp.route('/<int:vacante_id>', methods=['GET'])
@jwt_required(optional=True)
def detalle_vacante(vacante_id):
    resultado, status = VacanteService.obtener_vacante_por_id(vacante_id)
    if status != 200:
        return jsonify(resultado), status

    vacante = resultado
    jwt_data = None
    try:
        jwt_data = get_jwt()
    except Exception:
        jwt_data = None

    # si no autenticado y vacante no disponible -> deny
    if not jwt_data and vacante.get('estado') != 'Disponible':
        return jsonify({'error': 'No autorizado para ver esta vacante'}), 403

    return jsonify(vacante), 200

# Asignar vacante (reclutador)
@vacantes_bp.route('/<int:vacante_id>/asignar', methods=['POST'])
@jwt_required()
def asignar_vacante(vacante_id):
    claims = get_jwt()
    rol = claims.get('rol')
    if rol != 'Reclutador':
        return jsonify({'error': 'No autorizado'}), 403

    datos = request.get_json() or {}
    usuario_postulante_id = datos.get('postulante_id')
    if not usuario_postulante_id:
        return jsonify({'error': 'Faltan datos: postulante_id'}), 400

    reclutador_id = int(get_jwt_identity())
    resultado, status = VacanteService.asignar_vacante(vacante_id, reclutador_id, usuario_postulante_id)
    return jsonify(resultado), status
