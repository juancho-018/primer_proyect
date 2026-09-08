from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.venta import Venta
from app.models.pedido import Pedido
from app.models.producto import Producto
from app import db

venta_bp = Blueprint('venta', __name__)

@venta_bp.route('/crearventas')
def crearventas():
    return render_template('crearventas.html')

@venta_bp.route('/tventa', methods=['GET'])
def tventa():
    cod_ven = request.args.get('cod_ven')
    if cod_ven:
        ventas = Venta.query.filter_by(cod_ven=cod_ven).all()
    else:
        ventas = Venta.query.all()
    return render_template('tventa.html', venta=ventas)

@venta_bp.route('/add_ventas', methods=['POST'])
def add_venta():
    cod_ven = request.form.get('cod_ven')
    cod_pe1 = request.form.get('cod_pe1')
    cod_p1 = request.form.get('cod_p1')

    # Validar existencia de pedido y producto
    pedido_exists = Pedido.query.get(cod_pe1)
    producto_exists = Producto.query.get(cod_p1)

    if not pedido_exists or not producto_exists:
        flash('Error: El pedido o producto especificado no existe.', 'danger')
        return redirect(url_for('venta.tventa'))

    try:
        nueva_venta = Venta(
            cod_ven=cod_ven,
            cod_pe1=cod_pe1,
            cod_p1=cod_p1
        )
        db.session.add(nueva_venta)
        db.session.commit()
        flash('Venta agregada exitosamente.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al agregar la venta: {e}', 'danger')

    return redirect(url_for('venta.tventa'))

@venta_bp.route('/eliminar_ventas/<string:cod_ven>')
def eliminar_ventas(cod_ven):
    try:
        v = Venta.query.get(cod_ven)
        if v:
            db.session.delete(v)
            db.session.commit()
            flash('Venta eliminada exitosamente.', 'success')
        else:
            flash('Venta no encontrada.', 'warning')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al eliminar venta: {e}', 'danger')
    return redirect(url_for('venta.tventa'))

@venta_bp.route('/editar_ventas/<string:cod_ven>')
def obtener_ventas(cod_ven):
    v = Venta.query.get(cod_ven)
    if not v:
        flash('Venta no encontrada.', 'danger')
        return redirect(url_for('venta.tventa'))
    return render_template('editventas.html', ventas=v)

@venta_bp.route('/actualizar_ventas/<string:cod_ven>', methods=['POST'])
def actualizar_ventas(cod_ven):
    try:
        v = Venta.query.get(cod_ven)
        if v:
            v.cod_pe1 = request.form.get('cod_pe1')
            v.cod_p1 = request.form.get('cod_p1')
            db.session.commit()
            flash('Venta actualizada exitosamente.', 'success')
        else:
            flash('Venta no encontrada.', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al actualizar venta: {e}', 'danger')
    return redirect(url_for('venta.tventa'))
