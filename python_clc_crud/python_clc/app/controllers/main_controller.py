from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user
from app.models.producto import Producto
from app.models.categoria import Categoria

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def inicio():
    productos = Producto.query.all()
    return render_template('inicio.html', productos=productos)

@main_bp.route('/inicioadmin')
def inicioadmin():
    if not current_user.is_authenticated or current_user.rol != 'admin':
        flash('Acceso restringido únicamente a usuarios administradores.', 'danger')
        return redirect(url_for('main.inicio'))
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
    if not current_user.is_authenticated or current_user.rol != 'admin':
        flash('Acceso restringido únicamente a usuarios administradores.', 'danger')
        return redirect(url_for('main.inicio'))
    return render_template('iniciocrud.html')
