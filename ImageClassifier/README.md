# 🖼️ Clasificador de Imágenes con Transfer Learning

Este proyecto implementa un **clasificador de imágenes** utilizando **Transfer Learning** con la arquitectura **MobileNetV2**.  
El objetivo es mostrar cómo reutilizar modelos preentrenados en **ImageNet** para resolver un problema de clasificación sobre el dataset **CIFAR-10**.  

---

## 📌 Descripción
- Se utiliza **CIFAR-10**, un dataset que contiene 60.000 imágenes de 10 clases diferentes (avión, auto, perro, gato, etc.).  
- Se aplica **Transfer Learning** congelando las capas convolucionales de MobileNetV2 y entrenando solo la parte final (clasificador denso).  
- Se entrena el modelo, se evalúa en datos de prueba y se despliega una aplicación interactiva con **Streamlit**.  

---

## 🚀 Tecnologías
- **Python 3.9+**  
- **TensorFlow / Keras**  
- **Streamlit** (para la interfaz web)  
- **Matplotlib** (para gráficas de entrenamiento)  

---

## 📂 Estructura del Proyecto
├── train.ipynb # Notebook con el entrenamiento del modelo \
├── app.py # Aplicación web con Streamlit \
├── image_classifier.h5 # Modelo entrenado \
├── requirements.txt # Dependencias del proyecto \
└── README.md # Documentación \

## ⚙️ Instalación y uso

### 1. Clonar repositorio
```
git clone https://github.com/tuusuario/01-ImageClassifier.git
cd 01-ImageClassifier
```

### 2. Crear entorno e instalar dependencias
```
pip install -r requirements.txt
```

### 3. Entrenar modelo
```
jupyter notebook train.ipynb
```

### 4. Ejecutar aplicación web
```
streamlit run app.py
```
