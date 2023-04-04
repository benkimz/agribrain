import streamlit as st

from agscripts.regions import kenyan_regions
from agscripts.passwords import password_hash
from agscripts.sql import UserEntry, user_info

st.set_page_config(
    page_icon="favicon.ico", 
    page_title="Agri Brain | Sign UP"
)

location_options = kenyan_regions("./assets/regions.json")

st.title("AgriBrain Sign UP")

name = st.text_input("Name")
location = st.selectbox("Location", location_options)
email = st.text_input("Email Address")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

if st.button("Submit"):
    if password != confirm_password:
        st.warning("Passwords do not match!")
    else:
        try:
            user = UserEntry(name, 
                             location, 
                             email, 
                             password_hash(password))
            st.success("Thank you for signing up!")
        except Exception as error:
            st.warning("--error -signing up")


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
