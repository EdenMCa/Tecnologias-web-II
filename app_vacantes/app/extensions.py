# Aquí crearemos las instancias
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy() # Instancia de SQLAlchemy para manejar la base de datos.
jwt = JWTManager() # Instancia de JWTManager para manejar la autenticación JWT.