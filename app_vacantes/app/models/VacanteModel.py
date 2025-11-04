from app.extensions import db
from datetime import datetime

class VacanteModel(db.Model):
    __tablename__ = 'vacantes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_vacante = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    detalles = db.Column(db.Text, nullable=True)
    fecha_publicacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    fecha_edicion = db.Column(db.DateTime, nullable=True)
    estado = db.Column(db.String(20), nullable=False, default='Disponible')  # 'Disponible' | 'Ocupada'

    # relaciones a usuarios
    usuario_creador_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    usuario_postulante_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=True)

    # relaciones 
    usuario_creador = db.relationship('UsuariosModel', foreign_keys=[usuario_creador_id], backref='vacantes_creadas', lazy=True)
    usuario_postulante = db.relationship('UsuariosModel', foreign_keys=[usuario_postulante_id], backref='vacantes_postuladas', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre_vacante': self.nombre_vacante,
            'descripcion': self.descripcion,
            'detalles': self.detalles,
            'fecha_publicacion': self.fecha_publicacion.isoformat() if self.fecha_publicacion else None,
            'fecha_edicion': self.fecha_edicion.isoformat() if self.fecha_edicion else None,
            'estado': self.estado,
            'usuario_creador_id': self.usuario_creador_id,
            'usuario_postulante_id': self.usuario_postulante_id,
            'usuario_creador': self.usuario_creador.nombre_usuario if self.usuario_creador else None,
            'usuario_postulante': self.usuario_postulante.nombre_usuario if self.usuario_postulante else None
        }
    
