from app import db

class Pedido(db.Model):
    __tablename__ = 'pedido'

    cod_pe = db.Column(db.Integer, primary_key=True)
    f_pe = db.Column(db.Date)
    cant_pe = db.Column(db.Integer)
    vt_pe = db.Column(db.String(30))
    cod_cli1 = db.Column(db.Integer, db.ForeignKey('cliente.cod_cli'), nullable=True)
