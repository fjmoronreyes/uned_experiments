# Tesis — Sesgos y análisis del discurso en IA generativa

Este proyecto contiene los experimentos de la tesis para analizar la **alineación discursiva**
entre textos periodísticos y texto generado por modelos de IA, utilizando embeddings y
similitud coseno.

La gestión del entorno se realiza con **Poetry** y el trabajo experimental se hace desde
**notebooks en el editor (VS Code / Windsurf)**, no lanzando servidores Jupyter manualmente.

---

## Estructura del proyecto

tesis/
├── data/
│ ├── raw/ # Textos originales (periódicos)
│ └── clean/ # Textos normalizados
├── notebooks/
│ └── experiments.ipynb
├── results/ # Resultados de ejecuciones
├── src/ # Código Python reusable
└── README.md


---

## Requisitos

- Python **3.12**
- Poetry instalado (`pipx install poetry` recomendado)
- Editor con soporte de notebooks (VS Code / Windsurf)

---

## Setup del entorno (pasos que funcionan)

Desde la raíz del proyecto (`tesis/`):

### 1. Configurar Poetry para usar venv local

```bash
poetry config virtualenvs.in-project true --local
poetry config virtualenvs.create true --local
```

### 2. Crear el entorno virtual con Python 3.12

```bash
poetry env use /usr/bin/python3.12
```

Esto crea el entorno en:

```bash
tesis/.venv/
```

### 3. Instalar dependencias

```
poetry install
poetry add numpy pandas scikit-learn python-dotenv openai
poetry add --group dev jupyter ipykernel
```
