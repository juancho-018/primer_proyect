from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.user import User
from app.services.mailer import send_welcome_email_async
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
@auth_bp.route('/ingresar', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        identificador = request.form.get('nom_us', '').strip()
        con_us = request.form.get('con_us', '').strip()

        # Buscar por correo o por nombre de usuario
        user = User.query.filter(
            (User.correo_usu == identificador) | (User.nom_us == identificador)
        ).first()

        if user and user.check_password(con_us):
            login_user(user)
            
            # Obtener el correo del usuario que acaba de iniciar sesión
            correo_destino = user.correo_usu.strip() if (user.correo_usu and '@' in user.correo_usu) else None
            
            # Si inició sesión ingresando su correo en el formulario, guardarlo en su perfil
            if not correo_destino and '@' in identificador:
                correo_destino = identificador
                try:
                    user.correo_usu = identificador
                    db.session.commit()
                except Exception:
                    db.session.rollback()

            # Enviar el correo de bienvenida EXCLUSIVAMENTE al usuario que inició sesión
            if correo_destino:
                send_welcome_email_async(correo_destino, user.nom_us)
            
            flash(f"¡Muchas gracias por ingresar nuevamente a la magia del crochet, un proyecto creado en el 2024!", "success")
            if getattr(user, 'rol', None) == 'admin':
                return redirect(url_for('main.inicioadmin'))
            return redirect(url_for('main.inicio'))
        else:
            flash("Nombre de usuario / correo o contraseña incorrectos.", "danger")
            return redirect(url_for('auth.login'))

    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Has cerrado sesión correctamente.", "info")
    return redirect(url_for('auth.login'))
