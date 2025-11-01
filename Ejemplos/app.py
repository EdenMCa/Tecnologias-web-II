from flask import Flask, jsonify  # Importamos Flask y jsonify

app = Flask(__name__)  # Inicializamos la app

usuarios = [
    {"id": 1, "nombre": "Rosendo"},
    {"id": 2, "nombre": "Eden"}
]

@app.route('/')  # Ruta principal
def hola(): 
    return '¡Hola Mundo! c:'

@app.route('/usuarios')  # Ruta para obtener usuarios
def obtener_usuarios():
    return jsonify(usuarios)  # Devuelve JSON

if __name__ == '__main__':
    app.run(debug=True)
