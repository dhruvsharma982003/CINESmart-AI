import streamlit as st
import pandas as pd
import pickle
import requests
import time

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
    

    col1, col2, col3 = st.columns([2, 1, 2])  # Adjust width ratio

    with col2:
        selected_song_name = st.selectbox(
        "Select a song",
        song_list
    )

    st.markdown("""
    <style>
    .stSelectbox div[data-baseweb="select"] {
        max-width: 100% !important;
    }
    button[kind="primary"] {
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

    YOUTUBE_API_KEY = 'AIzaSyCJPMRlkYiISJIxFgydSbzPqhsjHlLdBD4'
    YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search'
    YOUTUBE_VIDEO_URL = 'https://www.youtube.com/watch?v='

    if st.button('Recommend'):
        recommended_songs = get_recommendations(selected_song_name)
        recommended_songs_posters = [fetch_poster(i[0]) for i in recommended_songs]
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(recommended_songs[0])    
            st.image(recommended_songs_posters[0])

        # to get songs from youtube
            search_params = {
                'part': 'snippet',
                'q': recommended_songs[0],
                'type': 'video',
                'key': YOUTUBE_API_KEY
            }
            response = requests.get(YOUTUBE_API_URL, params=search_params)
            data = response.json()
            video_id = data['items'][0]['id']['videoId']
            st.markdown(f'<iframe width="100%" height="315" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
            st.markdown(f'<a href="{YOUTUBE_VIDEO_URL}{video_id}" target="_blank">Watch on YouTube</a>', unsafe_allow_html=True)
            
        with col2:
            st.text(recommended_songs[1])    
            st.image(recommended_songs_posters[1])
            # to get songs from youtube
            search_params = {
                'part': 'snippet',
                'q': recommended_songs[1],
                'type': 'video',
                'key': YOUTUBE_API_KEY
            }
            response = requests.get(YOUTUBE_API_URL, params=search_params)
            data = response.json()
            video_id = data['items'][0]['id']['videoId']
            st.markdown(f'<iframe width="100%" height="315" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
            st.markdown(f'<a href="{YOUTUBE_VIDEO_URL}{video_id}" target="_blank">Watch on YouTube</a>', unsafe_allow_html=True)
            
        with col3:
            st.text(recommended_songs[2])    
            st.image(recommended_songs_posters[2])
            # to get songs from youtube
            search_params = {
                'part': 'snippet',
                'q': recommended_songs[2],
                'type': 'video',
                'key': YOUTUBE_API_KEY
            }
            response = requests.get(YOUTUBE_API_URL, params=search_params)
            data = response.json()
            video_id = data['items'][0]['id']['videoId']
            st.markdown(f'<iframe width="100%" height="315" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
            st.markdown(f'<a href="{YOUTUBE_VIDEO_URL}{video_id}" target="_blank">Watch on YouTube</a>', unsafe_allow_html=True)
            
        with col4:
            st.text(recommended_songs[3])    
            st.image(recommended_songs_posters[3])
            # to get songs from youtube
            search_params = {
                'part': 'snippet',
                'q': recommended_songs[3],
                'type': 'video',
                'key': YOUTUBE_API_KEY
            }
            response = requests.get(YOUTUBE_API_URL, params=search_params)
            data = response.json()
            video_id = data['items'][0]['id']['videoId']
            st.markdown(f'<iframe width="100%" height="315" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
            st.markdown(f'<a href="{YOUTUBE_VIDEO_URL}{video_id}" target="_blank">Watch on YouTube</a>', unsafe_allow_html=True)
            
        with col5:
            st.text(recommended_songs[4])    
            st.image(recommended_songs_posters[4])
            # to get songs from youtube
            search_params = {
                'part': 'snippet',
                'q': recommended_songs[4],
                'type': 'video',
                'key': YOUTUBE_API_KEY
            }
            response = requests.get(YOUTUBE_API_URL, params=search_params)
            data = response.json()
            video_id = data['items'][0]['id']['videoId']
            st.markdown(f'<iframe width="100%" height="315" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
            st.markdown(f'<a href="{YOUTUBE_VIDEO_URL}{video_id}" target="_blank">Watch on YouTube</a>', unsafe_allow_html=True)

    df = pd.read_csv('Songs Dataset.csv')

    col1, col2 = st.columns(2)

# Function to create a counter animation
    def counter(label, end_value):
        count = 0
        increment = end_value // 100  # adjust speed
        if increment == 0:
            increment = 1
        placeholder = st.empty()
        while count < end_value:
            count += increment
            if count > end_value:
                count = end_value
            placeholder.metric(label, f"{count:,}")
            time.sleep(0.01)

    # Create the two counters
    with col1:
        counter("Total Songs", 57650)

    with col2:
        counter("Total Artists", 643)

        st.markdown(
    """
    <style>
    .card {
        background-color: #1c1c1f;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.3);
        margin: 10px;
    }
    .title {
        font-size: 24px;
        font-weight: bold;
        color: white;
        margin-bottom: 10px;
    }
    .description {
        font-size: 16px;
        color: #d3d3d3;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

    # Create four columns
    col1, col2, col3, col4 = st.columns(4)

    # Column 1 - Recommendations
    with col1:
        st.markdown(
            """
            <div class="card">
                <div class="title">🧭 Recommendations</div>
                <div class="description">Get super accurate recommendations based on your ratings from the users whose taste is closest to yours</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Column 2 - Rate & Review
    with col2:
        st.markdown(
            """
            <div class="card">
                <div class="title">📝 Rate & Review</div>
                <div class="description">Rate everything you watch to build your taste profile, then heap praise or throw shade with reviews</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Column 3 - Track
    with col3:
        st.markdown(
            """
            <div class="card">
                <div class="title">📒 Track</div>
                <div class="description">Keep track of what you watched with your Watchlist, and when you watched it with your own Watch Journal</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Column 4 - Collections
    with col4:
        st.markdown(
            """
            <div class="card">
                <div class="title">🖼️ Collections</div>
                <div class="description">Create your own private collections or collaborate on shared lists with friends on any topic or genre</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("""
    ### **The Smart Way To Pick A Songs.**

    Picking the perfect song smartly is about matching the mood, moment, and meaning you're aiming for. First, think about the purpose — is it for relaxing, hyping up, focusing, or expressing a feeling? Then, consider the vibe you want: upbeat, emotional, chill, energetic, or something else. It's smart to also pay attention to lyrics — pick songs whose words resonate with your situation or enhance the atmosphere you're creating. Genre can guide you too: pop for energy, indie for calm, classical for focus, hip-hop for motivation, and so on. If you're stuck, look at your past favorites or explore curated playlists based on mood or activity. A truly smart pick also considers your audience — what will make everyone feel good or connect instantly? In short, smart song selection is a blend of emotional instinct, purpose, vibe-matching, and a little exploration. 🎵
                
    ### Why Makes This Song Recommendation Engine Unique?
    * What makes this song recommendation engine unique is its ability to deeply understand not just what users like, but why they like it.
    * Instead of only matching basic genres or artists, it analyzes listening patterns, mood preferences, lyrical themes, tempo, and even the emotional tone behind user choices
    * It learns over time, adapting to changing tastes — whether you're looking for comfort, energy, nostalgia, or discovery
    * Unlike typical engines, it doesn’t just recommend the "most popular" songs — it curates truly personal experiences, introducing hidden gems alongside favorites.
    * This smart, evolving understanding creates a much more human-like, intuitive music journey every time you press play.
    """, unsafe_allow_html=True)
    

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
