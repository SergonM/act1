# Rutas de archivos
DATA_DIR = "data/"
OUTPUT_DIR = "output/"
GROBID_DIR = "grobid-0.8.1/"

# Configuración de Grobid
GROBID_URL = "http://localhost:8070/api/processFulltextDocument"
GROBID_ALIVE = "http://localhost:8070/api/health"
HEADERS = {"Accept": "application/xml"}

# Namespace para XML TEI
NAMESPACE = {'tei': 'http://www.tei-c.org/ns/1.0'}
