import json
import streamlit as st

@st.cache_data
def load_team_data():
    file_path = "./assets/team/config.json"
    with open(file_path, mode="r", encoding="utf-8") as fp:
        team_data = json.load(fp)
    return team_data

def display_member(member_name, user_name, image_url, twitter_handle, \
    linkedin_handle, github_handle, description):
    
    st.write(f"<h4 style='text-align:center'>{member_name}</h4>", \
        unsafe_allow_html=True)
    with st.container():
        ml, mn, mr = st.columns([4, 10, 4])
        with mn:
            st.image(image_url, width=200)
    st.write(f"<p style='text-align:center'>\
        <a style='color:blue' href='https://twitter.com/{twitter_handle}'>Twitter</a>\
            | <a style='color:blue' href='https://linkedin.com/in/{linkedin_handle}'>\
                LinkedIn</a> | <a style='color:blue' href='https://github.com/{github_handle}'>\
                    GitHub</a></p>", unsafe_allow_html=True)
    
    st.write(f"<p style='text-align:center'>{description}<br>\
            <small style='color:#006a08;'>@{user_name}</small></p>", 
             unsafe_allow_html=True)

def main():
    st.set_page_config(page_icon="favicon.ico", page_title="Agri Brain | -team", layout='wide')    
    st.markdown("<center> <h1> The AgriBrain Team </h1> </center>", 
                unsafe_allow_html=True)
    st.write('-------------------------')

    team = load_team_data()
    benkimz, davies = team["members"]
    
    col1, col2 = st.columns([1, 1])

    with col1:
        display_member(
            member_name=benkimz["name"], 
            user_name=benkimz["username"], 
            image_url=benkimz["icon"], 
            twitter_handle=benkimz["twitter"], 
            linkedin_handle=benkimz["linkedin"], 
            github_handle=benkimz["github"], 
            description=benkimz["description"]
        )
    with col2:
        display_member(
            member_name=davies["name"], 
            user_name=davies["username"], 
            image_url=davies["icon"], 
            twitter_handle=davies["twitter"], 
            linkedin_handle=davies["linkedin"], 
            github_handle=davies["github"], 
            description=davies["description"]
        )


if __name__ == '__main__':
    main()
    
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
        /*div[data-testid=stToolbar]{
            display: none!important;
        }*/
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
