import time

import requests
import streamlit as st
from PIL import Image

STYLES = {
    "candy": "candy",
    "composition 6": "composition_vii",
    "feathers": "feathers",
    "la_muse": "la_muse",
    "mosaic": "mosaic",
    "starry night": "starry_night",
    "the scream": "the_scream",
    "the wave": "the_wave",
    "udnie": "udnie",
}

def app(backend):
    st.set_option("deprecation.showfileUploaderEncoding", False)

    st.title("Apply Visual Styles to a Target Image")

    image = st.file_uploader("Choose an image")

    style = st.selectbox("Choose the style", [i for i in STYLES.keys()])

    col1, col2 = st.columns(2)

    if st.button("Style Transfer"):
        if image is not None and style is not None:
            files = {"file": image.getvalue()}
            original_image = Image.open(image)

            res = requests.post(backend+f"/{style}", files=files)
            st.header(res)
            img_path = res.json()
            image = Image.open(img_path.get("name"))

            
            col1.header("Original")
            col1.image(original_image, use_column_width=True)
            col2.header("Translated")
            col2.image(image, use_column_width=True)

            

            # displayed_styles = [style]
            # displayed = 1
            # total = len(STYLES)

            # st.write("Generating other models...")

            # while displayed < total:
            #     for style in STYLES:
            #         if style not in displayed_styles:
            #             try:
            #                 path = f"{img_path.get('name').split('.')[0]}_{STYLES[style]}.jpg"
            #                 image = Image.open(path)
            #                 st.image(image, width=500)
            #                 time.sleep(1)
            #                 displayed += 1
            #                 displayed_styles.append(style)
            #             except:
            #                 pass
