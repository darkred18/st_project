import streamlit as st
from itertools import cycle
# from PIL import Image
# from PIL import ImageOps

import qr_reader
from my_utils.getWinNumsToCSV import crawlingLottoData, analyze_nums


if 'file_uploader' not in st.session_state:
    st.session_state['load_imgs'] = []
    st.session_state['load_names'] = []
    st.session_state['button_label'] = "Load"

# def image_resize(f_imgs):
#     #이미지가 자동으로 회전되는 현상을 막아줌.
#     #ImageOps.exif_transpose(image)
#     imgs = [ImageOps.exif_transpose(Image.open(f)) for f in f_imgs]

#     for img in imgs:
#         w,h = img.size
#         img_width = 640 if w > h else 480
#         if w <= img_width: continue
#         img_ratio = img_width/float(w)
#         img_height = int((h * img_ratio)) 
#         img = img.resize((img_width,img_height))
#     return imgs

html2 = """
    <style>
        [data-testid="StyledFullScreenButton"] {
            right: 0;
            top: 0;
            height: 1.5rem;
            width: 1.5rem;
        }
        
        img {
            max-height: 300px;
        }
        img:hover {
            transform: scale(1);
            border:1px solid blue;
        }
        img:active {
            transform: scale(1.1);
        }
    </style>
"""
st.markdown(html2, unsafe_allow_html=True)

def uploader_callback():
    # if st.session_state['load_imgs']:
    #     st.write('add button %d' % len(st.session_state['file_uploader']))
    # else:
    #     st.write('remove button %d' % len(st.session_state['file_uploader']))


    if st.session_state['file_uploader'] != []:
        st.session_state['button_label'] = "Clear"
        img_list = []
        name_list = []
        for img in st.session_state['file_uploader']:
            if img.name not in name_list:
                name_list.append(img.name)
                img_list.append(img)

        img_resized = qr_reader.image_resize(img_list)
        st.session_state['load_imgs'] = img_resized
        st.session_state['load_names'] = name_list
    else:
        st.session_state['button_label'] = "Load"
        st.session_state['load_imgs'] = st.session_state['file_uploader']

def test():
    print('test')

    
# streamlit =======================================

# Create a list to store the uploaded file names
file_list = []

# Use the file_uploader to allow users to upload files
uploaded_files = st.file_uploader("Upload Files", accept_multiple_files=True)

# Loop through the uploaded files
for uploaded_file in uploaded_files:
    if uploaded_file is not None:
        # Append the name of the uploaded file to the file_list
        file_list.append(uploaded_file.name)

# Display the list of uploaded file names
st.write("Uploaded Files:")
for file_name in file_list:
    # Provide a checkbox for each file name to allow users to remove files
    remove_file = st.checkbox(file_name)
    if remove_file:
        # Remove the file name from the file_list if the checkbox is selected
        file_list.remove(file_name)




with st.form("my-form", clear_on_submit=True, ):
    uploaded_image = st.file_uploader('image : ', key='file_uploader',
                                accept_multiple_files=True )
    if uploaded_image:
        st.write('이미지 불러옴 : %d'%len(uploaded_image))
    else:
        st.write('이미지 지움 : %d'%len(uploaded_image))

    c3_1, c3_2 = st.columns([5, 1])
    with c3_2:
        submitted = st.form_submit_button(st.session_state['button_label'],on_click=uploader_callback)

cols = cycle(st.columns(4)) # st.columns here since it is out of beta at the time I'm writing this
for idx, filteredImage in enumerate(st.session_state['load_imgs']):
    next(cols).image(filteredImage, width=150, caption=st.session_state['load_names'][idx],use_column_width=True)

if st.button('분석'):
    res = qr_reader.get_number_from_image(st.session_state['load_imgs'])
    if res == []:
        st.write('qr코드 읽지 못함.')
    else:
        for r in res:
            round, nums = r[0]
            res = analyze_nums(int(round),nums)
            if res:
                st.write(round + '회차 당첨')
                for n in nums:
                    st.text(str(n))
            else:
                st.write(round + '회차 낙첨')


# streamlit -----------------------------------------



# [data-testid="StyledFullScreenButton"] {
#             right: 0;
#             top: 0;
            # visibility: hidden;
#         }
# button {
#     height: auto;
#     padding-top: 10px !important;
#     padding-bottom: 10px !important;
# }
# div[data-testid="stImage"]:hover
#         {
#             border:1px solid blue;
#         }


# html = """
# <html>
# <head>
#     <!--    파이스크립트를 실행하기 위해 head 부분에 css와 js 파일을 로드-->
#     <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
#     <script defer src="https://pyscript.net/alpha/pyscript.js"></script>

# </head>
# <body>
    
#     <img src="/Users/darkred/Documents/btc_project/images/beautiful-dog.jpg" alt="My Image"/> 
# </body>
#     <style>
#         [data-testid="StyledFullScreenButton"] {
#             right: 0;
#             top: 0;
#             height: 1.5rem;
#             width: 1.5rem;
#         }
        
#         img {
#             max-height: 300px;
#         }
#         img:hover {
#             transform: scale(1);
#             border:1px solid blue;
#         }
#         img:active {
#             transform: scale(1.5);

#             <py-script> print('Hello, World!') </py-script>

#         }
#     </style>
# </html>
# """