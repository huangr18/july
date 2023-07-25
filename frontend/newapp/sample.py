import streamlit as st

import requests
import time
from PIL import Image

import subprocess


def app(backend):


    col1, col2 = st.columns(2)

    st.header('AI trainer :sunglasses:')
    origin_video = st.file_uploader("Choose a video file", type=['mp4'])
    if origin_video is not None:
        st.header('File name', origin_video.name)

        if st.button('Start upload'):
            # origin_video_data = { "file": origin_video.getvalue() }
            # res = requests.post(backend+"/sample", origin_video=origin_video)
            # st.write(origin_video_data, ':gem:')
            # res = requests.post(backend+"/sample", origin_video_data=origin_video_data)
            # st.write(res)
# **************************** start running opencv **************************************************************************

            temp_file_to_save = origin_video.name
            # st.write(temp_file_to_save)
            def write_bytesio_to_file(filename, bytesio):
            #     """
            #     Write the contents of the given BytesIO to a file.
            #     Creates the file or overwrites the file if it does
            #     not exist yet. 
            #     """
                with open('../../storage/sample/%s'%filename, "wb") as outfile:
            #         # Copy the BytesIO stream to the output file
                    outfile.write(bytesio.getbuffer())


            # write origin video to storage/sample folder
            write_bytesio_to_file(temp_file_to_save, origin_video)



            res = requests.post(backend+f"/{temp_file_to_save}")
            # res = res.json().get("name")
            st.write(res)

            

# *************************** show result video ********************************************************************************
            col2.header("Result")
            col2.video(origin_video)

            st.snow()
            st.success('Done!')

        else:
            st.write('Goodbye')


        col1.header("Original")
        col1.video(origin_video)

    else:
        st.write('nope')