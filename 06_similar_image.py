import streamlit as st
import cv2
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import glob

# app title
st.set_page_config(page_title="Image Matcher", page_icon=":camera:", layout="wide")

# Custom CSS for better styling
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f2f6;
        padding: 20px;
    }
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #333;
    }
    .upload-section {
        border: 2px dashed #ccc;
        padding: 20px;
        border-radius: 10px;
        background-color: #fff;
    }
    .image-section {
        text-align: center;
    }
    .image-caption {
        font-size: 18px;
        color: #555;
    }
    </style>
""", unsafe_allow_html=True)

# App title
st.markdown("<div class='title'>Image Matcher</div>", unsafe_allow_html=True)

# Feature extraction using color histograms
def color_histogram(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    cv2.normalize(hist, hist)
    return hist.flatten()

# Upload image section
st.markdown("<div class='upload-section'>", unsafe_allow_html=True)
uploaded_img = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
st.markdown("</div>", unsafe_allow_html=True)

if uploaded_img is not None:
    file_bytes_img = np.asarray(bytearray(uploaded_img.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes_img, cv2.IMREAD_COLOR)

    if img is not None:
        queryFeature = color_histogram(img)
        highestSimilarity = -1
        mostSimilarImage = ""

        for filename in glob.iglob('database/*.jpg'):
            database_img = cv2.imread(filename, cv2.IMREAD_COLOR)
            if database_img is not None:
                database_Feature = color_histogram(database_img)
                similarity = cosine_similarity([queryFeature], [database_Feature])[0][0]
                if similarity > highestSimilarity:
                    highestSimilarity = similarity
                    mostSimilarImage = filename

        if mostSimilarImage:
            st.markdown("<div class='image-section'>", unsafe_allow_html=True)
            st.write(f"Most similar image: {mostSimilarImage}")
            similar_img = cv2.imread(mostSimilarImage, cv2.IMREAD_COLOR)
            similar_img_rgb = cv2.cvtColor(similar_img, cv2.COLOR_BGR2RGB)
            query_img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            st.image(query_img_rgb, caption="Query Image", use_column_width=True)
            st.image(similar_img_rgb, caption="Most Similar Image", use_column_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.write("No similar image found.")
    else:
        st.error("Error reading the uploaded image.")
else:
    st.write("Please upload an image.")



