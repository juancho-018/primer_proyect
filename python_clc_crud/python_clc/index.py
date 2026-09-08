"""
Archivo de entrada de compatibilidad.
Redirige al patrón App Factory en app/__init__.py
"""
from app import create_app

app = create_app()

if __name__ == '__main__':
    print("\n========================================================")
    print(" 🚀 Servidor Flask Iniciado (Modo MVC + Estética Pastel)")
    print(" 🌐 URL Local: http://127.0.0.1:5000")
    print("========================================================\n")
    app.run(debug=True, port=5000)
