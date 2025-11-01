from app.models.UsuariosModel import RolModel
from app.extensions import db

class RolService:

    @staticmethod
    def obtener_roles():
        # Retorna lista de diccionarios con roles y sus usuarios (nombres)        
        roles = RolModel.query.all()
        return [
            {
                'id': r.id,
                'nombre_rol': r.nombre_rol,
                'usuarios': [u.nombre_usuario for u in r.usuarios]  # lista de nombres
            }
            for r in roles
        ]
    
    @staticmethod
    def crear_rol(nombre_rol):

        if not nombre_rol:
            return ({'error': 'Faltan campos obligatorios'}), 400
        
        # Verificar existencia
        if RolModel.query.filter_by(nombre_rol=nombre_rol).first():
            return ({'error': 'El nombre del rol ya existe'}), 400

        nuevo_rol = RolModel(
            nombre_rol=nombre_rol
        )
        
        try:
            db.session.add(nuevo_rol)
            db.session.commit()
            return {
                'mensaje': 'Rol creado exitosamente',
                'rol': nuevo_rol.to_dict()
            }, 201
        except Exception as e:
            db.session.rollback()
            return {'error': 'Error al crear rol', 'detalle': str(e)}, 500
