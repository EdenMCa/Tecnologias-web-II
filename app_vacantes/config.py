import os
from dotenv import load_dotenv
from datetime import timedelta

# Cargar .env aquí para que os.getenv() dentro de la clase Config vea las variables.
load_dotenv()


class Config:
    DEBUG = True  # Para que se recargue la app al guardar (ctrl + s).
    PORT = 5000  # Se puede cambiar el puerto.

    # Construir la URI con valores por defecto razonables
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'root')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '3306')
    DB_NAME = os.getenv('DB_NAME', 'vacantes_db')

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desactivar para evitar warnings. Consume recursos
    
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")  # Cambiar en producción
    
    # Token para hacer operaciones autenticadas.
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)  # Duración del token de acceso
    
    # Token para refrescar el acceso. Sirve para obtener un nuevo token de acceso sin necesidad de loguearse de nuevo.
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)  # Duración del token de refresco