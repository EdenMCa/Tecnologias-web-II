from flask import Flask
from dotenv import load_dotenv

# Cargar variables que esten en env lo antes posible
load_dotenv()

from app.routes.usuarios_routes import usuarios_bp
from app.routes.roles_routes import roles_bp
from app.routes.auth_routes import auth_bp
from app.routes.vacantes_routes import vacantes_bp  
from app.extensions import db, jwt
from config import Config
from app.models.UsuariosModel import UsuariosModel, RolModel  # Importar el modelo para crear la tabla
from app.models.VacanteModel import VacanteModel 

# Crear e iniciar nuestra aplicación, devolver una instancia de la clase Flask con las configuraciones asignadas.

# Definimos la función
def create_app():
    # Instancear la clase
    app = Flask(__name__)
    
    # Cargar una configuracion
    app.config.from_object(Config)

    # Inicializar las extensiones (después de cargar la configuración), reciben el contexto de la app
    db.init_app(app)
    jwt.init_app(app) 
    
    # Para probar de manera local: crear/actualizar las tablas sólo si la conexión funciona.
    with app.app_context():
        try:
            #   db.drop_all()  # Elimina las tablas en la base de datos si existen. Cada que se reinicie la app se borran los datos.
            db.create_all()  # Crea las tablas en la base de datos si no existen.
        except Exception as e:
            # No romper el arranque por errores de conexión (credenciales/DB apagada).
            print('Advertencia: no se pudieron crear/actualizar las tablas:', e)
    
    # Registrar blueprint
    app.register_blueprint(usuarios_bp, url_prefix='/usuarios')
    app.register_blueprint(roles_bp, url_prefix='/roles')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(vacantes_bp, url_prefix='/vacantes')
    
    return app