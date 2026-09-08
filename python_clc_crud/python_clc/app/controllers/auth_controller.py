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
            # Disparar Mailer asíncrono
            send_welcome_email_async(user.correo_usu, user.nom_us)
            
            flash(f"¡Muchas gracias por ingresar nuevamente a la magia del crochet, un proyecto creado en el 2024!", "success")
            if user.rol == 'admin' or user.nom_us == 'admin' or user.correo_usu == 'admin@gmail.com':
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
