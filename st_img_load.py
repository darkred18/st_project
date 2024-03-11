import streamlit as st
from itertools import cycle
from PIL import Image
from my_utils.getWinNumsToCSV import *
import qr_reader


# sys.path.append('/Users/darkred/Documents/btc_project')


if 'file_uploader' not in st.session_state:
    st.session_state['load_imgs'] = []
    st.session_state['load_names'] = []
    st.session_state['button_label'] = "Load"


def uploader_callback():
    if st.session_state['file_uploader'] != []:
        st.session_state['button_label'] = "Clear"
        img_list = []
        name_list = []
        for img in st.session_state['file_uploader']:
            if img.name not in name_list:
                name_list.append(img.name)
                img_list.append(img)
        st.session_state['load_imgs'] = img_list
        st.session_state['load_names'] = name_list
    else:
        st.session_state['button_label'] = "Load"
        st.session_state['load_imgs'] = st.session_state['file_uploader']


def say_hello():
   db_path = 'my_utils/lotto_number_DB.csv'
   info, round = crawlingLottoData(db_path)
   st.write(info)
   st.write(round)



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

def test_click():
    print('test click')  

html = """
<html>
<head>
    <!--    파이스크립트를 실행하기 위해 head 부분에 css와 js 파일을 로드-->
    <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>

</head>
<body>
    
    <img src="/Users/darkred/Documents/btc_project/images/beautiful-dog.jpg" alt="My Image"/> 
</body>
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
            transform: scale(1.5);

            <py-script> print('Hello, World!') </py-script>

        }
    </style>
</html>
"""
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


with st.form("my-form", clear_on_submit=True):
    uploaded_image = st.file_uploader('image : ',key='file_uploader',
                                accept_multiple_files=True )
    c3_1, c3_2 = st.columns([5, 1])
    with c3_2:
        submitted = st.form_submit_button(st.session_state['button_label'],on_click=uploader_callback)


cols = cycle(st.columns(4)) # st.columns here since it is out of beta at the time I'm writing this
for idx, filteredImage in enumerate(st.session_state['load_imgs']):
    next(cols).image(filteredImage, width=150, caption=st.session_state['load_names'][idx],use_column_width=True)
    


if st.button('분석'):
    imgs = [Image.open(f) for f in st.session_state['load_imgs']]
    qr_reader.get_number_from_image(imgs)

    # say_hello()
    