import streamlit as st
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from PIL import Image
import numpy as np

#Cargar modelo entrenado
model = tf.keras.models.load_model("image_classifier.h5")

st.title("Clasificador de Imágenes - CIFAR10")

uploaded_file = st.file_uploader("Sube una imagen", type=["jpg","png"])

labels = ["avion", "auto", "pajaro", "gato", "ciervo", "perro", "rana", "caballo", "barco", "camion"]

if uploaded_file:
    image = Image.open(uploaded_file).resize((128,128))
    st.image(image, caption="Imagen subida", use_container_width=True)

    img_array = np.array(image)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    preds = model.predict(img_array)
    label = labels[np.argmax(preds)]
    st.write(f"Predicción: **{label}**")