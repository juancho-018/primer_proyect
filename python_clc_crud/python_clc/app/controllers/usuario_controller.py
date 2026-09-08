from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user
from app.models.user import User
from app.services.mailer import send_welcome_email_async
from app import db
from werkzeug.security import generate_password_hash

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/crearusuario')
def crearusuario():
    return render_template('crearusuario.html')

@usuario_bp.route('/tusuario', methods=['GET'])
def tusuario():
    cod_us = request.args.get('cod_us')
    if cod_us:
        usuarios = User.query.filter_by(cod_us=cod_us).all()
    else:
        usuarios = User.query.all()
    return render_template('tusuario.html', usuarios=usuarios)

@usuario_bp.route('/add_usuario', methods=['POST'])
def add_usuario():
    nom_us = request.form.get('nom_us', '').strip()
    con_us = request.form.get('con_us', '').strip()
    correo_usu = request.form.get('correo_usu', '').strip()

    if User.query.filter_by(nom_us=nom_us).first():
        flash('El nombre de usuario ya existe. Por favor elige otro.', 'danger')
        return redirect(url_for('usuario.crearusuario'))

    # Obtener el siguiente ID entero disponible para la columna cod_us
    max_id = db.session.query(db.func.max(User.cod_us)).scalar()
    try:
        next_id = int(max_id) + 1 if max_id is not None else 1
    except (ValueError, TypeError):
        next_id = 1

    hashed_password = generate_password_hash(con_us)
    nuevo_usuario = User(
        cod_us=next_id,
        nom_us=nom_us,
        con_us=hashed_password,
        correo_usu=correo_usu,
        rol='usuario'
    )
    try:
        db.session.add(nuevo_usuario)
        db.session.commit()

        # Disparar Mailer asíncrono
        send_welcome_email_async(correo_usu, nom_us)

        flash('¡Usuario registrado con éxito! Muchas gracias por ingresar a la magia del crochet, un proyecto creado en el 2024.', 'success')

        if current_user.is_authenticated:
            return redirect(url_for('usuario.tusuario'))
        else:
            return redirect(url_for('auth.login'))

    except Exception as e:
        db.session.rollback()
        flash(f'Error al registrar usuario: {e}', 'danger')
        return redirect(url_for('usuario.crearusuario'))

@usuario_bp.route('/eliminar_usuario/<string:cod_us>')
def eliminar_usuario(cod_us):
    try:
        usuario = User.query.get(cod_us)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            flash('Usuario eliminado exitosamente.', 'success')
        else:
            flash('Usuario no encontrado.', 'warning')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al eliminar usuario: {e}', 'danger')
    return redirect(url_for('usuario.tusuario'))

@usuario_bp.route('/editar_usuario/<string:cod_us>')
def obtener_usuario(cod_us):
    usuario = User.query.get(cod_us)
    if not usuario:
        flash('Usuario no encontrado.', 'danger')
        return redirect(url_for('usuario.tusuario'))
    return render_template('editusuario.html', usuario=usuario)

@usuario_bp.route('/actualizar_usuario/<string:cod_us>', methods=['POST'])
def actualizar_usuario(cod_us):
    try:
        usuario = User.query.get(cod_us)
        if usuario:
            usuario.nom_us = request.form.get('nom_us')
            usuario.correo_usu = request.form.get('correo_usu')
            nueva_clave = request.form.get('con_us')
            if nueva_clave:
                usuario.con_us = generate_password_hash(nueva_clave)
            db.session.commit()
            flash('Usuario actualizado exitosamente.', 'success')
        else:
            flash('Usuario no encontrado.', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al actualizar usuario: {e}', 'danger')
    return redirect(url_for('usuario.tusuario'))
