# 🧶 CLC - La Magie Du Crochet (Plataforma E-Commerce MVC)

> **Proyecto original creado en el 2024, retornado, refactorizado y modernizado por Juan Meneses en el 2026.**

![CLC E-Commerce](static/img/logofondono.png)

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
│   │   ├── user.py
│   │   ├── cliente.py
│   │   ├── producto.py
│   │   ├── categoria.py
│   │   ├── proveedor.py
│   │   ├── pedido.py
│   │   └── venta.py
│   │
│   ├── controllers/            # Controladores / Blueprints
│   │   ├── main_controller.py       # Vistas públicas
│   │   ├── auth_controller.py       # Login y Logout
│   │   ├── cliente_controller.py    # CRUD Clientes
│   │   ├── usuario_controller.py    # CRUD Usuarios
│   │   ├── producto_controller.py   # CRUD Productos
│   │   ├── categoria_controller.py  # CRUD Categorías
│   │   ├── proveedor_controller.py  # CRUD Proveedores
│   │   ├── pedido_controller.py     # CRUD Pedidos
│   │   ├── venta_controller.py      # CRUD Ventas
│   │   ├── api_controller.py        # API RESTful + JWT
│   │   └── compra_controller.py     # Carrito & Transacciones en BD
│   │
│   └── services/               # Servicios auxiliares
│       └── mailer.py           # Servicio asíncrono SMTP de correos
│
├── templates/                  # Vistas Jinja2
│   ├── base.html               # Layout base pastel con DataTables y SweetAlert2
│   ├── inicio.html
│   ├── login.html
│   ├── productos.html
│   ├── seccion.html
│   ├── nosotros.html           # Página multimedia con video e imágenes
│   ├── inicioadmin.html        # Dashboard Administrador
│   └── [ Formularios CRUD ]    # Vistas de creación y edición
│
├── static/                     # Recursos Estáticos
│   ├── css/
│   │   └── main_pastel.css     # Sistema de diseño rosado cálido pastel
│   ├── img/                    # Imágenes de catálogo y marcas
│   └── video.mp4               # Video promocional oficial
│
├── .env                        # Variables de entorno (SMTP y BD)
├── .env.example                # Plantilla de variables de entorno
├── run.py                      # Punto de entrada principal
└── index.py                    # Punto de entrada de compatibilidad
```

---

## 🛠️ Requisitos de Instalación

1. **Python 3.10+**
2. **Servidor MySQL / MariaDB** (Laragon o XAMPP con el puerto 3306 activo).
3. Base de datos MySQL nombrada `bd_clc1` con el script de datos [bd_clc1.sql](file:///c:/Users/jcami/Downloads/Python_clc%20%281%29~/python_clc_crud/bd_clc1.sql).

---

## 🚀 Guía de Inicio Rápido

### 1. Clonar / Navegar al Proyecto
```powershell
cd python_clc_crud\python_clc
```

### 2. Instalar Dependencias de Python
```powershell
pip install flask flask-sqlalchemy flask-login werkzeug mysqlclient PyJWT python-dotenv
```

### 3. Configurar Variables de Entorno (`.env`)
Copia el archivo `.env.example` como `.env` y configura tus credenciales SMTP de Gmail (si deseas recepción de correos en bandeja real):

```env
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=tu_correo@gmail.com
MAIL_PASSWORD=tu_contraseña_de_aplicación_google

DATABASE_URL=mysql://root:@localhost/bd_clc1
```

### 4. Ejecutar el Servidor
```powershell
python run.py
```

Accede desde tu navegador a: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 🔑 Credenciales de Acceso

* **Usuario Administrador**:
  * **Correo**: `admin@gmail.com`
  * **Contraseña**: `admin123`

---

## 🔗 Endpoints API RESTful (JWT)

| Método | Endpoint | Descripción | Requiere Token |
| :--- | :--- | :--- | :--- |
| `POST` | `/api/v1/auth/login` | Autentica usuario y emite Token JWT | No |
| `GET` | `/api/v1/productos` | Obtiene el catálogo completo en JSON | No |
| `GET` | `/api/v1/pedidos` | Obtiene los pedidos registrados | Sí (`Bearer <token>`) |
| `GET` | `/api/v1/user/profile` | Obtiene la información del usuario autenticado | Sí (`Bearer <token>`) |

---

## 📜 Licencia y Créditos

&copy; **Proyecto del 2024 CLC retomado por Juan Meneses en el 2026.**  
*Todos los derechos reservados. Desarrollado con pasión por el arte del tejido a mano en crochet.*
