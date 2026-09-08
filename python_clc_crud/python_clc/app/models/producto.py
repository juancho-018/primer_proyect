from app import db

class Producto(db.Model):
    __tablename__ = 'producto'

    cod_p = db.Column(db.Integer, primary_key=True)
    col_p = db.Column(db.String(50))
    tam_p = db.Column(db.String(50))
    tipo_p = db.Column(db.String(50))
    pre_p = db.Column(db.String(30))
    desc_p = db.Column(db.String(30))
    nom_p = db.Column(db.String(100))
    cod_prov1 = db.Column(db.Integer, db.ForeignKey('proveedor.cod_prov'), nullable=True)
    cod_c1 = db.Column(db.Integer, db.ForeignKey('categoria.cod_c'), nullable=True)
