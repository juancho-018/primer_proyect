from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.cliente import Cliente
from app import db
from datetime import datetime

cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route('/fcliente')
def fcliente():
    return render_template('fcliente.html')

@cliente_bp.route('/tcliente', methods=['GET', 'POST'])
def tcliente():
    cod_cli = request.args.get('cod_cli')
    if cod_cli:
        clientes = Cliente.query.filter_by(cod_cli=cod_cli).all()
    else:
        clientes = Cliente.query.all()
    return render_template('tcliente.html', clientes=clientes)

@cliente_bp.route('/add_cliente', methods=['POST'])
def add_cliente():
    try:
        cod_cli = request.form.get('cod_cli')
        nom_cli = request.form.get('nom_cli')
        corr_cli = request.form.get('corr_cli')
        sexo_cli = request.form.get('sexo_cli')
        direc_cli = request.form.get('direc_cli')
        tipoid_cli = request.form.get('tipoid_cli')
        id_cli = request.form.get('id_cli')
        fn_cli_raw = request.form.get('fn_cli')

        fn_cli = None
        if fn_cli_raw:
            try:
                fn_cli = datetime.strptime(fn_cli_raw, '%Y-%m-%d').date()
            except ValueError:
                fn_cli = None

        nuevo_cliente = Cliente(
            cod_cli=cod_cli,
            nom_cli=nom_cli,
            corr_cli=corr_cli,
            sexo_cli=sexo_cli,
            direc_cli=direc_cli,
            tipoid_cli=tipoid_cli,
            id_cli=id_cli,
            fn_cli=fn_cli
        )
        db.session.add(nuevo_cliente)
        db.session.commit()
        flash('Cliente registrado exitosamente.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al registrar cliente: {e}', 'danger')

    return redirect(url_for('cliente.tcliente'))

@cliente_bp.route('/eliminar_cliente/<string:cod_cli>')
def eliminar_cliente(cod_cli):
    try:
        cliente = Cliente.query.get(cod_cli)
        if cliente:
            db.session.delete(cliente)
            db.session.commit()
            flash('Cliente eliminado exitosamente.', 'success')
        else:
            flash('Cliente no encontrado.', 'warning')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al eliminar cliente: {e}', 'danger')
    return redirect(url_for('cliente.tcliente'))

@cliente_bp.route('/editar_cliente/<string:cod_cli>')
def obtener_cliente(cod_cli):
    cliente = Cliente.query.get(cod_cli)
    if not cliente:
        flash('Cliente no encontrado.', 'danger')
        return redirect(url_for('cliente.tcliente'))
    return render_template('feditcliente.html', cliente=cliente)

@cliente_bp.route('/actualizar_cliente/<string:cod_cli>', methods=['POST'])
def actualizar_cliente(cod_cli):
    try:
        cliente = Cliente.query.get(cod_cli)
        if cliente:
            cliente.nom_cli = request.form.get('nom_cli')
            cliente.corr_cli = request.form.get('corr_cli')
            cliente.sexo_cli = request.form.get('sexo_cli')
            cliente.direc_cli = request.form.get('direc_cli')
            cliente.tipoid_cli = request.form.get('tipoid_cli')
            cliente.id_cli = request.form.get('id_cli')
            
            fn_cli_raw = request.form.get('fn_cli')
            if fn_cli_raw:
                try:
                    cliente.fn_cli = datetime.strptime(fn_cli_raw, '%Y-%m-%d').date()
                except ValueError:
                    pass

            db.session.commit()
            flash('Cliente actualizado exitosamente.', 'success')
        else:
            flash('Cliente no encontrado.', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al actualizar cliente: {e}', 'danger')

    return redirect(url_for('cliente.tcliente'))
