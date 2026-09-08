from flask import Blueprint, render_template
from app.models.producto import Producto
from app.models.categoria import Categoria

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def inicio():
    productos = Producto.query.all()
    return render_template('inicio.html', productos=productos)

@main_bp.route('/inicioadmin')
def inicioadmin():
    return render_template('inicioadmin.html')

@main_bp.route('/seccion')
def seccion():
    categorias = Categoria.query.all()
    productos = Producto.query.all()
    return render_template('seccion.html', categorias=categorias, productos=productos)

@main_bp.route('/products')
def products():
    productos = Producto.query.all()
    return render_template('products.html', productos=productos)

@main_bp.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@main_bp.route('/yo')
def yo():
    return render_template('yo.html')

@main_bp.route('/iniciocrud')
def iniciocrud():
    return render_template('iniciocrud.html')
