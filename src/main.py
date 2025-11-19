from modules.utils import extract_plain_text, text_to_iob, combine
import spacy
from spacy.tokenizer import Tokenizer
from modules.conlleval import evaluate_conll_file


print("Iniciando procesamiento")
print("=" * 50)

# Convertimos y guardamos el texto plano
plain_text = extract_plain_text('../data/raw/TESTB-ESP.txt')
with open('../data/processed/plain_text.txt', 'w', encoding='utf-8') as out_file:
    out_file.write(plain_text)   
print("Texto plano extraído y guardado en 'data/processed/plain_text.txt'")




##Customizamos la tockenización y cargamos un modelo preentrenado
nlp = spacy.load("es_core_news_sm")
nlp.tokenizer=Tokenizer(nlp.vocab)

# Leer el texto desde un archivo
with open("../data/processed/plain_text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Procesar el texto con SpaCy
doc = nlp(text)

spacy_otput=text_to_iob(doc)
with open('../data/processed/pred_labels.txt', 'w', encoding='utf-8') as out_file:
    out_file.write(spacy_otput)


# Nombres de los archivos
true_labels_file = "../data/raw/TESTB-ESP.txt"
pred_labels_file = "../data/processed/pred_labels.txt"
output_file = "../data/processed/combined.txt"
combine(true_labels_file,pred_labels_file,output_file)

# EVALUACIÓN
with open("../data/processed/combined.txt", "r") as file:
    result = evaluate_conll_file(file)

print("\nRESULTADOS DE LA EVALUACIÓN:")
print("=" * 50)
print(result)
print("=" * 50)



