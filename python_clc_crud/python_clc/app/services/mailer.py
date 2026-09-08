import os
import smtplib
import threading
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def send_welcome_email_async(destinatario, usuario):
    try:
        _send_email_thread(destinatario, usuario)
    except Exception as e:
        print(f"[Error Mailer Directo]: {e}")

def _send_email_thread(destinatario, usuario):
    asunto = "¡Bienvenido a la magia del crochet! - CLC"
    mensaje_texto = "Muchas gracias por ingresar nuevamente a la magia del crochet, un proyecto creado en el 2024."

    smtp_server = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    smtp_port = int(os.environ.get('MAIL_PORT', 587))
    sender_email = os.environ.get('MAIL_USERNAME', 'camilomeneses161@gmail.com')
    sender_password = os.environ.get('MAIL_PASSWORD', 'ntye womk heil erbb')

    target_recipient = destinatario.strip() if (destinatario and '@' in destinatario) else sender_email

    msg = MIMEMultipart('related')
    msg['From'] = f"CLC Crochet <{sender_email}>"
    msg['To'] = target_recipient
    msg['Subject'] = asunto

    # Plantilla HTML Pastel Rosado Cálido con Logo
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{ font-family: 'Plus Jakarta Sans', Arial, -apple-system, sans-serif; background-color: #fff5f7; margin: 0; padding: 20px; }}
            .container {{ background-color: #ffffff; border-radius: 20px; border: 1.5px solid #fbb6ce; max-width: 580px; margin: 0 auto; padding: 2.5rem 2rem; box-shadow: 0 10px 25px rgba(213, 63, 140, 0.1); text-align: center; }}
            .header-logo {{ max-height: 75px; width: auto; margin-bottom: 1rem; display: block; margin-left: auto; margin-right: auto; }}
            .badge {{ background-color: #ffe4e9; color: #d53f8c; padding: 0.4rem 1.2rem; border-radius: 20px; font-weight: 600; font-size: 0.85rem; display: inline-block; margin-bottom: 1rem; }}
            .title {{ color: #702459; font-size: 1.8rem; font-weight: 700; margin: 0 0 1rem 0; font-family: 'Outfit', sans-serif; }}
            .greeting {{ font-size: 1.1rem; color: #2d3748; margin-bottom: 1.5rem; }}
            .message-card {{ background: linear-gradient(135deg, #fff0f3 0%, #ffe4e9 100%); border-radius: 16px; border-left: 5px solid #d53f8c; padding: 1.8rem; margin: 1.5rem 0; text-align: center; }}
            .message-text {{ font-size: 1.15rem; color: #702459; margin: 0; font-weight: 700; line-height: 1.6; }}
            .divider {{ height: 1px; background-color: #ffe4e9; margin: 2rem 0; }}
            .footer {{ font-size: 0.88rem; color: #718096; line-height: 1.5; }}
        </style>
    </head>
    <body>
        <div class="container">
            <!-- Logo incrustado en línea mediante CID -->
            <img src="cid:clc_logo" alt="CLC Logo" class="header-logo">
            
            <div class="badge">La Magie Du Crochet</div>
            
            <h1 class="title">¡Hola, {usuario}!</h1>
            <p class="greeting">Nos alegra tenerte nuevamente en nuestra plataforma artesanal.</p>
            
            <div class="message-card">
                <p class="message-text">
                    "Muchas gracias por ingresar nuevamente a la magia del crochet, un proyecto creado en el 2024"
                </p>
            </div>
            
            <div class="divider"></div>
            
            <div class="footer">
                <p>&copy; Proyecto del 2024 CLC retomado por Juan Meneses en el 2026</p>
                <p style="font-size: 0.8rem; color: #a0aec0;">Tejidos a mano con amor y dedicación.</p>
            </div>
        </div>
    </body>
    </html>
    """

    msg_alternative = MIMEMultipart('alternative')
    msg.attach(msg_alternative)
    msg_alternative.attach(MIMEText(mensaje_texto, 'plain'))
    msg_alternative.attach(MIMEText(html_content, 'html'))

    # Adjuntar la imagen del logo como recurso inline (CID)
    logo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'static', 'img', 'logofondono.png'))
    if os.path.exists(logo_path):
        try:
            with open(logo_path, 'rb') as f:
                logo_img = MIMEImage(f.read())
                logo_img.add_header('Content-ID', '<clc_logo>')
                logo_img.add_header('Content-Disposition', 'inline', filename='logofondono.png')
                msg.attach(logo_img)
        except Exception as img_err:
            print(f"[Aviso Logo Mailer]: No se pudo adjuntar logo inline: {img_err}")

    print(f"\n========================================================")
    print(f" [Mailer CLC]: Enviando correo a -> {msg['To']}")
    print(f" Estilo: Pastel Rosado Calido con Logo Inline")
    print(f"========================================================\n")

    clean_password = sender_password.replace(" ", "").strip()

    # Intento de envío real con SSL en puerto 465 primero (óptimo para Render/Nube) y fallback en 587
    if clean_password:
        try:
            server = smtplib.SMTP_SSL(smtp_server, 465, timeout=10)
            server.login(sender_email, clean_password)
            server.send_message(msg)
            server.quit()
            print(f" -> ¡Correo SMTP enviado con éxito vía SSL (Puerto 465) a {target_recipient}!")
        except Exception as e465:
            print(f" -> [Aviso Puerto 465 SSL]: {e465}. Reintentando vía TLS (Puerto 587)...")
            try:
                server = smtplib.SMTP(smtp_server, 587, timeout=10)
                server.starttls()
                server.login(sender_email, clean_password)
                server.send_message(msg)
                server.quit()
                print(f" -> ¡Correo SMTP enviado con éxito vía TLS (Puerto 587) a {target_recipient}!")
            except Exception as e587:
                print(f" -> [ERROR CRÍTICO SMTP MAILER]: No se pudo entregar por 465 ni 587: {e587}")
