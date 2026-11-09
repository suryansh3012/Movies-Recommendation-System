import streamlit as st
import pickle
import joblib

st.title("Movie Recommandation System")

with open("movies.pickle",'rb') as m:
    movies=pickle.load(m)

similarity=joblib.load("similarity.joblib",'rb')

movie_names=movies['title'].values

def recommend(name_movies):

    movie_index=movies[movies['title']==name_movies].index[0]

    recommendations=similarity[movie_index]

    movie_list=sorted(enumerate(recommendations),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]

    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies



name_movies=st.selectbox("Enter the Movie Name",movie_names)

if st.button("Recommend"):
    r=recommend(name_movies)
    st.write("The Recommended movies are :")

    for i in r:
        st.write(i)



"""1. Libraries
- streamlit – Creates the website.
- pickle – Loads the movie dataset.
- joblib – Loads the similarity matrix.
2. Important code and meanings
Code	        Remember its use
st.title()  	Website heading
pickle.load()	Loads saved dataset
joblib.load()	Loads similarity scores
movies['title']	Selects movie title column
.values	        Converts column into an array
def	            Creates a function
.index[0]	    Finds movie index
similarity[index]	Gets similarity scores
enumerate()  	Adds index to scores
sorted()	    Sorts scores
reverse=True	Highest to lowest
lambda x:x[1]	Sorts using similarity score
[1:6]	        Selects 5 movies, skips first
append()	    Adds movie to list
return	        Returns recommended movies
st.selectbox() 	Creates dropdown
st.button()  	Creates button
st.write()   	Displays output

3. Most important concepts
Remember these 5 things:
1. Index: Position of a movie in the dataset.
2. Similarity: How similar two movies are.
3. Enumerate: Combines index and similarity score.
4. Lambda: A shortcut for writing a small function.
5. Return: Sends the result back from a function."""

'''git init
git add .
git commit -m "Message"
git remote add origin URL
git branch -M main
git push -u origin main'''