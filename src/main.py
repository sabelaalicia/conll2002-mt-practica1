from modules.utils import extract_plain_text, text_to_iob, combine
import spacy

print("Iniciando procesamiento")
print("=" * 50)

# Convertimos y guardamos el texto plano


print("Extrayendo texto plano desde TESTB-ESP.txt...")
plain_text = extract_plain_text('../data/raw/TESTB-ESP.txt')
with open('../data/processed/plain_text.txt', 'w', encoding='utf-8') as out_file:
    out_file.write(plain_text)
print("Texto plano extraído y guardado en 'data/processed/plain_text.txt'")



print("\n Configurando modelo de SpaCy...")
##Customizamos la tockenización y cargamos un modelo preentrenado

from spacy.tokenizer import Tokenizer
nlp = spacy.load("es_core_news_sm")
nlp.tokenizer=Tokenizer(nlp.vocab)
print(" Modelo es_core_news_sm cargado correctamente")

# Leer el texto desde un archivo
with open("../data/processed/plain_text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Procesar el texto con SpaCy
print("Procesando texto con SpaCy...")
doc = nlp(text)
print(f"Procesamiento completado: {len(doc)} tokens analizados")

print("Convirtiendo a formato IOB...")
spacy_otput=text_to_iob(doc)
with open('../data/processed/pred_labels.txt', 'w', encoding='utf-8') as out_file:
    out_file.write(spacy_otput)
print("Etiquetas predichas guardadas en 'data/processed/pred_labels.txt'")

print("\n Creando el archivo combinado para poder evaluar los resultados")
# Nombres de los archivos
true_labels_file = "../data/raw/TESTB-ESP.txt"
pred_labels_file = "../data/processed/pred_labels.txt"
output_file = "../data/processed/combined.txt"
combine(true_labels_file,pred_labels_file,output_file)
print("Archivo combinado creado: 'data/processed/combined.txt'")

# Importar el script
from modules.conlleval import evaluate_conll_file

with open("../data/processed/combined.txt", "r") as file:
    result = evaluate_conll_file(file)

print("\nRESULTADOS DE LA EVALUACIÓN:")
print("=" * 50)
print(result)
print("=" * 50)
print(" Proceso completado")



