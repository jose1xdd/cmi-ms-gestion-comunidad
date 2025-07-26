# Usa la imagen base de Python 3.11 Slim
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt desde el directorio anterior
COPY ../requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . .

# Expone el puerto en el que FastAPI correrá
EXPOSE 8081

# Define el comando para ejecutar la aplicación
CMD ["python", "main.py"]
