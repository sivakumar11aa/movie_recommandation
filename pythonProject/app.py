import streamlit as st
import pickle
import pandas as pd

import base64

import plotly.express as px



def recomand(movie):


        movie_index = movies[movies['title'] == movie].index[0]
        distance = similarity[movie_index]
        movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

        recommend_movies=[]

        recommended_movies_poster = []
        for i in movie_list:

            recommend_movies.append(movies.iloc[i[0]].title)


        return  recommend_movies
movie_dict=pickle.load(open('movie_dic.pkl','rb'))
movies=pd.DataFrame(movie_dict)

st.title("movie recomand system")
similarity=pickle.load(open('similarity.pkl','rb'))
#title = st.text_input("", "Life of Brian")
movie_list = movies['title'].values
select_movies =st.selectbox("enter the movie",movie_list)

if st.button('recomand'):
   recommendations=recomand(select_movies)
   for i in recommendations:
       st.write(i)


def add_bg_from_local():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://images.pexels.com/photos/2387819/pexels-photo-2387819.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local()