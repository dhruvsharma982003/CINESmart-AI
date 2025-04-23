import streamlit as st
from pymongo import MongoClient

def app():
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

    st.title("Account")

    choice = st.selectbox("Select an option", ["Login", "Sign Up"])
    
    def connect_to_mongo():
        client = MongoClient("mongodb://localhost:27017/")
        db = client["movie_database"]
        collection = db["users"]
        return db, collection
    
    
    if choice == "Login":
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            db, collection = connect_to_mongo()
            user = collection.find_one({"username": username})
            if user and user["password"] == password:
                st.success("Login successful!")
                # Add additional functionality for logged-in users here
            else:
                st.error("Invalid username or password.")
    elif choice == "Sign Up":
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        email = st.text_input("Email")
        if st.button("Sign Up"):
            if username and password and email:
                db, collection = connect_to_mongo()
                data = {
                    "username": username,
                    "password": password,
                    "email": email
                }
                collection.insert_one(data)
                st.success("Sign up successful! You can now log in.")
            else:
                st.error("Please fill in all fields.")
     
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
        <a href="mailto:DhruvSharma1234asd@gmail.com.com">Contact Us</a>
        <a>About Us</a></p>
    </div>
    """,
    unsafe_allow_html=True
)  