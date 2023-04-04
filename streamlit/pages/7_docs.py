import streamlit as st

st.set_page_config(
    page_icon="favicon.ico", 
    page_title="Agri Brain", 
    layout="wide"
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

st.markdown(
    """
    ### Crop Yield Model
    ---
    
    ##### Model Input and Output using the inference script:
    ---
    """)

st.markdown(
    """
    To make a prediction, a python dictionary is passed to a function/ api that does 
    inference from the model and returns the desired outputs.
    
    * Query format:

        ```python
        query = {
            'county': 'county goes here', 
            'crop': 'crop of interest', 
            'year': 'year of interest', 
            'area': 'area of interest in HA'
        }
        ```
        
    * Output format:
    
        ```python
        # production in Metric tons
        # yield in production per unit HA
        output = (production, yield)
        ```
    
    """
)