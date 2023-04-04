import json
import streamlit as st

from agscripts.passwords import password_verify

st.set_page_config(
    page_icon="favicon.ico", 
    page_title="Agri Brain -Admin"
)

st.markdown(
    """
    <style>
        html, body, #root{
            border: none!important;
        }
        header[data-testid=stHeader]{
            background: #006a08!important;
        }        
        section[data-testid=stSidebar]{
            background: #e5ffe1!important;
        }
        hr{
            margin: 0px!important;
        }     
        div[data-testid=stToolbar]{
            display: none!important;
        }
        .stButton > button{
            background: #3232f9!important; color: #ffffff!important;
            border: none!important; outline: none!important; box-shadow: none!important;
        }
        a{
            text-decoration: none!important; color: blue!important;
        }
        label > div[data-testid=stMarkdownContainer] > p, label > div > p{
            font-size: 1.2em!important;
        }
        footer{
            display: none!important;
        }
    </style>
    """, unsafe_allow_html=True
)

admin = st.text_input(
    label="User", 
    autocomplete="on", 
    placeholder="username"
)
admin_password = st.text_input(
    label="Administrator Password", 
    type="password", 
    autocomplete="on", 
    placeholder="********"
)

auth_button = st.button(label="Authenticate: ")
if auth_button:
    with open("./assets/interview/admin-auth.json", mode="r") as fp:
        credentials = json.load(fp)
    
    if admin == credentials["username"]: 
        if password_verify(password=admin_password, hashed=credentials["secure_hash"].encode()):
            with open("./assets/interview/feedback/responses-en.csv", mode="r") as fp:
                st.download_button(
                    label="Feedback (EN)", 
                    data=fp.read(), 
                    file_name=fp.name.split("/")[-1]
                )
            with open("./assets/interview/feedback/responses-sw.csv", mode="r") as fp: 
                st.download_button(
                    label="Feedback (SW)", 
                    data=fp.read(), 
                    file_name=fp.name.split("/")[-1]
                )
                
            if st.button("Register an ARC"):
                arcname = st.text_input("ARC name: ")
                chair = st.text_input("Chair email: ")
                location = st.selectbox("Location", [])
                capacity = st.number_input("Farmers capacity")
                products = st.text_area("Priority products")
        else:
            st.write("Wrong Password!")