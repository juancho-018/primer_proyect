from app import db

class Proveedor(db.Model):
    __tablename__ = 'proveedor'

    cod_prov = db.Column(db.Integer, primary_key=True)
    nom_prov = db.Column(db.String(100))
    tel_prov = db.Column(db.String(30))
    trans_prov = db.Column(db.String(30))
    edad_prov = db.Column(db.Integer)
    direc_prov = db.Column(db.String(150))
    sexo_prov = db.Column(db.String(20))
    tipoid_prov = db.Column(db.String(50))
    id_prov = db.Column(db.BigInteger)
    corr_prov = db.Column(db.String(100))
