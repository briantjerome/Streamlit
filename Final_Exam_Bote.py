import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

@st.cache(allow_output_mutation=True)
def load_model():
    model = tf.keras.models.load_model('best_model.h5')
    return model

model = load_model()

st.write("""
# Fashion MNIST Accessory System
""")

file = st.file_uploader("Choose a fashion accessory image (bag, shirt, etc.) from your computer", type=["jpg", "png"])

if file is None:
    st.text("Please upload an image file")
else:
    img = image.load_img(file, target_size=(64, 64), color_mode="grayscale")
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    prediction = model.predict(img_array)
    predicted_class_index = np.argmax(prediction)
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress',
                   'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    st.image(img, use_column_width=True)
    st.success("Predicted Class: " + class_names[predicted_class_index])
