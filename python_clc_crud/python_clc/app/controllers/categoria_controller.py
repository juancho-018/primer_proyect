from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.categoria import Categoria
from app import db

categoria_bp = Blueprint('categoria', __name__)

@categoria_bp.route('/crearcategoria')
def crearcategoria():
    return render_template('crearcategoria.html')

@categoria_bp.route('/tcategoria', methods=['GET'])
def tcategoria():
    cod_c = request.args.get('cod_c')
    if cod_c:
        categorias = Categoria.query.filter_by(cod_c=cod_c).all()
    else:
        categorias = Categoria.query.all()
    return render_template('tcategoria.html', categorias=categorias)

@categoria_bp.route('/add_categoria', methods=['POST'])
def add_categoria():
    try:
        nueva_cat = Categoria(
            cod_c=request.form.get('cod_c'),
            nom_c=request.form.get('nom_c')
        )
        db.session.add(nueva_cat)
        db.session.commit()
        flash('Categoría agregada exitosamente.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al agregar categoría: {e}', 'danger')
    return redirect(url_for('categoria.tcategoria'))

@categoria_bp.route('/eliminar_categoria/<string:cod_c>')
def eliminar_categoria(cod_c):
    try:
        cat = Categoria.query.get(cod_c)
        if cat:
            db.session.delete(cat)
            db.session.commit()
            flash('Categoría eliminada exitosamente.', 'success')
        else:
            flash('Categoría no encontrada.', 'warning')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al eliminar categoría: {e}', 'danger')
    return redirect(url_for('categoria.tcategoria'))

@categoria_bp.route('/editar_categoria/<string:cod_c>')
def obtener_categoria(cod_c):
    cat = Categoria.query.get(cod_c)
    if not cat:
        flash('Categoría no encontrada.', 'danger')
        return redirect(url_for('categoria.tcategoria'))
    return render_template('editcategoria.html', categoria=cat)

@categoria_bp.route('/actualizar_categoria/<string:cod_c>', methods=['POST'])
def actualizar_categoria(cod_c):
    try:
        cat = Categoria.query.get(cod_c)
        if cat:
            cat.nom_c = request.form.get('nom_c')
            db.session.commit()
            flash('Categoría actualizada exitosamente.', 'success')
        else:
            flash('Categoría no encontrada.', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al actualizar categoría: {e}', 'danger')
    return redirect(url_for('categoria.tcategoria'))
