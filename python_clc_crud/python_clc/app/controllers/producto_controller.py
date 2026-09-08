from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.producto import Producto
from app.models.categoria import Categoria
from app.models.proveedor import Proveedor
from app import db

producto_bp = Blueprint('producto', __name__)

@producto_bp.route('/crearproducto')
def crearproducto():
    return render_template('crearproducto.html')

@producto_bp.route('/tproducto', methods=['GET'])
def tproducto():
    cod_p = request.args.get('cod_p')
    if cod_p:
        productos = Producto.query.filter_by(cod_p=cod_p).all()
    else:
        productos = Producto.query.all()
    return render_template('tproducto.html', productos=productos)

@producto_bp.route('/add_producto', methods=['POST'])
def add_producto():
    cod_p = request.form.get('cod_p')
    col_p = request.form.get('col_p')
    tam_p = request.form.get('tam_p')
    tipo_p = request.form.get('tipo_p')
    pre_p = request.form.get('pre_p')
    desc_p = request.form.get('desc_p')
    nom_p = request.form.get('nom_p')
    cod_c1 = request.form.get('cod_c1')
    cod_prov1 = request.form.get('cod_prov1')

    # Verificar categoría y proveedor si se proporcionaron
    if cod_c1 and not Categoria.query.get(cod_c1):
        flash('Error: La categoría especificada no existe.', 'danger')
        return redirect(url_for('producto.tproducto'))
    
    if cod_prov1 and not Proveedor.query.get(cod_prov1):
        flash('Error: El proveedor especificado no existe.', 'danger')
        return redirect(url_for('producto.tproducto'))

    try:
        nuevo_prod = Producto(
            cod_p=cod_p,
            col_p=col_p,
            tam_p=tam_p,
            tipo_p=tipo_p,
            pre_p=pre_p,
            desc_p=desc_p,
            nom_p=nom_p,
            cod_c1=cod_c1,
            cod_prov1=cod_prov1
        )
        db.session.add(nuevo_prod)
        db.session.commit()
        flash('Producto agregado exitosamente.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al agregar producto: {e}', 'danger')

    return redirect(url_for('producto.tproducto'))

@producto_bp.route('/eliminar_producto/<string:cod_p>')
def eliminar_producto(cod_p):
    try:
        prod = Producto.query.get(cod_p)
        if prod:
            db.session.delete(prod)
            db.session.commit()
            flash('Producto eliminado exitosamente.', 'success')
        else:
            flash('Producto no encontrado.', 'warning')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al eliminar producto: {e}', 'danger')
    return redirect(url_for('producto.tproducto'))

@producto_bp.route('/editar_producto/<string:cod_p>')
def obtener_producto(cod_p):
    prod = Producto.query.get(cod_p)
    if not prod:
        flash('Producto no encontrado.', 'danger')
        return redirect(url_for('producto.tproducto'))
    return render_template('editproducto.html', producto=prod)

@producto_bp.route('/actualizar_producto/<string:cod_p>', methods=['POST'])
def actualizar_producto(cod_p):
    try:
        prod = Producto.query.get(cod_p)
        if prod:
            prod.col_p = request.form.get('col_p')
            prod.tam_p = request.form.get('tam_p')
            prod.tipo_p = request.form.get('tipo_p')
            prod.pre_p = request.form.get('pre_p')
            prod.desc_p = request.form.get('desc_p')
            prod.nom_p = request.form.get('nom_p')
            prod.cod_c1 = request.form.get('cod_c1')
            prod.cod_prov1 = request.form.get('cod_prov1')
            db.session.commit()
            flash('Producto actualizado exitosamente.', 'success')
        else:
            flash('Producto no encontrado.', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al actualizar producto: {e}', 'danger')
    return redirect(url_for('producto.tproducto'))
