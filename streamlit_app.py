import streamlit as st
from itertools import cycle
import qr_reader
from my_utils.getWinNumsToCSV import crawlingLottoData, analyze_nums
import time

if 'file_uploader_key' not in st.session_state:
    st.session_state['file_uploader_key']   = 0
    st.session_state['file_uploader']   = []
    st.session_state['load_imgs']       = []
    st.session_state['load_names']      = []
    st.session_state['check_res']       = []

css = """
    <style>
        
        [data-testid="stButton"] 'update DB'{
        
            padding-top: 50px;
}

        [data-testid="StyledFullScreenButton"] {
                right: 0;
                top: 0;
                height: 1.5rem;
                width: 1.5rem;
            }
            
        
        .uploadedFiles {
            display: none;
        }

        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}

    </style>
"""
st.markdown(css, unsafe_allow_html=True)

def uploader_callback():
    stime = time.time()
    if st.session_state['file_uploader'] != []:
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
        st.session_state['load_imgs']   = st.session_state['file_uploader']

    print('uploader_callback : %f'%(time.time() - stime))

def remove_image(idx_list):
    temp = st.session_state['load_names']
    for i in reversed(idx_list):
        del st.session_state['load_names'][i]
        del st.session_state['load_imgs'][i]
        del st.session_state['check_res'][i]

def btn_clear_all():
    st.session_state['load_names'] = []
    st.session_state['load_imgs'] = []
    st.session_state['check_res'] = []

def btn_clear_select():
    chk_box = st.session_state['check_res'] 
    checked = [i for i,chk in enumerate(chk_box) if chk]
    remove_image(checked)


# streamlit =======================================

col1, col2 = st.columns([5, 1])
with col1:
    uploaded_images = st.file_uploader('image : ', 
                                       key=st.session_state['file_uploader_key'],
                                        accept_multiple_files=True )
with col2:
    if st.button("update DB", use_container_width=True):
        crawlingLottoData()

if uploaded_images:
    st.session_state['file_uploader'] = uploaded_images
    
    uploader_callback()
    
    
    st.session_state["file_uploader_key"] += 1
    st.rerun()

stime = time.time()
cols = cycle(st.columns(4)) # st.columns here since it is out of beta at the time I'm writing this
for idx, filteredImage in enumerate(st.session_state['load_imgs']):
    name = st.session_state['load_names'][idx]
    with next(cols):
        st.image(filteredImage, use_column_width=True)
        st.session_state['check_res'][idx] = st.checkbox(name, key=name)
print('image display : %f'%(time.time()-stime))

c3_1, c3_2 = st.columns([3, 1])

stime = time.time()
with c3_1:
    if st.button("선택한 이미지 삭제", use_container_width=True):
        btn_clear_select()
        st.rerun()
with c3_2:
    if st.button("모든 이미지 삭제", use_container_width=True):
        btn_clear_all()
        st.rerun()
print('image clear : %f'%(time.time()-stime))


if st.button('분석', use_container_width=True):
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