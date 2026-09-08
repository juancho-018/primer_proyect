from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.pedido import Pedido
from app.models.cliente import Cliente
from app import db
from datetime import datetime

pedido_bp = Blueprint('pedido', __name__)

@pedido_bp.route('/crearpedido')
def crearpedido():
    return render_template('crearpedido.html')

@pedido_bp.route('/tpedido', methods=['GET'])
def tpedido():
    cod_pe = request.args.get('cod_pe')
    if cod_pe:
        pedidos = Pedido.query.filter_by(cod_pe=cod_pe).all()
    else:
        pedidos = Pedido.query.all()
    return render_template('tpedido.html', pedidos=pedidos)

@pedido_bp.route('/add_pedido', methods=['POST'])
def add_pedido():
    cod_pe = request.form.get('cod_pe')
    f_pe_raw = request.form.get('f_pe')
    cant_pe = request.form.get('cant_pe')
    vt_pe = request.form.get('vt_pe')
    cod_cli1 = request.form.get('cod_cli1')

    # Verificar que el cliente existe
    cliente = Cliente.query.get(cod_cli1)
    if not cliente:
        flash('Error: El cliente no existe.', 'danger')
        return redirect(url_for('pedido.tpedido'))

    f_pe = None
    if f_pe_raw:
        try:
            f_pe = datetime.strptime(f_pe_raw, '%Y-%m-%d').date()
        except ValueError:
            f_pe = None

    try:
        nuevo_pedido = Pedido(
            cod_pe=cod_pe,
            f_pe=f_pe,
            cant_pe=cant_pe,
            vt_pe=vt_pe,
            cod_cli1=cod_cli1
        )
        db.session.add(nuevo_pedido)
        db.session.commit()
        flash('Pedido agregado exitosamente.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al agregar el pedido: {e}', 'danger')

    return redirect(url_for('pedido.tpedido'))

@pedido_bp.route('/eliminar_pedido/<string:cod_pe>')
def eliminar_pedido(cod_pe):
    try:
        pedido = Pedido.query.get(cod_pe)
        if pedido:
            db.session.delete(pedido)
            db.session.commit()
            flash('Pedido eliminado exitosamente.', 'success')
        else:
            flash('Pedido no encontrado.', 'warning')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al eliminar pedido: {e}', 'danger')
    return redirect(url_for('pedido.tpedido'))

@pedido_bp.route('/editar_pedido/<string:cod_pe>')
def obtener_pedido(cod_pe):
    pedido = Pedido.query.get(cod_pe)
    if not pedido:
        flash('Pedido no encontrado.', 'danger')
        return redirect(url_for('pedido.tpedido'))
    return render_template('editpedido.html', pedido=pedido)

@pedido_bp.route('/actualizar_pedido/<string:cod_pe>', methods=['POST'])
def actualizar_pedido(cod_pe):
    try:
        pedido = Pedido.query.get(cod_pe)
        if pedido:
            f_pe_raw = request.form.get('f_pe')
            if f_pe_raw:
                try:
                    pedido.f_pe = datetime.strptime(f_pe_raw, '%Y-%m-%d').date()
                except ValueError:
                    pass
            pedido.cant_pe = request.form.get('cant_pe')
            pedido.vt_pe = request.form.get('vt_pe')
            pedido.cod_cli1 = request.form.get('cod_cli1')
            db.session.commit()
            flash('Pedido actualizado exitosamente.', 'success')
        else:
            flash('Pedido no encontrado.', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al actualizar pedido: {e}', 'danger')
    return redirect(url_for('pedido.tpedido'))
