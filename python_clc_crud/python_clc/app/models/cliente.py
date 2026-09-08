from app import db

class Cliente(db.Model):
    __tablename__ = 'cliente'

    cod_cli = db.Column(db.Integer, primary_key=True)
    nom_cli = db.Column(db.String(100))
    corr_cli = db.Column(db.String(100))
    sexo_cli = db.Column(db.String(20))
    direc_cli = db.Column(db.String(150))
    tipoid_cli = db.Column(db.String(50))
    id_cli = db.Column(db.BigInteger)
    fn_cli = db.Column(db.Date)
