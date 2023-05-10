import streamlit as st
from glob import glob
from streamlit_image_annotation import pointdet

label_list = ['deer', 'human', 'dog', 'penguin', 'framingo', 'teddy bear']
image_path_list = glob('image/*.jpg')
if 'result_dict' not in st.session_state:
    result_dict = {}
    for img in image_path_list:
        result_dict[img] = {'points': [[0,0],[50,150], [200,200]],'labels':[0,3,4]}
    st.session_state['result_dict'] = result_dict.copy()

num_page = st.slider('page', 0, len(image_path_list)-1, 0, key='slider')
target_image_path = image_path_list[num_page]

new_labels = pointdet(image_path=target_image_path, 
                        label_list=label_list, 
                        points=st.session_state['result_dict'][target_image_path]['points'],
                        labels=st.session_state['result_dict'][target_image_path]['labels'], key=target_image_path)
if new_labels is not None:
    st.session_state['result_dict'][target_image_path]['points'] = [v['point'] for v in new_labels]
    st.session_state['result_dict'][target_image_path]['labels'] = [v['label_id'] for v in new_labels]
st.json(st.session_state['result_dict'])