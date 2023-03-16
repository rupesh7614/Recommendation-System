import pandas as pd
import streamlit as st
import pandas
import numpy
import pickle

model = pickle.load(open("df_dict.pkl","rb"))
similarity = pickle.load(open("similarity.pkl","rb"))

movies = pd.DataFrame(model)



def recommend(movie):
    text = movies[movies['title'] == movie].index[0]
    movie_list = sorted(list(enumerate(similarity[text])), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies=[]
    for i in movie_list:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies



st.title("recomender system")

option = st.selectbox(
    'what would like to recommended',
    movies['title'].values )




if st.button('Recommend'):
    recommendation = recommend(option)
    for i in recommendation:
        st.write(i)




