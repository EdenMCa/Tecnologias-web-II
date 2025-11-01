from app.models.UsuariosModel import UsuariosModel

class AuthUsuarioService:
    @staticmethod
    def authenticate_user(nombre_usuario, password):
        usuario = UsuariosModel.query.filter_by(nombre_usuario=nombre_usuario).first()
        
        if usuario and usuario.password == password:
            return usuario
        return None