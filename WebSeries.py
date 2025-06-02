import streamlit as st
import requests
import pandas as pd
import pickle
import time

def app(): 

    def show_poster(series):
        url = f"https://www.omdbapi.com/?t={series}&apikey=7d86b5a4"
        response = requests.get(url)
        data = response.json()
        poster_path = data.get('Poster', 'https://via.placeholder.com/150')  # Default placeholder if no poster is found
        return poster_path
    
    def get_recommendations(series):
        series_index = df[df['Series Title'] == series].index[0]
        distances = sorted(list(enumerate(similarity[series_index])), reverse=True, key=lambda x: x[1])
        recommended_series = []
        for i in distances[1:6]:
            recommended_series.append(df.iloc[i[0]]['Series Title'])
        return recommended_series
    

    st.markdown("<h1 style='text-align:center; color: white;'>WebSeries</h1>", unsafe_allow_html=True)

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

    WebSeries = pickle.load(open('df3_dict.pkl', 'rb'))
    df = pd.DataFrame(WebSeries)
    similarity = pickle.load(open('similarity3.pkl', 'rb'))

    col1, col2, col3 = st.columns([2, 1, 2])  # Adjust width ratio

    with col2:
        selected_series = st.selectbox(
        'Select a Web Series',
        df['Series Title'].values
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
        recommended_series = get_recommendations(selected_series)
        recommended_series_posters = [show_poster(series) for series in recommended_series]
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(recommended_series[0])
            st.image(recommended_series_posters[0])
            # to get web series trailer
            search_params = {
                'part': 'snippet',
                'q': f"{recommended_series[0]} trailer",
                'key': YOUTUBE_API_KEY,
                'type': 'video'
            }
            response = requests.get(YOUTUBE_API_URL, params=search_params)
            data = response.json()
            video_id = data['items'][0]['id']['videoId']
            st.video(YOUTUBE_VIDEO_URL + video_id)
            
        with col2:
            st.text(recommended_series[1])
            st.image(recommended_series_posters[1])
            # to get web series trailer
            search_params = {
                'part': 'snippet',
                'q': f"{recommended_series[1]} trailer",
                'key': YOUTUBE_API_KEY,
                'type': 'video'
            }
            response = requests.get(YOUTUBE_API_URL, params=search_params)
            data = response.json()
            video_id = data['items'][0]['id']['videoId']
            st.video(YOUTUBE_VIDEO_URL + video_id)
            
        with col3:
            st.text(recommended_series[2])
            st.image(recommended_series_posters[2])
            # to get web series trailer
            search_params = {
                'part': 'snippet',
                'q': f"{recommended_series[2]} trailer",
                'key': YOUTUBE_API_KEY,
                'type': 'video'
            }
            response = requests.get(YOUTUBE_API_URL, params=search_params)
            data = response.json()
            video_id = data['items'][0]['id']['videoId']
            st.video(YOUTUBE_VIDEO_URL + video_id)
            
        with col4:
            st.text(recommended_series[3])
            st.image(recommended_series_posters[3])
            # to get web series trailer
            search_params = {
                'part': 'snippet',
                'q': f"{recommended_series[3]} trailer",
                'key': YOUTUBE_API_KEY,
                'type': 'video'
            }
            response = requests.get(YOUTUBE_API_URL, params=search_params)
            data = response.json()
            video_id = data['items'][0]['id']['videoId']
            st.video(YOUTUBE_VIDEO_URL + video_id)
            
        with col5:
            st.text(recommended_series[4])
            st.image(recommended_series_posters[4])
            # to get web series trailer
            search_params = {
                'part': 'snippet',
                'q': f"{recommended_series[4]} trailer",
                'key': YOUTUBE_API_KEY,
                'type': 'video'
            }
            response = requests.get(YOUTUBE_API_URL, params=search_params)
            data = response.json()
            video_id = data['items'][0]['id']['videoId']
            st.video(YOUTUBE_VIDEO_URL + video_id)

    
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
        counter("Total WebSeries", 12109)

    with col2:
        counter("Total genres", 858)

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
    ### **The Smart Way To Pick A Web Series.**

    Choosing the right web series to watch is more than just following trends — it’s about matching your mood, interests, and time investment. Start by identifying the genre you’re currently craving: whether it's mystery, comedy, sci-fi, or drama, knowing your preference narrows your search immediately. Next, check ratings and reviews from trusted platforms but don't rely solely on numbers — read a few short reviews to understand why people liked or disliked it. Always consider the episode length and the total number of seasons; if you have limited time, short and single-season series might suit you better. Watching trailers or pilot episodes is a smart move too — they give you a quick glimpse of storytelling style, pace, and acting quality. Also, factor in the show's creators and actors; if you've enjoyed their past work, chances are higher you'll enjoy this one too. Finally, trust your instincts: if a show doesn’t click with you after an episode or two, it’s perfectly okay to move on. Watching a web series should be exciting, not a commitment you feel forced to finish.
                
    ### Why Makes This Web Series Recommendation Engine Unique?
    1. Personalized Matching:
    It analyzes individual user preferences (genre, language, actors, ratings) to deliver truly tailored recommendations.

    2. Emotion & Mood Based Suggestions:
    Goes beyond genre — recommends based on your current mood (thrilling, light-hearted, emotional, etc.).

    3. AI-Powered Smart Learning:
    Continuously improves suggestions as you watch, rate, and interact more with the platform.

    4. Multi-Platform Integration:
    Recommends shows available across different streaming services (Netflix, Amazon Prime, Disney+, etc.), not tied to just one.

    5. Rich Metadata Usage:
    Considers deep factors like director style, screenplay tone, soundtrack feel, and audience reviews — not just superficial tags.
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
