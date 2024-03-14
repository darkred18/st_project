import streamlit as st

if "file_uploader_key" not in st.session_state:
    st.session_state["file_uploader_key"] = 0

if "uploaded_files" not in st.session_state:
    st.session_state["uploaded_files"] = []

files = st.file_uploader(
    "Upload some files",
    accept_multiple_files=True,
    key=st.session_state["file_uploader_key"],
)

if files:
    st.session_state["uploaded_files"] = files
    st.session_state["file_uploader_key"] += 1
    st.rerun()

if st.button("Clear uploaded files"):
    # st.session_state["file_uploader_key"] += 1
    # st.rerun()


    st.write("Uploaded files:", st.session_state["uploaded_files"])




# import streamlit as st
# from PIL import Image
# import numpy as np

# img_file_buffer = st.camera_input("Take a picture")

# if img_file_buffer is not None:
#     # To read image file buffer as a PIL Image:
#     img = Image.open(img_file_buffer)

#     # To convert PIL Image to numpy array:
#     img_array = np.array(img)

#     # Check the type of img_array:
#     # Should output: <class 'numpy.ndarray'>
#     st.write(type(img_array))

#     # Check the shape of img_array:
#     # Should output shape: (height, width, channels)
#     st.write(img_array.shape)
