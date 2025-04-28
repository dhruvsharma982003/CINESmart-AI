# to make front end  or UI of CINESmart AI[Movie Recommnedation System]

import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import Home, Account, Songs, WebSeries

st.set_page_config(page_title="CINE SMART AI", page_icon=":movie_camera:", layout="wide")

# to make multipage website
class MultiPage:
    def __init__(self):
        self.pages = []
        self.navbar = None

    def add_page(self, title, func):
        self.pages.append({"title": title, "function": func})    

    def run():
        st.markdown(
    """
    <style>
    .header-container {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 30px;
    }
    .logo-text {
        font-size: 40px;
        font-weight: bold;
        color: white;
        font-family: 'Arial', sans-serif;
    }
    .logo-img {
        width: 60px;
        height: 60px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

    # Assuming you have a logo image
        st.markdown(
            """
            <div class="header-container">
                <img src="https://sdmntprwestus.oaiusercontent.com/files/00000000-8554-6230-8c89-67998e956a86/raw?se=2025-04-28T13%3A02%3A03Z&sp=r&sv=2024-08-04&sr=b&scid=30605222-5d63-5f71-b72b-3078fe56bea0&skoid=a47cd303-16a2-427e-8efb-2ce406116005&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-04-28T11%3A24%3A02Z&ske=2025-04-29T11%3A24%3A02Z&sks=b&skv=2024-08-04&sig=QzknEso6bDPtQccUEYM7ZUPs4XVtGcvtaSZAkhxJxNk%3D" class="logo-img" alt="Logo">
                <div class="logo-text">CINESmart AI</div>
            </div>
            """,
            unsafe_allow_html=True
        )


        app = option_menu(
            menu_title=None,
            options=["Home", "Account", "Songs", "WebSeries","Facebook", "Instagram", "Youtube"],
            icons=["house", "person", "music-note-beamed", "tv", "facebook", "instagram", "youtube"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
            styles={
                "container": {"padding": "0 !important", "background-color": "#262730"},
                "icon": {"color": "white", "font-size": "20px"},
                "nav-link": {"font-size": "18px", "text-align": "center", "margin": "0px", "--hover-color": "#4C4F69",},
                "nav-link-selected": {"background-color": "#ff4b4b"},
                }
        )
        

        if app == "Home":
            Home.app()
        elif app == "Account":
            Account.app()
        elif app == "Songs":
            Songs.app()
        elif app == "WebSeries":
            WebSeries.app()

        elif app == "Facebook":

            st.markdown(
        "[🌐 Follow us on Facebook](https://www.facebook.com/profile.php?id=100074248155882)",
        unsafe_allow_html=True
    )
            
        elif app == "Instagram":
            st.markdown(
        "[🌐 Follow us on Instagram](https://www.instagram.com/dhruvsharma311003/)",
        unsafe_allow_html=True
    )

        elif app == "Youtube":

            st.markdown(
                "[Youtube](https://www.youtube.com/)",
                unsafe_allow_html=True
            )

                
            st.markdown(
                """
                <style>
                .stApp {
                    background-color: #262730;
                }
                .stButton > button {
                    background-color: #ff4b4b;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    padding: 10px 20px;
                    font-size: 16px;
                    cursor: pointer;
                }
                .stButton > button:hover {
                    background-color: #4C4F69;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
        

    run()
