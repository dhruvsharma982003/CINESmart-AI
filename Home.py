import streamlit as st
# to use OMDB API for trending movies pictures
import requests
import pandas as pd
import pickle 
import random
import time

def app(): 
    def fetch_poster(movie):
        url = f"https://www.omdbapi.com/?t={movie}&apikey=7d86b5a4"
        response = requests.get(url)
        data = response.json()
        poster_path = data.get('Poster', 'https://via.placeholder.com/150')  # Default placeholder if no poster is found
        return poster_path
    
    def get_recommendations(title):
        index = new_df[new_df['title'] == title].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        for i in distances[1:6]:
            print(new_df.iloc[i[0]].title)
        recommended_movies = [new_df.iloc[i[0]].title for i in distances[1:6]]
        return recommended_movies
    
    movie = pickle.load(open('movie_dict.pkl','rb'))
    new_df = pd.DataFrame(movie)
    similarity = pickle.load(open('similarity.pkl','rb'))

    st.markdown("<h1 style='text-align: center; color: white;'>Welcome to CINE SMART AI - Your Personalized Movie Guide</h1>", unsafe_allow_html=True)

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

    movies_list = new_df['title'].values

    # Use columns to center and limit the width
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        selected_movie = st.selectbox(
        "Type or select a movie from the dropdown",
        movies_list
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


    if st.button("Recommend"):
        recommended_movies = get_recommendations(selected_movie)
        recommended_movies_posters = [fetch_poster(movie) for movie in recommended_movies]
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(recommended_movies[0])
            st.image(recommended_movies_posters[0])
             # to get the movie trailers
        search_params = {
            'part': 'snippet',
            'q': f"{recommended_movies[0]} trailer",
            'key': YOUTUBE_API_KEY,
            'type': 'video',
            'maxResults': 1
        }
        response = requests.get(YOUTUBE_API_URL, params=search_params)
        video_id = response.json()['items'][0]['id']['videoId']
        st.video(YOUTUBE_VIDEO_URL + video_id)
        
        with col2:
            st.text(recommended_movies[1])
            st.image(recommended_movies_posters[1])
            # to get the movie trailers
        search_params = {
            'part': 'snippet',
            'q': f"{recommended_movies[1]} trailer",
            'key': YOUTUBE_API_KEY,
            'type': 'video',
            'maxResults': 1
        }
        response = requests.get(YOUTUBE_API_URL, params=search_params)
        video_id = response.json()['items'][0]['id']['videoId']
        st.video(YOUTUBE_VIDEO_URL + video_id)
        
        with col3:
            st.text(recommended_movies[2])
            st.image(recommended_movies_posters[2])
            # to get the movie trailers
        search_params = {
            'part': 'snippet',
            'q': f"{recommended_movies[2]} trailer",
            'key': YOUTUBE_API_KEY,
            'type': 'video',
            'maxResults': 1
        }
        response = requests.get(YOUTUBE_API_URL, params=search_params)
        video_id = response.json()['items'][0]['id']['videoId']
        st.video(YOUTUBE_VIDEO_URL + video_id)
        
        with col4:
            st.text(recommended_movies[3])
            st.image(recommended_movies_posters[3])
            # to get the movie trailers
        search_params = {
            'part': 'snippet',
            'q': f"{recommended_movies[3]} trailer",
            'key': YOUTUBE_API_KEY,
            'type': 'video',
            'maxResults': 1
        }
        response = requests.get(YOUTUBE_API_URL, params=search_params)
        video_id = response.json()['items'][0]['id']['videoId']    
        st.video(YOUTUBE_VIDEO_URL + video_id)
        
        with col5:
            st.text(recommended_movies[4])
            st.image(recommended_movies_posters[4])
            # to get the movie trailers
        search_params = {
            'part': 'snippet',
            'q': f"{recommended_movies[4]} trailer",
            'key': YOUTUBE_API_KEY,
            'type': 'video',
            'maxResults': 1
        }
        response = requests.get(YOUTUBE_API_URL, params=search_params)
        video_id = response.json()['items'][0]['id']['videoId']
        st.video(YOUTUBE_VIDEO_URL + video_id)
        
        # to load the dataset
    df = pd.read_csv('Movies.csv')

    # # to count total movies, genres, languages
    # total_movies = df.shape[0]
    # total_genres = df['genres'].nunique()
    # total_languages = df['original_language'].nunique()

    # # streamlit layout

    # col1, col2, col3 = st.columns(3)

    # with col1:
    #     st.markdown(f"""
    #     <div style='text-align: center;'>
    #         <h1 style='color: #E74C3C;'>{total_movies}</h1>
    #         <p style='font-size:18px; color: white;'>MOVIES</p>
    #     </div>
    # """, unsafe_allow_html=True)

    # with col2:
    #     st.markdown(f"""
    #     <div style='text-align: center;'>
    #         <h1 style='color: #E74C3C;'>{total_genres}</h1>
    #         <p style='font-size:18px; color: white;'>GENRES</p>
    #     </div>
    # """, unsafe_allow_html=True)

    # with col3:
    #     st.markdown(f"""
    #     <div style='text-align: center;'>
    #         <h1 style='color: #E74C3C;'>{total_languages}</h1>
    #         <p style='font-size:18px; color: white;'>LANGUAGES</p>
    #     </div>
    # """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

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

    # Create the three counters
    with col1:
        counter("Total Movies", 4803)

    with col2:
        counter("Total Genres", 1175)

    with col3:
        counter("Total Languages", 37)

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
    ### **The Smart Way To Pick A Movie.**

    Choosing the perfect movie isn't just about scrolling endlessly or relying on random picks — it's about finding something that truly matches your mood, preferences, and occasion. A smart movie recommendation system simplifies this by analyzing your favorite genres, past watches, trending content, and even special categories like "based on true stories" or "best for movie dates." Instead of wasting time browsing, the system learns your taste and narrows down choices that align with your interests. Whether you’re in the mood for an action-packed thriller, a heartfelt romance, or an inspiring documentary, smart recommendations help you discover high-quality movies you might’ve missed — all tailored to your viewing style. It’s like having a personal movie expert who knows exactly what to suggest, every time you hit play.
                
    ### Why Makes This Movie Recommendation Engine Unique?
    * all listed movies are hand-picked and manually tagged by film connoisseurs ensuring high quality recommendations
    * even your mood and the occasion are considered in the movie suggestion
    * NEW: you can now watch movie trailers directly on our website
    * you get only one recommendation at a time, so there isn’t a hard decision again (there is a button to get the next recommendation)
    * new movies are added consistently
    * special recommendations for movie dates: these movies are perfect for dates & will help you to make a good impression on your crush
    * special categories: movies based on true stories or books, Spy Movies, Cop Movies, Heist Movies, Girl Power Movies, Racing Movies, Space Movies, Wedding Movies, IMDb Top 250 movies, movies set in New York, movies set in Las Vegas, movies that may change the way you look at life …
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
