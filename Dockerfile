# Usa una imagen base de Python
FROM python:3.11-slim
# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requerimientos al contenedor
COPY requirements.txt .

# Instala las dependencias desde el archivo de requerimientos
RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto para ejecutar el contenedor
CMD ["python","main.py"]