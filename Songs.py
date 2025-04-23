import streamlit as st
import pandas as pd
import pickle
import requests

def app():
    
    def fetch_poster(title):
        url = f"https://www.omdbapi.com/?t={title}&apikey=7d86b5a4"
        response = requests.get(url)
        data = response.json()
        poster_path = data.get('Poster', 'https://via.placeholder.com/150')
        return poster_path 

    # to define recommendation using similarity score
    def get_recommendations(title):
        index = df[df['song'] == title].index[0]
        distances = similarity[index]
        song_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
        for i in song_list:
            print(df.iloc[i[0]].song)
        recommended_songs = [df.iloc[i[0]].song for i in song_list]
        return recommended_songs

    st.markdown("<h1 style='text-align:center; color: white;'>Songs</h1>", unsafe_allow_html=True)

    st.markdown( 
        """
        <style>
        .stApp {
            background-image: url("https://img.freepik.com/free-vector/dark-black-background-design-with-stripes_1017-38064.jpg?t=st=1743092096~exp=1743095696~hmac=3e78af6bfb6684f0aee52a6c13563ecf115a23ce36b6b02018ab2bb9934f7173&w=996");
            background-attachment: fixed;
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    music = pickle.load(open('df2_dict.pkl','rb'))
    df = pd.DataFrame(music)
    similarity = pickle.load(open('similarity2.pkl','rb'))

    song_list = df['song'].values
    

    selected_song_name = st.selectbox(
        "Select a song",
        song_list
    )

    if st.button('Recommend'):
        recommended_songs = get_recommendations(selected_song_name)
        recommended_songs_posters = [fetch_poster(i[0]) for i in recommended_songs]
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(recommended_songs[0])    
            st.image(recommended_songs_posters[0])
        with col2:
            st.text(recommended_songs[1])    
            st.image(recommended_songs_posters[1])
        with col3:
            st.text(recommended_songs[2])    
            st.image(recommended_songs_posters[2])
        with col4:
            st.text(recommended_songs[3])    
            st.image(recommended_songs_posters[3])
        with col5:
            st.text(recommended_songs[4])    
            st.image(recommended_songs_posters[4])
    

    st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #262730;
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    .footer a {
        color: #4db8ff;
        text-decoration: none;
        margin: 0 10px;
    }
    </style>
    <div class="footer">
        <p>© 2025 CINESmart AI | <a href="https://github.com/dhruvsharma982003" target="_blank">GitHub</a> | 
        <a href="www.linkedin.com/in/dhruv-sharma-116001229" target="_blank">LinkedIn</a> | 
        <a href="mailto:DhruvSharma1234asd@gmail.com.com">Contact Us</a></p>
    </div>
    """,
    unsafe_allow_html=True
) 