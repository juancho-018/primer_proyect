# 🧶 CLC - La Magie Du Crochet (Plataforma E-Commerce MVC)

> **Proyecto original creado en el 2024, retornado, refactorizado y modernizado por Juan Meneses en el 2026.**

Plataforma web de comercio electrónico y gestión empresarial (CRUD) para prendas de vestir, accesorios y productos artesanales hechos a mano en crochet. Desarrollada en **Python (Flask)** bajo el patrón de arquitectura **MVC (Modelo-Vista-Controlador)**, integrada con **MySQL**, autenticación por **JWT**, sistema de carrito de compras transaccional y servicio de envío de correos asíncronos (**Mailer SMTP**).

---

## 🌟 Características Principales

### 🏗️ 1. Arquitectura MVC & Clean Code
* **Modelos (`app/models/`)**: Mapeo ORM con **SQLAlchemy** para 7 entidades (`User`, `Cliente`, `Producto`, `Categoria`, `Proveedor`, `Pedido`, `Venta`).
* **Controladores (`app/controllers/`)**: Blueprints independientes para la separación de responsabilidades en rutas web y API RESTful.
* **Vistas (`templates/` & `base.html`)**: Plantilla maestra responsiva en Jinja2 con extensión de componentes.

### 🛡️ 2. Seguridad & Autenticación
* **Contraseñas Encriptadas**: Encriptación segura de contraseñas usando `scrypt` (`werkzeug.security`).
* **Autenticación Obligatoria Global**: Protección de rutas que exige inicio de sesión previo para navegar en el sistema.
* **Autenticación JWT para API**: Emisión y verificación de firma de tokens **JSON Web Tokens (PyJWT)** en el módulo API RESTful (`/api/v1/`).
* **Usuario Administrador Predeterminado**:
  * **Correo / Usuario**: `admin@gmail.com` | `admin`
  * **Contraseña**: `admin123`

### 🛒 3. E-Commerce & Simulación de Compras en BD
* **Catálogo Dinámico**: Carga de productos reales desde MySQL con precios, tallas, colores e imágenes de catálogo.
* **Carrito de Compras**: Gestión interactiva en el frontend con contador en vivo y persistencia.
* **Transacciones en BD**: Al finalizar la simulación de compra, se crean automáticamente registros asociados en las tablas `pedido` y `ventas` de MySQL.

### 📧 4. Servicio Mailer de Correos
* **Envío Asíncrono**: Envío de correos de bienvenida en segundo plano sin bloquear el navegador.
* **Plantilla HTML Pastel con Logo Inline**: Formato estilizado con el logo incrustado vía CID (`cid:clc_logo`).
* **Mensaje Institucional**:
  > *"Muchas gracias por ingresar nuevamente a la magia del crochet, un proyecto creado en el 2024"*

### 🎨 5. Diseño Visual & Experiencia de Usuario (UI/UX)
* **Tema Warm Pink Pastel**: Paleta de colores rosados cálidos suaves (`#fff5f7`, `#ffe4e9`, `#d53f8c`, `#702459`).
* **DataTables**: Tablas interactivas con búsqueda en tiempo real, ordenación y paginación en español.
* **SweetAlert2**: Alertas emergentes Toast, confirmaciones modales de eliminación y avisos interactivos.
* **Multimedia**: Reproductor de video promocional HTML5 (`static/video.mp4`), imágenes reales de Misión/Visión y enlaces directos a redes sociales (WhatsApp, Instagram, Facebook).

---

## 📂 Estructura del Proyecto

```text
python_clc_crud/python_clc/
│
├── app/
│   ├── __init__.py             # App Factory, configuración DB, Blueprints y Seeder Admin
│   ├── models/                 # Modelos ORM (SQLAlchemy)
│   ├── controllers/            # Controladores / Blueprints
│   └── services/               # Servicio Mailer de correos
│
├── templates/                  # Vistas Jinja2 y plantillas CRUD
├── static/                     # CSS pastel, imágenes y video promocional
├── .env                        # Variables de entorno
├── run.py                      # Punto de entrada principal
└── index.py                    # Punto de entrada de compatibilidad
```

---

## 🚀 Guía de Inicio Rápido

```powershell
cd python_clc_crud\python_clc
pip install flask flask-sqlalchemy flask-login werkzeug mysqlclient PyJWT python-dotenv
python run.py
```

Accede desde tu navegador a: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

* **Correo Administrador**: `admin@gmail.com`
* **Contraseña**: `admin123`

---

## 📜 Licencia y Créditos

&copy; **Proyecto del 2024 CLC retomado por Juan Meneses en el 2026.**
