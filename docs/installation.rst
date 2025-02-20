Instalación y Configuración
===========================

Este método inicia **Grobid y la aplicación** en contenedores separados, lo que facilita la ejecución sin instalar dependencias manualmente.

1️⃣ **Clonar el repositorio**
--------------------------------
.. code-block:: bash

   git clone https://github.com/SergonM/act1.git
   cd act1

2️⃣ **Agregar los artículos en la carpeta `data/`**
---------------------------------------------------
- En la carpeta `data/` hay 10 artículos en PDF por defecto.
- Puedes reemplazarlos o agregar nuevos documentos en esta carpeta.

3️⃣ **Iniciar los servicios con Docker Compose**
-------------------------------------------------
Ejecuta el siguiente comando para levantar los servicios:

.. code-block:: bash

   docker-compose up -d

🔹 Esto iniciará:  
- **Grobid** en `http://localhost:8070`  
- **La aplicación**, que interactúa con Grobid y procesa los artículos  

📌 **Notas**:
- Si Grobid no responde, verifica que el servicio esté activo en `http://localhost:8070/api/isalive`.
- Para detener los servicios:
.. code-block:: bash

   docker-compose down




