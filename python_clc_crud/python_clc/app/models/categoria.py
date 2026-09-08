from app import db

class Categoria(db.Model):
    __tablename__ = 'categoria'

    cod_c = db.Column(db.Integer, primary_key=True)
    nom_c = db.Column(db.String(100))
