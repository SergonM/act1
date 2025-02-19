# 📝 Análisis de Artículos Científicos con Grobid  

Este repositorio contiene un pipeline de procesamiento de artículos científicos en **PDF**, utilizando **Grobid** para la extracción de datos y herramientas de visualización en **Python**.  

## 🚀 Objetivos del Proyecto  
El programa realiza los siguientes análisis sobre **10 artículos de acceso abierto**:  
1. **📌 Nube de palabras** basada en los resúmenes (**abstracts**).  
2. **📊 Gráfico** con el número de figuras por artículo.  
3. **🔗 Lista de enlaces** extraídos de cada documento.  

---

## 📁 Estructura del Proyecto  
```sh
├── data/                  # 📂 PDFs de entrada para su procesamiento  
├── output/                # 📂 Resultados generados (XMLs, gráficos, JSONs)  
│   ├── wordcloud.png      # 📊 Nube de palabras basada en los abstracts  
│   ├── figures_per_paper.png # 📈 Número de figuras por artículo  
│   ├── links_per_paper.json  # 🔗 Lista de enlaces extraídos  
├── src/                   # 📂 Código fuente del pipeline  
│   ├── config.py          # ⚙️ Configuración del entorno y rutas  
│   ├── extraction.py      # 🔍 Extracción de abstracts, figuras y enlaces  
│   ├── process.py         # 🛠️ Envío de PDFs a Grobid y procesamiento  
│   ├── visualization.py   # 📊 Generación de gráficos y visualizaciones  
│   ├── main.py            # 🚀 Script principal del programa  
├── Dockerfile             # 🐳 Configuración de contenedor para la aplicación  
├── docker-compose.yml     # 🐳 Configuración de servicios (Grobid + App)  
├── requirements.txt       # 📦 Dependencias necesarias  
├── rationale.md           # 📝 Validación de los resultados obtenidos  
├── LICENSE                # ⚖️ Licencia del proyecto  
└── README.md              # 📖 Documentación del repositorio  
```

---

## 🛠️ Instalación y Ejecución con Docker Compose  

Este método inicia **Grobid y la aplicación** en contenedores separados, lo que facilita la ejecución sin necesidad de instalar dependencias manualmente.  

### 1️⃣ Clonar el repositorio  
```sh
git clone https://github.com/SergonM/act1.git
cd act1
```

### 2️⃣ Agregar los artículos en la carpeta data/

    En la carpeta data/ se encuentran 10 artículos en formato PDF por defecto.
    Puedes reemplazarlos o agregar nuevos documentos en esta carpeta.

### 3️⃣ Iniciar los servicios con Docker Compose
```sh
docker-compose up -d
```

🔹 Esto iniciará:  
- **Grobid** en `http://localhost:8070`  
- **La aplicación**, que interactúa con Grobid y procesa los artículos  



📌 **Notas:**  
- Si Grobid no responde, verifica que el servicio esté activo en `http://localhost:8070/api/isalive`.  
- Para detener los servicios:  
  ```sh
  docker-compose down
  ```

---

## 📊 Resultados Esperados  
Después de ejecutar el análisis, los resultados estarán en la carpeta `output/`:

| Archivo | Descripción |
|---------|------------|
| **`wordcloud.png`** | Nube de palabras con los términos más frecuentes en los resúmenes |
| **`figures_per_paper.png`** | Gráfico con la cantidad de figuras por artículo |
| **`links_per_paper.json`** | Lista de enlaces externos extraídos de los artículos |

---

## 📄 Validación de Resultados  
Para más detalles sobre la validación de los resultados, consulta el archivo [`rationale.md`](rationale.md).  

---

## 📜 Licencia
Este proyecto está bajo la licencia **GNU General Public License v3.0**.  

---

### 🔗 Referencias  
- [Grobid GitHub](https://github.com/kermitt2/grobid)  
- [Documentación de WordCloud](https://github.com/amueller/word_cloud)  
- [Docker Compose](https://docs.docker.com/compose/)  
