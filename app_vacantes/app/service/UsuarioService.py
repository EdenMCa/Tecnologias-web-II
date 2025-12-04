# Archivo creado con el fin de implementar la logica de negocio para usuarios.
from app.models.UsuariosModel import UsuariosModel, RolModel
from app.extensions import db

class UsuarioService:

    @staticmethod
    def obtener_usuarios():
        usuarios = UsuariosModel.query.all()
        return [u.to_dict() for u in usuarios]
        
    @staticmethod
    def crear_usuario(nombre_usuario, password, rol_id):

        if not nombre_usuario or not password or rol_id is None:
            return ({'error': 'Faltan campos obligatorios (nombre_usuario, password, rol_id)'}), 400
        
        if UsuariosModel.query.filter_by(nombre_usuario=nombre_usuario).first():
            return ({'error': 'El nombre de usuario ya existe'}), 400

        # Verificar que el rol exista
        rol = RolModel.query.get(rol_id)
        if not rol:
            return {'error': f'Rol con id {rol_id} no encontrado'}, 404

        # Crear el nuevo usuario
        nuevo_usuario = UsuariosModel(
            nombre_usuario = nombre_usuario,
            password = password,
            rol_id = rol_id
        )
        
        # Try except para manejar errores al guardar en la base de datos
        try:
            # Add sirve para agregar el objeto a la sesión actual
            db.session.add(nuevo_usuario)

            # Commit guarda los cambios en la base de datos
            db.session.commit()
            return ({'mensaje': 'Usuario creado exitosamente', 'usuario': nuevo_usuario.to_dict()}), 201
        except Exception as e:
            db.session.rollback()
            return ({'error': 'Error al guardar el usuario en la base de datos', 'detalle': str(e)}), 500
    

    # Buscar usuario por id
    @staticmethod
    def obtener_usuario_por_id(usuario_id):
        usuario = UsuariosModel.query.get(usuario_id)
        if not usuario:
            return {'error': 'Usuario no encontrado'}, 404
        return usuario.to_dict(), 200
      
    # Actualizar usuario por id
    @staticmethod
    def actualizar_usuario(usuario_id, datos_actualizados):
        # Busca el usuario en la base de datos
        usuario = UsuariosModel.query.get(usuario_id)
        
        # Verificar si el usuario existe
        if not usuario:
            return ({'error': 'Usuario no encontrado'}), 404

        # Actualizar los campos del usuario
        # Actualizar campos si vienen en el body
        if 'nombre_usuario' in datos_actualizados:
            # verificar unicidad si se cambia el nombre
            nuevo_nombre = datos_actualizados['nombre_usuario']
            if nuevo_nombre != usuario.nombre_usuario and UsuariosModel.query.filter_by(nombre_usuario=nuevo_nombre).first():
                return {'error': 'El nombre de usuario ya existe'}, 400
            usuario.nombre_usuario = nuevo_nombre

        if 'password' in datos_actualizados:
            usuario.password = datos_actualizados['password']


        if 'rol_id' in datos_actualizados:
            nuevo_rol_id = datos_actualizados['rol_id']
            rol = RolModel.query.get(nuevo_rol_id)
            if not rol:
                return {'error': f'Rol con id {nuevo_rol_id} no encontrado'}, 404
            usuario.rol_id = nuevo_rol_id

        try:
            db.session.commit()
            return ({'mensaje': 'Usuario actualizado exitosamente', 'usuario': usuario.to_dict()}), 200
        except Exception as e:
            return ({'error': 'Error al actualizar el usuario en la base de datos', 'detalle': str(e)}), 500
        
    # Eliminar usuario por id
    @staticmethod
    def eliminar_usuario(usuario_id):
        # Busca el usuario en la base de datos
        usuario = UsuariosModel.query.get(usuario_id)
        
        # Verificar si el usuario existe
        if not usuario:
            return ({'error': 'Usuario no encontrado'}), 404
        
        try:
            # Sirve para eliminar el objeto de la sesión actual.
            db.session.delete(usuario)
            db.session.commit()
            return ({'mensaje': 'Usuario eliminado exitosamente'}), 200
        except Exception as e:
            return ({'error': 'Error al eliminar el usuario de la base de datos', 'detalle': str(e)}), 500 