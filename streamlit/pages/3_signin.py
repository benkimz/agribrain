import streamlit as st

from agscripts.sql import sql_parser, user_info
from agscripts.passwords import password_verify

st.set_page_config(
    page_icon="favicon.ico", 
    page_title="Agri Brain | Sign IN"
)

st.title("Sign in to AgriBrain: ")


email = st.text_input("Email Address")
password = st.text_input("Password", type="password")


if st.button("Sign In"):
    try:
        username, location, email, userpassword = user_info(email)
        if password_verify(password, userpassword):
            st.success("Signed in successfully!")
    except Exception as error:
        st.write("--error: please check the fields again: {}".format(error))


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
        a{
            text-decoration: none!important; color: blue!important;
        }
        label > div[data-testid=stMarkdownContainer] > p, label > div > p{
            font-size: 1.2em!important;
        }
        footer{
            display: none!important;
        }    
        div.stButton > button:first-child {
            background-color: #0066cc;
            color: white;
            border-radius: 10px;
            margin: 0 auto;
            display: block;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


st.markdown("---")
st.markdown("Made with ❤️ by AgriBrain")
