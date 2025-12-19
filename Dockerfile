# Imagen base con Python
FROM python:3.11-slim

# Configurar entorno
ENV PYTHONUNBUFFERED=1

# Crear carpeta de trabajo
WORKDIR /app

# Copiar los archivos de dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código del proyecto
COPY . .

# Exponer el puerto
EXPOSE 5000

# Ejecutar usando gunicorn (más estable que el server de Flask)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
