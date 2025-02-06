import streamlit as st
import face_recognition
import numpy as np
from PIL import Image

def compare_faces(img1, img2):
    enc1 = face_recognition.face_encodings(img1)
    enc2 = face_recognition.face_encodings(img2)

    if not enc1 or not enc2:
        return None  # Лицо не найдено

    dist = np.linalg.norm(enc1[0] - enc2[0])
    prob = max(0.0, 1.0 - dist / 1.2)  # Грубая нормировка
    return prob

st.title("🔍 Сравнение лиц по фото")

uploaded_file1 = st.file_uploader("Загрузите первое фото", type=["jpg", "png", "jpeg"])
uploaded_file2 = st.file_uploader("Загрузите второе фото", type=["jpg", "png", "jpeg"])

if uploaded_file1 and uploaded_file2:
    img1 = face_recognition.load_image_file(uploaded_file1)
    img2 = face_recognition.load_image_file(uploaded_file2)

    st.image([Image.open(uploaded_file1), Image.open(uploaded_file2)], caption=["Фото 1", "Фото 2"], width=300)

    probability = compare_faces(img1, img2)

    if probability is not None:
        st.write(f"**Вероятность, что это один человек: {probability:.2f}**")
    else:
        st.write("❌ Лицо на одном из фото не найдено")
