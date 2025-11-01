from app import create_app
from app.extensions import db
from sqlalchemy import text

app = create_app() # Devuelve una instancia de la aplicación Flask.

def check_db_connection(app):
    """Función para verificar la conexión a la base de datos al iniciar la aplicación."""
    try:
        with app.app_context():
            # Intentar ejecutar una consulta simple
            db.session.execute(text("SELECT 1"))
            print("Conexión a la base de datos exitosa.")
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        
if __name__ == '__main__':
    # Usar puerto por defecto si no está en la configuración
    port = app.config.get('PORT', 5000)
    host = app.config.get('HOST', '127.0.0.1')
    debug = app.config.get('DEBUG', True)
    check_db_connection(app) # Se llama a la función para verificar la conexión a la base de datos.
    app.run(host=host, port=port, debug=debug)
    