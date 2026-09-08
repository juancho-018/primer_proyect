from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.proveedor import Proveedor
from app import db

proveedor_bp = Blueprint('proveedor', __name__)

@proveedor_bp.route('/crearproveedor')
def crearproveedor():
    return render_template('crearproveedor.html')

@proveedor_bp.route('/tproveedor', methods=['GET'])
def tproveedor():
    cod_prov = request.args.get('cod_prov')
    if cod_prov:
        proveedores = Proveedor.query.filter_by(cod_prov=cod_prov).all()
    else:
        proveedores = Proveedor.query.all()
    return render_template('tproveedor.html', proveedores=proveedores)

@proveedor_bp.route('/add_proveedor', methods=['POST'])
def add_proveedor():
    try:
        nuevo_prov = Proveedor(
            cod_prov=request.form.get('cod_prov'),
            nom_prov=request.form.get('nom_prov'),
            tel_prov=request.form.get('tel_prov'),
            trans_prov=request.form.get('trans_prov', ''),
            edad_prov=request.form.get('edad_prov') or None,
            direc_prov=request.form.get('direc_prov'),
            sexo_prov=request.form.get('sexo_prov'),
            tipoid_prov=request.form.get('tipoid_prov'),
            id_prov=request.form.get('id_prov') or None,
            corr_prov=request.form.get('corr_prov')
        )
        db.session.add(nuevo_prov)
        db.session.commit()
        flash('Proveedor agregado exitosamente.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al agregar proveedor: {e}', 'danger')
    return redirect(url_for('proveedor.tproveedor'))

@proveedor_bp.route('/eliminar_proveedor/<string:cod_prov>')
def eliminar_proveedor(cod_prov):
    try:
        prov = Proveedor.query.get(cod_prov)
        if prov:
            db.session.delete(prov)
            db.session.commit()
            flash('Proveedor eliminado exitosamente.', 'success')
        else:
            flash('Proveedor no encontrado.', 'warning')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al eliminar proveedor: {e}', 'danger')
    return redirect(url_for('proveedor.tproveedor'))

@proveedor_bp.route('/editar_proveedor/<string:cod_prov>')
def obtener_proveedor(cod_prov):
    prov = Proveedor.query.get(cod_prov)
    if not prov:
        flash('Proveedor no encontrado.', 'danger')
        return redirect(url_for('proveedor.tproveedor'))
    return render_template('editproveedor.html', proveedor=prov)

@proveedor_bp.route('/actualizar_proveedor/<string:cod_prov>', methods=['POST'])
def actualizar_proveedor(cod_prov):
    try:
        prov = Proveedor.query.get(cod_prov)
        if prov:
            prov.nom_prov = request.form.get('nom_prov')
            prov.tel_prov = request.form.get('tel_prov')
            prov.trans_prov = request.form.get('trans_prov')
            prov.edad_prov = request.form.get('edad_prov') or None
            prov.direc_prov = request.form.get('direc_prov')
            prov.sexo_prov = request.form.get('sexo_prov')
            prov.tipoid_prov = request.form.get('tipoid_prov')
            prov.id_prov = request.form.get('id_prov') or None
            prov.corr_prov = request.form.get('corr_prov')
            db.session.commit()
            flash('Proveedor actualizado exitosamente.', 'success')
        else:
            flash('Proveedor no encontrado.', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al actualizar proveedor: {e}', 'danger')
    return redirect(url_for('proveedor.tproveedor'))
