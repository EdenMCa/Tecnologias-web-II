from app.models.VacanteModel import VacanteModel
from app.models.UsuariosModel import UsuariosModel
from app.extensions import db
from datetime import datetime

class VacanteService:

    @staticmethod
    def crear_vacante(usuario_creador_id, nombre_vacante, descripcion=None, detalles=None):
        if not nombre_vacante:
            return {'error': 'Faltan campos obligatorios (nombre)'}, 400

        # verificar que creador exista y sea reclutador si se desea (validación en routes también)
        usuario_creador = UsuariosModel.query.get(usuario_creador_id)
        if not usuario_creador:
            return {'error': f'Usuario creador con id {usuario_creador_id} no encontrado'}, 404

        nueva_vacante = VacanteModel(
            nombre_vacante=nombre_vacante,
            descripcion=descripcion,
            detalles=detalles,
            fecha_publicacion=datetime.utcnow(),
            fecha_edicion=None,
            estado='Disponible',
            usuario_creador_id = usuario_creador_id
        )
        try:
            db.session.add(nueva_vacante)
            db.session.commit()
            return {'mensaje': 'Vacante creada', 'vacante': nueva_vacante.to_dict()}, 201
        except Exception as e:
            db.session.rollback()
            return {'error': 'Error al crear vacante', 'detalle': str(e)}, 500

    @staticmethod
    def editar_vacante(vacante_id, usuario_creador_id, datos_actualizados):
        vacante = VacanteModel.query.get(vacante_id)
        if not vacante:
            return {'error': 'Vacante no encontrada'}, 404

        # solo el creador puede editar
        if vacante.usuario_creador_id != usuario_creador_id:
            return {'error': 'No autorizado: solo el creador puede editar'}, 403

        if 'nombre_vacante' in datos_actualizados:
            vacante.nombre = datos_actualizados['nombre_vacante']
        if 'descripcion' in datos_actualizados:
            vacante.descripcion = datos_actualizados['descripcion']
        if 'detalles' in datos_actualizados:
            vacante.detalles = datos_actualizados['detalles']

        vacante.fecha_edicion = datetime.utcnow()
        try:
            db.session.commit()
            return {'mensaje': 'Vacante actualizada', 'vacante': vacante.to_dict()}, 200
        except Exception as e:
            db.session.rollback()
            return {'error': 'Error al actualizar vacante', 'detalle': str(e)}, 500

    @staticmethod
    def obtener_vacantes_disponibles():
        vacantes = VacanteModel.query.filter_by(estado='Disponible').all()
        return [vacante.to_dict() for vacante in vacantes], 200

    @staticmethod
    def obtener_ultimas_tres_disponibles():
        vacantes = VacanteModel.query.filter_by(estado='Disponible').order_by(VacanteModel.fecha_publicacion.desc()).limit(3).all()
        return [vacante.to_dict() for vacante in vacantes], 200

    @staticmethod
    def obtener_vacante_por_id(vacante_id):
        vacante = VacanteModel.query.get(vacante_id)
        if not vacante:
            return {'error': 'Vacante no encontrada'}, 404
        return vacante.to_dict(), 200

    @staticmethod
    def listar_por_creador(usuario_creador_id):
        vacantes = VacanteModel.query.filter_by(usuario_creador_id=usuario_creador_id).all()
        return [vacante.to_dict() for vacante in vacantes], 200

    @staticmethod
    def asignar_vacante(vacante_id, reclutador_id, usuario_postulante_id):
        vacante = VacanteModel.query.get(vacante_id)
        if not vacante:
            return {'error': 'Vacante no encontrada'}, 404

        # solo el creador (reclutador) puede asignar
        if vacante.usuario_creador_id != reclutador_id:
            return {'error': 'No autorizado: solo el creador puede asignar'}, 403

        if vacante.estado == 'Ocupada':
            return {'error': 'Vacante ya está ocupada'}, 400

        usuario_postulante_id = UsuariosModel.query.get(usuario_postulante_id)
        if not usuario_postulante_id:
            return {'error': f'Postulante con id {usuario_postulante_id} no encontrado'}, 404

        vacante.usuario_postulante_id = usuario_postulante_id
        vacante.estado = 'Ocupada'
        vacante.fecha_edicion = datetime.utcnow()

        try:
            db.session.commit()
            return {'mensaje': 'Vacante asignada exitosamente', 'vacante': vacante.to_dict()}, 200
        except Exception as e:
            db.session.rollback()
            return {'error': 'Error al asignar vacante', 'detalle': str(e)}, 500
