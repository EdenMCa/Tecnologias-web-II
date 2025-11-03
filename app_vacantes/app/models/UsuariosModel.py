from app.extensions import db # Importar la instancia de db

class RolModel(db.Model):
    __tablename__ = 'roles'  # Nombre de la tabla en la base de datos.

    id = db.Column(db.Integer, primary_key=True) # Llave primaria
    nombre_rol = db.Column(db.String(50), nullable=False, unique=True) # Campo obligatorio

    usuarios = db.relationship('UsuariosModel', back_populates='rol', lazy=True) # Relación inversa

    def to_dict(self):
        return {
            'id': self.id,
            'nombre_rol': self.nombre_rol
        }

# Extiende de db.Model
class UsuariosModel(db.Model):
    __tablename__ = 'usuarios'  # Nombre de la tabla en la base de datos, si no se define, SQLAlchemy lo genera automáticamente.

    id = db.Column(db.Integer, primary_key=True) # Llave primaria, por defecto es autoincremental
    nombre_usuario = db.Column(db.String(50), nullable=False, unique=True) # Campo obligatorio
    password = db.Column(db.String(100), nullable=False) 

    # Establecer relación con RolModel (uno a muchos)
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    rol = db.relationship('RolModel', back_populates='usuarios')
        
    def to_dict(self):
        return {
            'id': self.id,
            'nombre_usuario': self.nombre_usuario,
            'password': self.password
        }
    