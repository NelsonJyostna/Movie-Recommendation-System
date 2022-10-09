import streamlit as st
import pickle
import pandas as pd
import requests


# First open an account in tmdb and create API Key

# Fetch_Poster
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=200a7042ea6ba4e6f4e1c92f1cfbb3bb&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']   # TMDB image path + json viewer poster path



# Recommend function
def recommend(movi):
    mask = movies['title'] == movi
    movi_index = movies[mask].index[0]
    distances = similarity[movi_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]  # sorted nearest 5 vectors

    recommended_movies = []
    recommended_poster_movies = []

    for i in movies_list:  # In movies_List 5 movies (5 vectors) are came
        movies_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        # fetch_poster function call and forward movie_id to above function fetch_poster
        recommended_poster_movies.append(fetch_poster(movies_id))
    return recommended_movies, recommended_poster_movies





movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)


similarity = pickle.load(open('similarity.pkl', 'rb'))




# title
st.title('Movie Recommender System')


#  Select_box
selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)


# Button
if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    #for i in recommendations:
     #   st.write(i)
     # Layout Your App  for image container in website
    col1, col2, col3 , col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])