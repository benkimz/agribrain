import streamlit as st

from PIL import Image

st.set_page_config(page_title="Weather", page_icon="favicon.ico")

st.markdown(
    """
    <style>
    hr{
        margin: 1px!important;
    }
    h3, h4, h5{
        text-align: center!important;
    }
    header[data-testid=stHeader]{
        background: #006a08!important;
    }
    </style>
    """, unsafe_allow_html=True
)

side_bar = st.sidebar

with side_bar:
    st.markdown(
    """
    ### Weather Today:
    ---    
    Element|Value|Units
    -------|-----|-----
    Min temp|{}|K
    Max temp|{}|K
    Mean temp|{}|K
    Precipitation|{}|mm
    Dewpoint|{}|K
    Surface pressure|{}|hPa
    Mean slp|{}|hPa
    U wind|{}|m/s
    V wind|{}|m/s
    """.format(8, 29, 22, 20, 3, 0.0001, 0.00012, 0.3, 0.05)
    )
    st.markdown(
    """
    ### List of symbols:
    ---
    Symbol|Meaning
    -------|------
    mm|milli meters
    K|Kelvins
    C|Celsius
    hPa|Pascal height
    Pa|Pascal
    m/s|meters per second 
    """
    )
    
banner_image = Image.open(r"assets/banners/solutionchallenge-2023-Website-EventBanners_Full.png")
st.image(banner_image, caption="Google Solutions Challenge -Agri Brain", use_column_width=True) 
st.title("Weather based insights:")
st.markdown(
    """
    ---
    #### Weekly weather forecast:-
    ---
    """
)
st.slider(
    label="Select Day Range: ", 
    max_value=7, 
    min_value=1, 
    step=1
)
st.markdown(
"""
---
#### <center>Suggested crops:</center>
---
""", unsafe_allow_html=True
)
first_row = st.container()
with first_row:
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        tomato = Image.open(r"./assets/images/tomato.jpeg")
        st.image(tomato, caption="Tomato", use_column_width=True)
        st.markdown(
        """
        * direct sunlight
        * temp: 14 - 30 degrees celsius
        * soil pH: 5.5 - 7.5
        """
        )      
    with col2:
        peas = Image.open(r"./assets/images/peas.jpeg")
        st.image(peas, caption="Peas", use_column_width=True)
        st.markdown(
        """
        * temp: 15 - 20 degrees celsius
        * adequate well distributed rainfall
        """
        )          
    with col3:
        cabbage = Image.open(r"./assets/images/cabbage.jpeg")
        st.image(cabbage, caption="Cabbage", use_column_width=True)
        st.markdown(
        """
        * temp: 15 - 20 degrees celsius
        * adequate well distributed rainfall
        """
        )
    with col4:
        maize = Image.open(r"./assets/images/maize.jpeg")
        st.image(maize, caption="Maize", use_column_width=True)
        st.markdown(
        """
        * temp: 15 - 25 degrees celsius
        * average air temperatures
        """
        )                      
       
second_row = st.container()
with second_row:
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        beans = Image.open(r"./assets/images/beans.jpeg")
        st.image(beans, caption="Beans", use_column_width=True)
        st.markdown(
        """
        * direct sunlight
        * temp: 14 - 30 degrees celsius
        * soil pH: 5.5 - 7.5
        """
        )      
    with col2:
        peas = Image.open(r"./assets/images/pumpkins.jpeg")
        st.image(peas, caption="Pumpkins", use_column_width=True)
        st.markdown(
        """
        * temp: 15 - 20 degrees celsius
        * adequate well distributed rainfall
        """
        )          
    with col3:
        cabbage = Image.open(r"./assets/images/oranges.jpeg")
        st.image(cabbage, caption="Oranges", use_column_width=True)
        st.markdown(
        """
        * temp: 15 - 20 degrees celsius
        * adequate well distributed rainfall
        """
        )
    with col4:
        maize = Image.open(r"./assets/images/apples.jpeg")
        st.image(maize, caption="Apples", use_column_width=True)
        st.markdown(
        """
        * temp: 15 - 25 degrees celsius
        * average air temperatures
        """
        )        

st.markdown(
"""
---
#### <center>Suggested livestock:</center>
---
""", unsafe_allow_html=True
)
first_row = st.container()
with first_row:
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        chicken = Image.open(r"./assets/images/chicken.jpeg")
        st.image(chicken, caption="Chicken", use_column_width=True)
        st.markdown(
        """
        * direct sunlight
        * temp: 14 - 30 degrees celsius
        """
        )      
    with col2:
        dairy = Image.open(r"./assets/images/dairy.jpeg")
        st.image(dairy, caption="Dairy", use_column_width=True)
        st.markdown(
        """
        * temp: 15 - 20 degrees celsius
        * adequate well distributed rainfall
        """
        )          
    with col3:
        goats = Image.open(r"./assets/images/goats.jpeg")
        st.image(goats, caption="Goats", use_column_width=True)
        st.markdown(
        """
        * temp: 15 - 20 degrees celsius
        * adequate well distributed rainfall
        """
        )
    with col4:
        sheep = Image.open(r"./assets/images/sheep.jpeg")
        st.image(sheep, caption="Sheep", use_column_width=True)
        st.markdown(
        """
        * temp: 15 - 25 degrees celsius
        * average air temperatures
        """
        )                      
       
second_row = st.container()
with second_row:
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        beef = Image.open(r"./assets/images/beef.jpeg")
        st.image(beef, caption="Beef cattle", use_column_width=True)
        st.markdown(
        """
        * direct sunlight
        * temp: 14 - 30 degrees celsius
        """
        )      
    with col2:
        beef = Image.open(r"./assets/images/pigs.jpeg")
        st.image(beef, caption="Pigs", use_column_width=True)
        st.markdown(
        """
        * direct sunlight
        * temp: 14 - 30 degrees celsius
        """
        )          
    with col3:
        beef = Image.open(r"./assets/images/rabbits.jpeg")
        st.image(beef, caption="Rabbits", use_column_width=True)
        st.markdown(
        """
        * direct sunlight
        * temp: 14 - 30 degrees celsius
        """
        ) 
    with col4:
        beef = Image.open(r"./assets/images/ducks.jpeg")
        st.image(beef, caption="Ducks", use_column_width=True)
        st.markdown(
        """
        * direct sunlight
        * temp: 14 - 30 degrees celsius
        """
        )