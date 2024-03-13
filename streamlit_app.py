import streamlit as st
from itertools import cycle
# from PIL import Image
# from PIL import ImageOps

import qr_reader
from my_utils.getWinNumsToCSV import crawlingLottoData, analyze_nums


if 'file_uploader_key' not in st.session_state:
    st.session_state['file_uploader_key']   = 0
    # st.session_state['button_label']    = "Load"
    st.session_state['file_uploader']   = []
    st.session_state['load_imgs']       = []
    st.session_state['load_names']      = []
    st.session_state['check_res']       = []



css = """
    <style>
        [data-testid="StyledFullScreenButton"] {
                right: 0;
                top: 0;
                height: 1.5rem;
                width: 1.5rem;
            }
            
        
        .uploadedFiles {
            display: none;
        }
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

def uploader_callback():
    if st.session_state['file_uploader'] != []:
        # st.session_state['button_label'] = "Clear"
        # temp_cnt = len(st.session_state['file_uploader'])
        img_list = st.session_state['load_imgs']
        name_list = st.session_state['load_names']
        check_list = st.session_state['check_res']

        pre_img = len(img_list)
        
        for img in st.session_state['file_uploader']:
            if img.name not in name_list:
                name_list.append(img.name)
                img_list.append(img)
                check_list.append(False)

        img_resized = qr_reader.image_resize(img_list[pre_img:])
        img_list[pre_img:] = img_resized

        st.session_state['load_imgs']   = img_list
        st.session_state['load_names']  = name_list
        st.session_state['check_res']   = check_list
    else:
        # st.session_state['button_label']    = "Load"
        st.session_state['load_imgs']       = st.session_state['file_uploader']

def remove_image(idx_list):
    temp = st.session_state['load_names']
    for i in reversed(idx_list):
        del st.session_state['load_names'][i]
        del st.session_state['load_imgs'][i]
        del st.session_state['check_res'][i]

def test_btn_evnt():
    chk_box = st.session_state['check_res'] 
    checked = []
    for i,chk in enumerate(chk_box):
        if chk:
            checked.append(i)
    
    remove_image(checked)
    # st.write(checked)
    # st.write(st.session_state['load_names'])
    # st.write('체크박스 개수 :  %d'%len(chk_box) )
    # st.write('이미지 개수 :  %d'%len(st.session_state['load_names']) )
    


# streamlit =======================================

uploaded_images = st.file_uploader('image : ', key=st.session_state['file_uploader_key'],
                            accept_multiple_files=True )

if uploaded_images:
    st.session_state['file_uploader'] = uploaded_images
    uploader_callback()

cols = cycle(st.columns(4)) # st.columns here since it is out of beta at the time I'm writing this
for idx, filteredImage in enumerate(st.session_state['load_imgs']):
    name = st.session_state['load_names'][idx]
    with next(cols):
        st.image(filteredImage, use_column_width=True)
        st.session_state['check_res'][idx] = st.checkbox(name, key=name)

c3_1, c3_2 = st.columns([5, 1])
with c3_1:
    btn_anal = st.button('분석', use_container_width=True)
with c3_2:
    # submitted = st.form_submit_button(st.session_state['button_label'],on_click=uploader_callback)
    btn_del = st.button("Clear", use_container_width=True)   #,on_click=test_btn_evnt)

if btn_del:
    st.session_state["file_uploader_key"] += 1
    test_btn_evnt()
    st.rerun()

if btn_anal:
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


# img {
#             max-height: 300px;
#         }
#         img:hover {
#             transform: scale(1);
#             border:1px solid blue;
#         }
#         img:active {
#             transform: scale(1.1);
#         }
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

# <body>
    
#     <img src="/Users/darkred/Documents/btc_project/images/beautiful-dog.jpg" alt="My Image"/> 
# </body>
#     <style>
        #         [data-testid='stFileUploader'] section > input + div {
        #     display: none;
        # }
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