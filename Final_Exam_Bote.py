import streamlit as st
import tensorflow as tf
from tensorflow import keras
from PIL import Image
import numpy as np

@st.cache(allow_output_mutation=True)
def load_model():
    model = keras.models.load_model('best_model.h5')
    return model

model = load_model()

st.write("""
# Fashion MNIST Accessory System
""")

file = st.file_uploader("Choose a fashion accessory image (bag, shirt, etc.) from your computer", type=["jpg", "png"])

if file is None:
    st.text("Please upload an image file")
else:
    img = Image.open(file).convert('L')
    img = img.resize((28, 28))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    predicted_class_index = np.argmax(prediction)
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress',
                   'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    st.image(img, use_column_width=True)
    st.success("Predicted Class: " + class_names[predicted_class_index]) 
