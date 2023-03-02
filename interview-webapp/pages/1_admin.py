import json
import time
import bcrypt
import streamlit as st


st.markdown(
    """
    <style>
        html, body, #root{
            border: none!important;
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
            background: green!important; color: #ffffff!important;
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
    with open("admin-auth.json", mode="r") as fp:
        credentials = json.load(fp)
    
    if admin == credentials["username"]: 
        if bcrypt.checkpw(admin_password.encode(), credentials["secure_hash"].encode()):
            with open("feedback/responses-en.csv", mode="r") as fp:
                st.download_button(
                    label="Feedback (EN)", 
                    data=fp.read(), 
                    file_name=fp.name.split("/")[-1]
                )
            with open("feedback/responses-sw.csv", mode="r") as fp: 
                st.download_button(
                    label="Feedback (SW)", 
                    data=fp.read(), 
                    file_name=fp.name.split("/")[-1]
                )        
        else:
            st.write("Wrong Password!")