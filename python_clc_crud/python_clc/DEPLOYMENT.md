# 🚀 Guía de Despliegue Rápido - Proyecto CLC (Magia del Crochet)

Esta guía te explica cómo desplegar la aplicación completa con **Base de Datos (MySQL)**, **Imágenes**, **Videos**, **JWT API**, **Envío de Correos Automático** y el diseño **Warm Pink Pastel** en pocos minutos.

---

## 📑 Opciones de Despliegue

1. [Opción A: Despliegue Rápido con Docker Compose (Recomendado para desarrollo/pruebas locales o VPS)](#opción-a-despliegue-rápido-con-docker-compose)
2. [Opción B: Despliegue en la Nube (Render.com / Railway)](#opción-b-despliegue-en-la-nube-render-railway)
3. [Opción C: Despliegue Tradicional en Servidor VPS (Ubuntu / Debian con Nginx + Gunicorn)](#opción-c-despliegue-en-vps-tradicional)

---

## 🐳 Opción A: Despliegue Rápido con Docker Compose

Es la forma más rápida y libre de fallos, ya que Docker inicializa automáticamente la base de datos MySQL con el script `bd_clc1.sql` e incluye todos los assets (imágenes y video).

### Prerrequisitos
- Tener instalado **Docker** y **Docker Compose**.

### Pasos:

1. Abre una terminal dentro de la carpeta del proyecto:
   ```bash
   cd python_clc_crud/python_clc
   ```

2. Ejecuta el comando de construcción e inicio:
   ```bash
   docker-compose up --build -d
   ```

3. ¡Listo! La aplicación estará corriendo en:
   - **Página Web:** `http://localhost:5000`
   - **Base de Datos MySQL:** `localhost:3306` (Usuario: `root`, Password: `rootpassword`, BD: `bd_clc1`)

4. Para ver los logs en tiempo real:
   ```bash
   docker-compose logs -f web
   ```

5. Para detener el servicio:
   ```bash
   docker-compose down
   ```

---

## ☁️ Opción B: Despliegue en la Nube (Render.com)

Render permite desplegar tanto la aplicación web Flask como la Base de Datos MySQL gratuitamente.

### Paso 1: Crear la Base de Datos MySQL en Render
1. Ve a [Render.com](https://render.com) e inicia sesión.
2. Crea un nuevo **MySQL Database** (o PostgreSQL/MariaDB).
3. Copia el **Internal Database URL** que Render genera (ej: `mysql://usuario:password@host/bd_clc1`).
4. Importa el archivo `bd_clc1.sql` a la base de datos usando DBeaver, MySQL Workbench o la CLI.

### Paso 2: Crear el Web Service en Render
1. Conecta tu repositorio de GitHub a Render.
2. Crea un **New Web Service**:
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r python_clc_crud/python_clc/requirements.txt`
   - **Start Command:** `gunicorn --bind 0.0.0.0:$PORT run:app`
3. En la sección **Environment Variables**, agrega:
   - `DATABASE_URL`: Tu URL de conexión MySQL de Render.
   - `SECRET_KEY`: `clc_secret_key_pastel_mvc_2026_super_secure_key_32bytes`
   - `MAIL_SERVER`: `smtp.gmail.com`
   - `MAIL_PORT`: `587`
   - `MAIL_USERNAME`: `camilomeneses161@gmail.com`
   - `MAIL_PASSWORD`: `ntye womk heil erbb`

4. Haz clic en **Deploy Web Service**. Render desplegará tu app con HTTPS automático.

---

## 💻 Opción C: Despliegue en VPS Tradicional (Ubuntu / Nginx)

Si posees un VPS (DigitalOcean, AWS EC2, Linode, Hetzner, etc.):

### 1. Clonar el repositorio e instalar dependencias
```bash
git clone <URL_DE_TU_REPOSITTORIO>
cd python_clc_crud/python_clc
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configurar la Base de Datos MySQL
```bash
sudo apt update && sudo apt install mysql-server -y
sudo mysql -u root -e "CREATE DATABASE bd_clc1;"
sudo mysql -u root bd_clc1 < ../bd_clc1.sql
```

### 3. Crear servicio Systemd para Gunicorn
Crea `/etc/systemd/system/clc.service`:
```ini
[Unit]
Description=Gunicorn instance to serve CLC Flask App
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/python_clc_crud/python_clc
Environment="PATH=/home/ubuntu/python_clc_crud/python_clc/venv/bin"
ExecStart=/home/ubuntu/python_clc_crud/python_clc/venv/bin/gunicorn --workers 3 --bind 127.0.0.1:5000 run:app

[Install]
WantedBy=multi-user.target
```

Inicia el servicio:
```bash
sudo systemctl start clc
sudo systemctl enable clc
```

### 4. Configurar Nginx con HTTPS (Certbot)
Crea `/etc/nginx/sites-available/clc`:
```nginx
server {
    listen 80;
    server_name tudominio.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```
Activa y aplica SSL:
```bash
sudo ln -s /etc/nginx/sites-available/clc /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
sudo certbot --nginx -d tudominio.com
```

---

## 🖼️ Verificación de Multimedia y Recursos

Todos los recursos estáticos se encuentran incluidos dentro de la estructura de la app y se empaquetan en el despliegue:
- 📹 Video en la sección 'Nosotros': `/static/video.mp4`
- 🖼️ Imágenes Misión/Visión/Logos: `/static/mision.jpeg`, `/static/vision.jpeg`, `/static/logofondono.png`
- 🎨 Estilos Pastel: `/static/css/main_pastel.css`

---

## 🔑 Credenciales por Defecto
- **Usuario Administrador:** `admin@gmail.com`
- **Contraseña:** `admin123`
