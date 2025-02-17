import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re
from extraction import extract_abstracts, count_figures
from config import OUTPUT_DIR

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

def plot_figures():
    """Genera un gráfico del número de figuras en cada artículo."""
    figure_counts = count_figures()
    
    plt.figure(figsize=(10, 5))
    plt.bar(figure_counts.keys(), figure_counts.values(), color='blue')
    plt.xlabel("Artículo")
    plt.ylabel("Número de Figuras")
    plt.title("Número de Figuras por Artículo")
    plt.xticks(rotation=45, ha='right')
    plt.savefig(os.path.join(OUTPUT_DIR, "figures_per_paper.png"))
    print("Gráfico generado: output/figures_per_paper.png")
