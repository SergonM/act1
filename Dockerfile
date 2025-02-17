# Usar la imagen oficial de OpenJDK 17 como base
FROM openjdk:11-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Definir variables de entorno
ENV GROBID_HOME=/app/grobid-0.8.1
ENV GROBID_PORT=8070

# Copiar Grobid al contenedor
COPY grobid-0.8.1 /app/grobid-0.8.1

# Instalar dependencias de Python
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Construir Grobid con Gradle
#WORKDIR $GROBID_HOME
#Sergio200SsRUN ./gradlew clean install

# Copiar el código fuente de Python
WORKDIR /app/src
COPY src/ /app/src/

# Exponer el puerto de Grobid
EXPOSE $GROBID_PORT

# Iniciar Grobid y luego ejecutar el script de Python
CMD java -Xms1G -Xmx4G -jar $GROBID_HOME/grobid-service/target/grobid-service-0.8.1.one-jar.jar & \
    sleep 10 && \
    python3 main.py && \
    wait
