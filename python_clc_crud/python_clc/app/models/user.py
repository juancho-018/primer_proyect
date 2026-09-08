from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = 'usuario'

    cod_us = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom_us = db.Column(db.String(80), nullable=False)
    con_us = db.Column(db.String(255), nullable=False)
    correo_usu = db.Column(db.String(120), nullable=False)
    rol = db.Column(db.String(20), default='usuario')

    def set_password(self, password):
        self.con_us = generate_password_hash(password)

    def check_password(self, password):
        if not self.con_us:
            return False
        
        # 1. Verificación directa en texto plano (respaldo usuarios antiguos)
        if self.con_us == password:
            return True
            
        # 2. Verificación con Hash seguro de Werkzeug
        try:
            if self.con_us.startswith('scrypt:') or self.con_us.startswith('pbkdf2:'):
                if check_password_hash(self.con_us, password):
                    return True
        except Exception:
            pass

        # 3. Respaldo si el hash fue truncado por una columna MySQL corta previa
        if len(self.con_us) <= 30 and password.startswith(self.con_us):
            return True

        return False

    def get_id(self):
        return str(self.cod_us)
