import streamlit as st
import tensorflow as tf
from tensorflow.keras.datasets import fashion_mnist

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
    image = tf.image.decode_image(file.read(), channels=1)
    image = tf.image.resize(image, [28, 28]) / 255.0
    image = tf.expand_dims(image, axis=0)

    prediction = model.predict(image)
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress',
                   'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
    
    predicted_class_index = tf.argmax(prediction[0]).numpy()
    predicted_class = class_names[predicted_class_index]

    st.image(image[0], use_column_width=True)
    st.success("Predicted Class: " + predicted_class)
