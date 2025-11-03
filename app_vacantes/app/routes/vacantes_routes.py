from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from app.service.VacanteService import VacanteService

vacantes_bp = Blueprint('vacantes', __name__)

# Crear vacante 
@vacantes_bp.route('/', methods=['POST'])
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

@vacantes_bp.route('/<int:vacante_id>', methods=['PUT'])
@jwt_required()
def editar_vacante(vacante_id):
    claims = get_jwt()
    rol = claims.get('role') 
    if rol != 'Reclutador':
        return jsonify({'error': 'Acceso denegado. No autorizado xc'}), 403

    datos = request.get_json() or {}
    usuario_actual_id = int(get_jwt_identity())
    resultado, status = VacanteService.editar_vacante(vacante_id, usuario_actual_id, datos)
    return jsonify(resultado), status

# Listar vacantes disponibles 
@vacantes_bp.route('/', methods=['GET'])
def obtener_vacantes():
    resultado, status = VacanteService.listar_vacantes_disponibles()
    return jsonify(resultado), status

# Ultimas 3 disponibles
@vacantes_bp.route('/latest', methods=['GET'])
def ultimas_tres():
    resultado, status = VacanteService.listar_ultimas_tres_disponibles()
    return jsonify(resultado), status

# Obtener detalle vacante (postulante puede ver si disponible; reclutador puede ver si es creador)
@vacantes_bp.route('/<int:vacante_id>', methods=['GET'])
@jwt_required(optional=True)
def detalle_vacante(vacante_id):
    # optional=True permite que endpoint sea accesible sin token (si quieres)
    resultado, status = VacanteService.obtener_vacante_por_id(vacante_id)
    if status != 200:
        return jsonify(resultado), status

    vac = resultado  # dict
    # si llamaron con token, podemos aplicar restricciones, si lo deseas
    # aquí suponemos que postulante solo ve disponibles, pero si deseas permitir ver siempre, omitir chequeo.
    jwt_data = None
    try:
        jwt_data = get_jwt()
        identity = get_jwt_identity()
    except Exception:
        jwt_data = None

    # si no autenticado y vacante no disponible -> deny
    if not jwt_data and vac['estado'] != 'Disponible':
        return jsonify({'error': 'No autorizado para ver esta vacante'}), 403

    return jsonify(vac), 200

# Listar vacantes del reclutador autenticado
@vacantes_bp.route('/mis', methods=['GET'])
@jwt_required()
def vacantes_reclutador():
    claims = get_jwt()
    rol = claims.get('rol')
    if rol != 'Reclutador':
        return jsonify({'error': 'No autorizado'}), 403

    usuario_id = int(get_jwt_identity())
    resultado, status = VacanteService.listar_por_creador(usuario_id)
    return jsonify(resultado), status

# Asignar vacante (reclutador)
@vacantes_bp.route('/<int:vacante_id>/assign', methods=['POST'])
@jwt_required()
def asignar_vacante(vacante_id):
    claims = get_jwt()
    rol = claims.get('rol')
    if rol != 'Reclutador':
        return jsonify({'error': 'No autorizado'}), 403

    datos = request.get_json() or {}
    postulante_id = datos.get('postulante_id')
    if not postulante_id:
        return jsonify({'error': 'Faltan datos: postulante_id'}), 400

    reclutador_id = int(get_jwt_identity())
    resultado, status = VacanteService.asignar_vacante(vacante_id, reclutador_id, postulante_id)
    return jsonify(resultado), status
