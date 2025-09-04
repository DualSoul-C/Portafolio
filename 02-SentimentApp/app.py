import streamlit as st
from transformers import pipeline

#Cargar modelo de análisis de sentimientos (Huggin Face)
classifier = pipeline("sentiment-analysis")

#Intefaz
st.title("📊 Análisis de Sentimientos con BERT")
st.write("Escribe un texto y obten el sentimiento (positivo, negativo o neutral)")

#Entrada de usuario
text = st.text_area("Intruduce tu texto aquí:")

if st.button("Analizar"):
    if text.strip() != "":
        result = classifier(text)[0]
        label = result['label']
        score = result['score']
        st.write(f"**Sentimiento:** {label}")
        st.write(f"**Confianza:** {score:.2f}")
    else:
        st.warning("Por favor ingresa un texto válido.")