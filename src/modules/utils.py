import re
import os
from typing import Optional, List, Tuple

def extract_plain_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    text = []
    for line in lines:
        if line.strip():
            word = line.split()[0]  # Toma la primera columna (palabra)
            text.append(word)
        else:
            text.append('')  # Si la línea está vacía es espacio

    # Unimos las palabras con espacios
    plain_text = ' '.join(text)
    return plain_text


def text_to_iob(doc):
    iob_output = []
    for token in doc:
        # Si el token está dentro de una entidad nombrada (B, I, O)
        if token.ent_iob_ == "B":
            iob_output.append(f"{token.text} B-{token.ent_type_}")
        elif token.ent_iob_ == "I":
            iob_output.append(f"{token.text} I-{token.ent_type_}")
        elif token.text!=' ':
            # Si no está dentro de una entidad nombrada, es Outside (O)
            iob_output.append(f"{token.text} O")
        else:
            iob_output.append(' ')

    iob_output = "\n".join(iob_output)

    return iob_output

def combine (true_labels_file, pred_labels_file, output_file):
    
    # Leemos ambos archivos
    with open(true_labels_file, "r", encoding="utf-8") as f:
        true_lines = f.read().strip().splitlines()

    with open(pred_labels_file, "r", encoding="utf-8") as f:
        pred_lines = f.read().strip().splitlines()

    # Creamos el archivo combinado
    with open(output_file, "w", encoding="utf-8") as f:
        for true_line, pred_line in zip(true_lines, pred_lines):
            if true_line.strip() == "" or pred_line.strip() == "":
                # Línea vacía (separación de oraciones)
                f.write("\n")
                continue

            # Dividir palabras y etiquetas
            true_word, true_label = true_line.rsplit(maxsplit=1)
            pred_word, pred_label = pred_line.rsplit(maxsplit=1)

            f.write(f"{true_word} {true_label} {pred_label}\n")

        f.write("\n")

