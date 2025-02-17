import os
import requests
import time
from config import GROBID_URL, HEADERS, DATA_DIR, OUTPUT_DIR

def process_pdf(file_path):
    """Envía un PDF a Grobid y guarda la respuesta XML."""
    with open(file_path, "rb") as pdf_file:
        response = requests.post(GROBID_URL, files={"input": pdf_file}, headers=HEADERS)
    
    if response.status_code == 200:
        output_file = os.path.join(OUTPUT_DIR, os.path.basename(file_path).replace(".pdf", ".xml"))
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"Procesado: {file_path} -> {output_file}")
    else:
        print(f"Error procesando {file_path}: {response.status_code}")

def process_all_pdfs():
    """Procesa todos los PDFs en el directorio DATA_DIR."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    pdf_files = [f for f in os.listdir(DATA_DIR) if f.endswith(".pdf")]
    
    for pdf in pdf_files:
        process_pdf(os.path.join(DATA_DIR, pdf))
        time.sleep(2)  # Evitar sobrecargar Grobid
