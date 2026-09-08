from app import create_app

app = create_app()

if __name__ == '__main__':
    print("\n========================================================")
    print(" 🚀 Servidor Flask Iniciado (Modo MVC + Estética Pastel)")
    print(" 👤 Usuario Admin predeterminado: admin@gmail.com")
    print(" 🔑 Contraseña Admin: admin123")
    print(" 🌐 URL Local: http://127.0.0.1:5000")
    print("========================================================\n")
    app.run(debug=True, port=5000)
