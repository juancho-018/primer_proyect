FROM python:3.11-slim

# Instalar paquetes del sistema necesarios para MySQL C connector
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiar e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código del proyecto
COPY . .

# Puerto expuesto
EXPOSE 5000

# Comando de inicio con Gunicorn (servidor WSGI de producción)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "3", "run:app"]
