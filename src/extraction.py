import os
import xml.etree.ElementTree as ET
import json
from config import NAMESPACE, OUTPUT_DIR

def extract_abstracts():
    """Extrae los abstracts de los archivos XML procesados."""
    abstracts = []
    for file in os.listdir(OUTPUT_DIR):
        if file.endswith(".xml"):
            tree = ET.parse(os.path.join(OUTPUT_DIR, file))
            root = tree.getroot()
            for abstract in root.findall(".//tei:abstract//tei:p", NAMESPACE):
                if abstract.text:
                    abstracts.append(abstract.text.strip())
    return abstracts

def count_figures():
    """Cuenta el número de figuras en cada artículo."""
    figure_counts = {}
    for file in os.listdir(OUTPUT_DIR):
        if file.endswith(".xml"):
            tree = ET.parse(os.path.join(OUTPUT_DIR, file))
            root = tree.getroot()
            figures = root.findall(".//tei:figure", NAMESPACE)
            figure_counts[file.replace(".xml", "")] = len(figures)
    return figure_counts

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
