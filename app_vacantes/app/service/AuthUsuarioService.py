from app.models.UsuariosModel import UsuariosModel

class AuthUsuarioService:
    @staticmethod
    def authenticateUser(nombre_usuario, password):
        usuario_db = UsuariosModel.query.filter_by(nombre_usuario=nombre_usuario).first()
        
        if usuario_db and usuario_db.password == password:
            return usuario_db
        return None