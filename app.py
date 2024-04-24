import streamlit as st
import pickle
import requests

movies = pickle.load(open("movies_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))
movies_list = movies['title'].values

def fetch_movie_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{movie_id}?api_key=a9c57462be79d0d2250a2a0d6074122c"
    data = requests.get(url, proxies=proxies)
    data = data.json()
    poster_path = data['poster_path']

    return "https://image.tmdb.org/t/p/w500/"+poster_path

st.header("Movies Recommendation System")
selected_movie = st.selectbox("Select a movie", movies_list)

def recommend(movie):
    index = movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])

    recommendations = []
    posters = []
    # Top-5 similars
    for i in distance[1:11]:
        m_id = movies.iloc[i[0]].id
        recommendations.append(movies.iloc[i[0]].title)
        posters.append(fetch_movie_poster(m_id))
    
    return recommendations, posters

if st.button("Get Recommendations"):
    mnames, mposters = recommend(selected_movie)
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)

    with col1:
        st.text(mnames[0])
        st.image(mposters[0])
    with col2:
        st.text(mnames[1])
        st.image(mposters[1])
    with col3:
        st.text(mnames[2])
        st.image(mposters[2])
    with col4:
        st.text(mnames[3])
        st.image(mposters[3])
    with col5:
        st.text(mnames[4])
        st.image(mposters[4])
    with col6:
        st.text(mnames[5])
        st.image(mposters[5])
    with col7:
        st.text(mnames[6])
        st.image(mposters[6])
    with col8:
        st.text(mnames[7])
        st.image(mposters[7])
    with col9:
        st.text(mnames[8])
        st.image(mposters[8])
    with col10:
        st.text(mnames[9])
        st.image(mposters[9])
    