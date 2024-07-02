import pickle

import streamlit as st

import requests

def fetching_poster(moviee_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(moviee_id)

    datta = requests.get(url)

    datta = datta.json()

    postter_path = datta['poster_path']

    full_path = "https://image.tmdb.org/t/p/w500/" + postter_path

    return full_path


def recomMovie(movie):
    indx = moviess[moviess['title'] == movie].index[0]

    distn = sorted(list(enumerate(similar[indx])), reverse=True, key= lambda r: r[1])

    name_of_movie_recommendation = []

    movie_recommended_poster = []

    for r in distn[1:6]:
        movie_id = moviess.iloc[r[0]]['movie_id']
        
        movie_recommended_poster.append(fetching_poster(movie_id))

        name_of_movie_recommendation.append(moviess.iloc[r[0]]['title'])

    return name_of_movie_recommendation, movie_recommended_poster        


st.header("Movie Recommendation System  Website using Machine Learning")

moviess = pickle.load(open('artificatss/movies_list.pkl', 'rb'))

similar = pickle.load(open('artificatss/similarity.pkl', 'rb'))

movie_lists = moviess['title'].values

the_selected_movies = st.selectbox(
    'Type or Select A Particular Movie to Get Some Recommendations', movie_lists)

if  st.button('Showing the Recommendation'):
    name_of_movie_recommendation,movie_recommended_poster = recomMovie(the_selected_movies)

    coln1, coln2, coln3, coln4, coln5 = st.columns(5)
    with coln1:
        st.text(name_of_movie_recommendation[0])
        st.image(movie_recommended_poster[0])
    with coln2:
        st.text(name_of_movie_recommendation[1])
        st.image(movie_recommended_poster[1])

    with coln3:
        st.text(name_of_movie_recommendation[2])
        st.image(movie_recommended_poster[2])
    with coln4:
        st.text(name_of_movie_recommendation[3])
        st.image(movie_recommended_poster[3])
    with coln5:
        st.text(name_of_movie_recommendation[4])
        st.image(movie_recommended_poster[4])