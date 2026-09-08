from app import db

class Venta(db.Model):
    __tablename__ = 'ventas'

    cod_ven = db.Column(db.Integer, primary_key=True)
    cod_pe1 = db.Column(db.Integer, db.ForeignKey('pedido.cod_pe'), nullable=True)
    cod_p1 = db.Column(db.Integer, db.ForeignKey('producto.cod_p'), nullable=True)
