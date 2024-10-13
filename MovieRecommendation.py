import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(
        page_title="Movie recommendation System",
)

st.title("Movie Recommender System")

def recommend(movie):
    movie_index=movie_list[movie_list['title']==movie].index[0]
    movies_list=sorted(list(enumerate(similarity_list[movie_index])),reverse=True,key=lambda x:x[1])[1:50]
    recommended_movies = []
    for i in movies_list:
        idx=i[0]
        rating=movie_list.iloc[idx].vote_average
        if(rating>=7):
            recommended_movie=movie_list.iloc[idx].title
            recommended_movies.append(recommended_movie)
    return recommended_movies

    # st.write("Recommended Movies: ")
    # print(movies_list)
    # for i in movies_list:
    #     st.write(movies_list.iloc[i[0]].title)


movie_list = pickle.load(open('movies.pkl', 'rb'))
similarity_list = pickle.load(open('similarity.pkl', 'rb'))
movie_list_title = movie_list['title'].values

selected_movie_name = st.selectbox(
'Which Movie You like??', movie_list_title
)
if st.button('Recommend'):
    st.write("Selected Movie: ", selected_movie_name)
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

