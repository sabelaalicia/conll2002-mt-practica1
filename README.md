# Proyecto de Minería de Textos - Práctica 1
## Reconocimiento de Entidades Nombradas (NER) con SpaCy

Este proyecto implementa un sistema de reconocimiento de entidades nombradas utilizando SpaCy para procesar texto en español y evaluarlo contra el conjunto de datos CoNLL-2002.

## Estructura del Proyecto

```
conll2002-mt-practica1/
├── README.md                 # Este archivo
├── requirements.txt          # Dependencias del proyecto
├── data/
│   ├── raw/                 # Datos originales
│   │   └── TESTB-ESP.txt    # Dataset CoNLL-2002 en español
│   └── processed/           # Datos procesados (generados automáticamente)
│       ├── plain_text.txt   # Texto plano extraído
│       ├── pred_labels.txt  # Predicciones de SpaCy
│       └── combined.txt     # Formato para evaluación
├── src/
│   ├── main.py             # Script principal
│   └── modules/
│       ├── utils.py        # Funciones auxiliares
│       └── conlleval.py    # Evaluación CoNLL
├── notebooks/              # Jupyter notebooks
└── docs/                  # Documentación adicional
```

## Instalación y Configuración

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/sabelaalicia/conll2002-mt-practica1.git
   cd conll2002-mt-practica1
   ```

2. **Crear entorno virtual (recomendado):**
   ```bash
   python -m venv venv
   
   # Activar el entorno virtual:
   # Windows:
   venv\Scripts\activate
   # Linux/macOS:
   source venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verificar instalación:**
   ```bash
   python -c "import spacy; print('SpaCy instalado correctamente')"
   python -c "import spacy; nlp = spacy.load('es_core_news_sm'); print('Modelo español cargado')"
   ```

## Uso

### Ejecución del Script Principal

```bash
cd src
python main.py
```


## Funcionalidades

### 1. Extracción de Texto Plano
- Convierte archivos CoNLL-2002 a texto plano
- Extrae solo las palabras (primera columna)
- Preserva la estructura de oraciones

### 2. Procesamiento con SpaCy
- Utiliza el modelo preentrenado `es_core_news_sm`
- Tokenización personalizada para mantener consistencia
- Reconocimiento automático de entidades nombradas

### 3. Conversión a Formato IOB
- Transforma las predicciones de SpaCy al formato IOB2
- Compatible con el estándar CoNLL-2002
- Etiquetas soportadas: PER, LOC, ORG, MISC

### 4. Evaluación de Rendimiento
- Métricas de precisión, recall y F1-score
- Evaluación por tipo de entidad
- Evaluación global del sistema

## Métricas de Evaluación

El sistema evalúa automáticamente:

- **Precisión**: Porcentaje de entidades predichas que son correctas
- **Recall**: Porcentaje de entidades reales que fueron encontradas
- **F1-Score**: Media armónica entre precisión y recall
- **Accuracy**: Precisión a nivel de token