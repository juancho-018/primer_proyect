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
        # Permite verificación segura con hash o contraseña plana antigua de respaldo
        if self.con_us.startswith('scrypt:') or self.con_us.startswith('pbkdf2:'):
            return check_password_hash(self.con_us, password)
        return self.con_us == password

    def get_id(self):
        return str(self.cod_us)
