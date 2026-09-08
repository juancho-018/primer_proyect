import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.security import generate_password_hash
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    template_dir = os.path.join(base_dir, 'templates')
    static_dir = os.path.join(base_dir, 'static')
    
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    
    # Configuración de base de datos MySQL / Cloud
    db_url = os.environ.get('DATABASE_URL', 'mysql://root:@localhost/bd_clc1')
    if db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql://", 1)
    elif db_url.startswith("mysql://"):
        # Asegurar compatibilidad con pymysql en servidores cloud donde mysqlclient C lib no está instalada
        try:
            import MySQLdb
        except ImportError:
            db_url = db_url.replace("mysql://", "mysql+pymysql://", 1)

    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'clc_secret_key_pastel_mvc_2026_super_secure_key_32bytes')

    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)
    from flask import request, redirect, url_for, flash
    from flask_login import current_user

    # Hook global: Obligatorio iniciar sesión para ver cualquier página
    @app.before_request
    def enforce_login_globally():
        if request.endpoint:
            # Permitir únicamente login, registro de usuarios, archivos estáticos y API de autenticación
            if request.endpoint.startswith('static') or request.endpoint.startswith('api.'):
                return
            if request.endpoint in ['auth.login', 'usuario.crearusuario', 'usuario.add_usuario']:
                return
            
            if not current_user.is_authenticated:
                flash("Debes iniciar sesión para acceder al sistema.", "warning")
                return redirect(url_for('auth.login'))

    # Definir user loader para Flask-Login
    from app.models.user import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(str(user_id))

    # Registrar Blueprints (Controladores)
    from app.controllers.main_controller import main_bp
    from app.controllers.auth_controller import auth_bp
    from app.controllers.cliente_controller import cliente_bp
    from app.controllers.usuario_controller import usuario_bp
    from app.controllers.producto_controller import producto_bp
    from app.controllers.categoria_controller import categoria_bp
    from app.controllers.proveedor_controller import proveedor_bp
    from app.controllers.pedido_controller import pedido_bp
    from app.controllers.venta_controller import venta_bp
    from app.controllers.api_controller import api_bp
    from app.controllers.compra_controller import compra_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(cliente_bp)
    app.register_blueprint(usuario_bp)
    app.register_blueprint(producto_bp)
    app.register_blueprint(categoria_bp)
    app.register_blueprint(proveedor_bp)
    app.register_blueprint(pedido_bp)
    app.register_blueprint(venta_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(compra_bp)

    # Inicializar tablas de base de datos si no existen
    with app.app_context():
        try:
            db.create_all()
        except Exception as e:
            print(f"[Advertencia DB]: {e}")

    return app
