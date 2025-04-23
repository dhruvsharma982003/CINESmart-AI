import streamlit as st
import requests
import pandas as pd
import pickle

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

    selected_series = st.selectbox(
        'Select a Web Series',
        df['Series Title'].values
    )

    if st.button('Recommend'):
        recommended_series = get_recommendations(selected_series)
        recommended_series_posters = [show_poster(series) for series in recommended_series]
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(recommended_series[0])
            st.image(recommended_series_posters[0])
        with col2:
            st.text(recommended_series[1])
            st.image(recommended_series_posters[1])
        with col3:
            st.text(recommended_series[2])
            st.image(recommended_series_posters[2])
        with col4:
            st.text(recommended_series[3])
            st.image(recommended_series_posters[3])
        with col5:
            st.text(recommended_series[4])
            st.image(recommended_series_posters[4])
    
        
    
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