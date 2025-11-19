from modules.utils import extract_plain_text, text_to_iob, combine
import spacy
from spacy.tokenizer import Tokenizer
from modules.conlleval import evaluate_conll_file

## Carga del modelo
nlp = spacy.load("es_core_news_sm")
nlp.tokenizer=Tokenizer(nlp.vocab)
print(" Modelo es_core_news_sm cargado correctamente")

## Procesamiento del archivo vacunacion_cyl.txt
with open("../data/raw/vacunacion_cyl.txt", "r", encoding="utf-8") as file:
    text_vacunacion = file.read()
doc_vacunacion = nlp(text_vacunacion)
print(f"Procesamiento completado: {len(doc_vacunacion)} tokens analizados")



##  Conversión a formato IOB
spacy_output_vacunacion=text_to_iob(doc_vacunacion)
with open('../data/processed/pred_labels_vacunacion.txt', 'w', encoding='utf-8') as out_file:
    out_file.write(spacy_output_vacunacion)
print("Etiquetas predichas guardadas en 'data/processed/pred_labels_vacunacion.txt'")


# Creamos el documento en formato word gold pred
true_labels_file = "../data/gold/gold_vacunacion.txt"
pred_labels_file = "../data/processed/pred_labels_vacunacion.txt"
output_file = "../data/processed/combined_vacunacion.txt"
combine(true_labels_file,pred_labels_file,output_file)

print("Archivo combinado creado: 'data/processed/combined_vacunacion.txt' para realizar la evaluación")

## Evaluación del modelo
with open("../data/processed/combined_vacunacion.txt", "r",encoding="utf-8") as file:
    result = evaluate_conll_file(file)

print("\nRESULTADOS DE LA EVALUACIÓN:")
print("=" * 50)
print(result)
print("=" * 50)
print(" Proceso completado")



