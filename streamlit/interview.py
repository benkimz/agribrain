import os
import json
import pandas as pd
import streamlit as st

from PIL import Image

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

side_bar = st.sidebar
with side_bar:
    st.markdown(
        """
        ## :star: Interview by Agri Brain:
        
        ### Goal:
        ---
        To gather insights from farmers or persons that are otherwise related to farming practices either 
        directly or indirectly.  
              
        ### Objectives:
        ---
        * To gather insights
        * Assessing challenges in the farming space
        * Selecting a problem to solve
        * Building a solution      
        
        ### Social Handles:
        ---
        
        * [:cat: GitHub](https://github.com/benkimz) 
        
        * [:link: LinkedIn](https://www.linkedin.com/in/benkimz)
        
        * [:bird: Twitter](https://www.twitter.com/benkimz_01) 
        
        * [:tv: YouTube](https://youtube.com/)
                
        """
    )

banner_image = Image.open(
    r"./assets/banners/solutionchallenge-2023-Website-EventBanners_Full.png"
)
st.image(banner_image, caption="Google Solutions Challenge -Agri Brain", use_column_width=True) 

st.markdown(
    """
    ### Investigating the challenges that farmers are facing.
    ---
    """
)

language = st.selectbox(label="Select Language", options=sorted({"en", "sw"}))

st.markdown(
    """
    #### <center>Interview questions:</center>
    ---
    """, unsafe_allow_html=True
)
questions_dir = "./assets/interview/questions/"
placeholders_dir = "./assets/interview/placeholders/"
options_dir = "./assets/interview/options/"

with open("{}questions-{}.json".format(questions_dir, language), mode="r", encoding="utf-8") as fp:
    questions = json.load(fp=fp)

with open("{}placeholders-{}.json".format(placeholders_dir, language), mode="r", encoding="utf-8") as fp:
    placeholders = json.load(fp=fp)
    
with open("{}options-{}.json".format(options_dir, language), mode="r", encoding="utf-8") as fp:
    radio_opts = json.load(fp)

answer_1 = st.radio(
    label="1). {}".format(questions["question_1"]),  
    options=tuple(radio_opts["question_1"])
)
answer_2 = st.radio(
    label="2). {}".format(questions["question_2"]), 
    options=tuple(radio_opts["question_2"])
)
answer_3 = st.radio(
    label="3). {}".format(questions["question_3"]), 
    options=tuple(radio_opts["question_3"])
)
answer_4 = st.radio(
    label="4). {}".format(questions["question_4"]), 
    options=tuple(radio_opts["question_4"])
)
answer_5 = st.radio(
    label="5). {}".format(questions["question_5"]), 
    options=tuple(radio_opts["question_5"])
)
answer_6 = st.radio(
    label="6). {}".format(questions["question_6"]), 
    options=tuple(radio_opts["question_6"])
)
answer_7 = st.radio(
    label="7). {}".format(questions["question_7"]), 
    options=tuple(radio_opts["question_7"])
)
answer_8 = st.radio(
    label="8). {}".format(questions["question_8"]), 
    options=tuple(radio_opts["question_8"])
)

response_file = "./assets/interview/feedback/responses-{}.csv".format(language)

def submit_interview(**kwargs):
    for index, item in enumerate(kwargs.items()):
        question_tag, answer = item
        answer = answer.strip()
        if not answer: return
    if os.path.getsize(response_file) == 0:
        columns = list(questions.keys())
        df = pd.DataFrame(columns=columns)
    else: df = pd.read_csv(response_file)
    rows, cols = df.shape
    df.loc[rows, :] = list(kwargs.values())
    df.to_csv(response_file, index=False)
    st.success("Response saved successfully!")
    

submit_button = st.button(label="submit interview")
if submit_button:
    submit_interview(
        **{
            "question_1": answer_1, 
            "question_2": answer_2, 
            "question_3": answer_3, 
            "question_4": answer_4, 
            "question_5": answer_5, 
            "question_6": answer_6, 
            "question_7": answer_7, 
            "question_8": answer_8
        }
    )