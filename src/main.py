import time
import requests
from process import process_all_pdfs
from extraction import extract_links
from visualization import generate_wordcloud, plot_figures
from config import GROBID_URL, GROBID_ALIVE

def check_grobid_alive():
    """Verifica si el servicio Grobid está activo antes de ejecutar cualquier tarea."""
    print("Verificando si Grobid está activo...")
    while True:
        try:
            response = requests.get(GROBID_ALIVE)
            if response.status_code == 200:
                print("Grobid está activo. Continuando con el proceso...")
                break
            else:
                print("Grobid no está disponible. Esperando...")
        except requests.exceptions.RequestException:
            print(GROBID_ALIVE)
            print("No se pudo conectar con Grobid. Reintentando en 5 segundos...")
        time.sleep(5)

def main_menu():
    """Menú principal para ejecutar opciones del pipeline."""
    while True:
        print("\nSeleccione una opción:")
        print("1. Procesar PDFs con Grobid")
        print("2. Generar visualizaciones")
        print("3. Extraer enlaces")
        print("4. Salir")
        
        choice = input("Ingrese su elección: ")
        
        if choice == "1":
            process_all_pdfs()
        elif choice == "2":
            generate_wordcloud()
            plot_figures()
        elif choice == "3":
            extract_links()
        elif choice == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    check_grobid_alive()
    #main_menu()
    process_all_pdfs()
    generate_wordcloud()
    plot_figures()
    extract_links()
    print("Saliendo del programa.")
