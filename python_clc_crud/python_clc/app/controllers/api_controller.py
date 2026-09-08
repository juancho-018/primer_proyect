import datetime
import jwt
from functools import wraps
from flask import Blueprint, request, jsonify, current_app
from app.models.user import User
from app.models.producto import Producto
from app.models.pedido import Pedido
from app import db

api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

def jwt_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
        
        if not token:
            return jsonify({'message': 'Token de autenticación faltante'}), 401
        
        try:
            secret = current_app.config['SECRET_KEY']
            data = jwt.decode(token, secret, algorithms=['HS256'])
            current_user_obj = User.query.get(str(data['sub']))
            if not current_user_obj:
                return jsonify({'message': 'Usuario no válido'}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'El token JWT ha expirado'}), 401
        except Exception as e:
            return jsonify({'message': f'Token inválido: {str(e)}'}), 401

        return f(current_user_obj, *args, **kwargs)
    return decorated

@api_bp.route('/auth/login', methods=['POST'])
def api_login():
    data = request.get_json() or {}
    identificador = data.get('username') or data.get('nom_us') or data.get('correo')
    password = data.get('password') or data.get('con_us')

    if not identificador or not password:
        return jsonify({'message': 'Nombre de usuario/correo y contraseña requeridos'}), 400

    user = User.query.filter(
        (User.correo_usu == identificador) | (User.nom_us == identificador)
    ).first()

    if user and user.check_password(password):
        payload = {
            'sub': str(user.cod_us),
            'nom_us': user.nom_us,
            'correo': user.correo_usu,
            'rol': user.rol,
            'iat': datetime.datetime.now(datetime.timezone.utc),
            'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=24)
        }
        token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({
            'status': 'success',
            'access_token': token,
            'user': {
                'id': user.cod_us,
                'nombre': user.nom_us,
                'correo': user.correo_usu,
                'rol': user.rol
            }
        }), 200
    
    return jsonify({'message': 'Credenciales inválidas'}), 401

@api_bp.route('/productos', methods=['GET'])
def api_productos():
    productos = Producto.query.all()
    resultado = []
    for p in productos:
        resultado.append({
            'cod_p': p.cod_p,
            'nom_p': p.nom_p,
            'pre_p': p.pre_p,
            'col_p': p.col_p,
            'tam_p': p.tam_p,
            'tipo_p': p.tipo_p,
            'desc_p': p.desc_p,
            'cod_c1': p.cod_c1,
            'cod_prov1': p.cod_prov1
        })
    return jsonify({'status': 'success', 'count': len(resultado), 'productos': resultado}), 200

@api_bp.route('/pedidos', methods=['GET'])
@jwt_required
def api_pedidos(current_user_obj):
    pedidos = Pedido.query.all()
    resultado = []
    for pe in pedidos:
        resultado.append({
            'cod_pe': pe.cod_pe,
            'f_pe': str(pe.f_pe),
            'cant_pe': pe.cant_pe,
            'vt_pe': pe.vt_pe,
            'cod_cli1': pe.cod_cli1
        })
    return jsonify({'status': 'success', 'count': len(resultado), 'pedidos': resultado}), 200

@api_bp.route('/user/profile', methods=['GET'])
@jwt_required
def api_user_profile(current_user_obj):
    return jsonify({
        'status': 'success',
        'user': {
            'id': current_user_obj.cod_us,
            'nombre': current_user_obj.nom_us,
            'correo': current_user_obj.correo_usu,
            'rol': current_user_obj.rol
        }
    }), 200
