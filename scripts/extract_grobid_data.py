import os
import requests
import time
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re
import json

GROBID_URL = "http://localhost:8070/api/processFulltextDocument"
DATA_DIR = "data/"
OUTPUT_DIR = "output/"
HEADERS = {"Accept": "application/xml"}
NAMESPACE = {"tei": "http://www.tei-c.org/ns/1.0"}  # Define el namespace

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



def extract_abstracts():
    """Extrae los abstracts de los archivos XML procesados."""
    abstracts = []

    for file in os.listdir(OUTPUT_DIR):
        if file.endswith(".xml"):
            tree = ET.parse(os.path.join(OUTPUT_DIR, file))
            root = tree.getroot()

            # Busca el abstract dentro del namespace
            for abstract in root.findall(".//tei:abstract//tei:p", namespaces=NAMESPACE):
                if abstract.text:
                    abstracts.append(abstract.text.strip())
                    print(abstract.text.strip())

    return abstracts

def generate_wordcloud():
    """Genera una nube de palabras basada en los abstracts."""
    abstracts = extract_abstracts()
    text = " ".join(abstracts)
    text = re.sub(r'[^a-zA-Z ]', '', text)  # Filtra caracteres no alfabéticos
    
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(os.path.join(OUTPUT_DIR, "wordcloud.png"))
    print("Nube de palabras generada: output/wordcloud.png")


def count_figures():
    """Cuenta el número de figuras en cada artículo y genera una gráfica."""
    figure_counts = {}
    for file in os.listdir(OUTPUT_DIR):
        if file.endswith(".xml"):
            tree = ET.parse(os.path.join(OUTPUT_DIR, file))
            root = tree.getroot()
            figures = root.findall(".//tei:figure", NAMESPACE)
            figure_counts[file.replace(".xml", "")] = len(figures)
    
    # Generar gráfico
    plt.figure(figsize=(10, 5))
    plt.bar(figure_counts.keys(), figure_counts.values(), color='blue')
    plt.xlabel("Artículo")
    plt.ylabel("Número de Figuras")
    plt.title("Número de Figuras por Artículo")
    plt.xticks(rotation=45, ha='right')
    plt.savefig(os.path.join(OUTPUT_DIR, "figures_per_paper.png"))
    print("Gráfico generado: output/figures_per_paper.png")

def extract_links():
    """Extrae enlaces externos de los artículos y los asocia a su contexto."""
    links_data = {}
    for file in os.listdir(OUTPUT_DIR):
        if file.endswith(".xml"):
            tree = ET.parse(os.path.join(OUTPUT_DIR, file))
            root = tree.getroot()
            
            links_info = []
            for ref in root.findall(".//tei:ref", NAMESPACE):
                link = ref.get("target")
                if link and not link.startswith("#"):
                    context = ref.text if ref.text else "No contexto disponible"
                    links_info.append({"link": link, "context": context})
            
            links_data[file.replace(".xml", "")] = links_info
    
    output_file = os.path.join(OUTPUT_DIR, "links_per_paper.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(links_data, f, indent=4)
    print(f"Lista de enlaces guardada en: {output_file}")

if __name__ == "__main__":
    process_all_pdfs()
    generate_wordcloud()
    count_figures()
    extract_links()