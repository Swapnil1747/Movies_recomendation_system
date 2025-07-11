import pickle
import streamlit as st
import requests
import os
import urllib.parse
from dotenv import load_dotenv

# Load .env file
load_dotenv()
omdb_api_key = os.getenv("OMDB_API_KEY")

def fetch_poster(movie_title):
    encoded_title = urllib.parse.quote(movie_title)
    url = f"http://www.omdbapi.com/?t={encoded_title}&apikey={omdb_api_key}"
    response = requests.get(url)
    data = response.json()

    # Optional: show the API response (for debugging)
    # st.write(f"OMDb response for '{movie_title}':", data)

    if data.get("Response") == "True" and data.get("Poster") and data["Poster"] != "N/A":
        return data["Poster"]
    else:
        return "https://via.placeholder.com/300x450?text=No+Image"

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        title = movies.iloc[i[0]].title
        recommended_movie_names.append(title)
        recommended_movie_posters.append(fetch_poster(title))
    return recommended_movie_names, recommended_movie_posters

# Streamlit UI
st.header('🎬 Movie Recommender System')

movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(recommended_movie_names[i])
            st.image(recommended_movie_posters[i])
