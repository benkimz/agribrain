import os
import json
import pandas as pd
import streamlit as st

st.set_page_config(
    page_icon=":star:", 
    page_title="AgriBrain Data Logger", 
    layout="wide"
)


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

main, right = st.columns([6, 1])

with main:
    st.title("AgriBrain Data Logger: ")

    with open("contexts.json", mode="r", encoding="utf-8") as fp: 
        context_tags = json.load(fp)
        
    context_tags = tuple(sorted(set(context_tags)))

    record_fields = {
        "question": "*", 
        "context": "*", 
        "answer": "*",  
        "keywords": "*", 
        "category": "*", 
        "intent": "*", 
        "procedure": "*"
    }

    question = st.text_input(
        label="Question: ", 
        placeholder="Questions comes here...", 
        autocomplete="off"
    )

    context_tag = st.selectbox(
        label="Suitable Answer Context: ", 
        options=context_tags
    )

    answer = st.text_area(
        label="Suitable Answer: ", 
        placeholder="Answer goes here...", 
        height=110
    )
    
    keywords = st.text_input(
        label="Keywords: ", 
        placeholder="Keyword 1, Keyword 2, Keyword 3"
    )

    question_category = st.selectbox(
        label="Question Category: ", 
        options=(
            "crop cultivation", 
            "livestock keeping", 
            "market related", 
            "weather queries", 
            "agricultural agencies", 
            "consumer questions", 
            "general questions"
        )
    )

    intent = st.selectbox(
        label="Intent: ", 
        options=(
            "clear a doubt", 
            "have fun", 
            "know why", 
            "know how", 
            "know where", 
            "know when", 
            "know what", 
            "curious to know more", 
            "get insights", 
            "critic"
        )
    )

    include_a_step_procedure = st.selectbox(
        label="Requires procedure: ", 
        options=(True, False)
    )
    
    save_button = st.button(label="Save Data")

    response_file = "./questions.csv"

    def save_data(**kwargs):
        for index, item in enumerate(kwargs.items()):
            question_tag, answer = item
            if type(answer) == str:
                answer = answer.strip()
        if not os.path.exists(response_file): 
            open(response_file, mode="w")
        if os.path.getsize(response_file) == 0:
            columns = list(record_fields.keys())
            df = pd.DataFrame(columns=columns)
        else: df = pd.read_csv(response_file)
        rows, cols = df.shape
        df.loc[rows, :] = list(kwargs.values())
        df.to_csv(response_file, index=False)
        st.success("Response saved successfully!")
        with right:
            entries, _ = df.shape
            st.markdown(
            """
            #### Progress:
            ---
            Total entries: {}
            """.format(entries)
            )
        
    if save_button:
        save_data(
            **{
                "question": question, 
                "context": context_tag, 
                "answer": answer, 
                "keywords": keywords, 
                "category": question_category, 
                "intent": intent, 
                "procedure": include_a_step_procedure
            }
        )