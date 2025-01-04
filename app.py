import streamlit as st
from streamlit_option_menu import option_menu
import random
from tmdbv3api import TMDb, Movie, Discover
from IPython.display import Image
from PIL import Image
import requests

from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd
import re

tmdb = TMDb()
tmdb.api_key = '59fa21d4a3485aae1e53d7cb4c21883e'
tmdb.language = "fr"

# Load the image
image = Image.open("logo.png") 

# Create a container
container = st.container()

with container:
    col1, col2 = st.columns([1, 2]) 
    with col1:
        st.image(image)
    with col2:
        st.title("Projet 2 Moving Frame") 
    
with st.sidebar :
    st.title("La région ciblée") 
    st.image("creuse.png")
    st.write("La mise en place du système de recommandation de films est faite pour le compte d'un gérant de cinéma de la Creuse pour lui permettre de sélectionner des films pour ses clients locaux. Les KPIs sont établis afin d'évaluer les films qui pourraient répondre aux préférences locales.") 
    
    st.subheader("Contactez-nous")
    with st.form("reply_form"):
        name = st.text_input("Nom")
        email = st.text_input("Email")
        phone = st.text_input("Téléphone")
        message = st.text_area("Ecrivez un méssage")
        submitted = st.form_submit_button("Soumettre")
        if submitted:
            st.success("Mercie pour votre réponse!")

    st.subheader("Postuler un commentaire")
    with st.form("comment_form"):
        comment = st.text_area("Votre commentaire")
        submitted = st.form_submit_button("Postuler")
        if submitted:
            st.success("Commentaire est postulé avec succès!") 


selection = option_menu(
        menu_title=None,
        options=["Accueil", "Recherche", "Notre Équipe", "Notre Site"],
        icons=["🏠", "🔭", "📷", "🖼️"],
        menu_icon="menu-app",
        default_index=0,
        orientation="horizontal",
    )

# Affichage du contenu en fonction de la sélection
if selection == "Accueil":
    st.write("# Bienvenue sur notre site!")

    st.write(""" 
        **Moving Frame comme Vision Dynamique**
        
        Imaginez une grande fenêtre sur un paysage en constante évolution. Cette fenêtre, que nous appellerons le Moving Frame, n'est pas statique. 
        Elle se déplace, s'ajuste et se réoriente en fonction des besoins du moment. 
        Ce cadre mouvant permet d'attraper les meilleures vues possibles à tout instant.

    """)

    # Initialize the Discover class
    discover = Discover()

    # Search for popular movies using the Discover object
    search_results = discover.discover_movies({"sort_by": "popularity.desc"})

    # Convert search_results to a list (if not already a list)
    search_results_list = list(search_results)

    # Ensure there are at least 10 movies to sample
    if len(search_results_list) < 10:
        print("Not enough movies to sample.")
    else:
        # Randomly select 10 movies from the results
        random_movies = random.sample(search_results_list, 6)

        # Initialize the Movie class for fetching details
        movie_search = Movie()

        movies = []
        # Loop through the selected movies and display their details
        for movie in random_movies:
            movie_id = movie.id
            # Get movie details
            movie_details = movie_search.details(movie_id)
            movies.append(movie.title)

    # Fonction pour récupérer l'image du film
    def get_movie_poster(movie_name):
          movie_search = Movie()
          search_results = movie_search.search(movie_name)  # Rechercher le film
          if search_results:
              movie_id = search_results[0].id
              movie_details = movie_search.details(movie_id)
              poster_path = movie_details.poster_path
              if poster_path:
                  return f"https://image.tmdb.org/t/p/w500/{poster_path}"
          return None

    # Télécharger et afficher les images
    cols = st.columns(3)  # Diviser l'écran en 3 colonnes
    for i, movie_name in enumerate(movies):
        with cols[i % 3]:  # Répartir les films dans les colonnes
            poster_url = get_movie_poster(movie_name)
            if poster_url:
                st.image( poster_url,caption=movie_name)
            else:
                st.write("Affiche non disponible")

elif selection == "Recherche": 

  # Charger le dataframe (df) contenant les films
  @st.cache_data
  def load_data():
      return pd.read_parquet('data.parquet')  # Remplacez par le chemin vers votre fichier
  df = load_data()
  # Préparer les données pour le modèle
  @st.cache_data
  def prepare_data(df):
      # Colonnes textuelles
      text_cols = ['overview', 'title', 'original_title', 'production_companies_name',
                  'actor', 'director']
      tfidf_matrices = [TfidfVectorizer().fit_transform(df[col].fillna('')).toarray() for col in text_cols]
      tfidf_combined_dense = np.concatenate(tfidf_matrices, axis=1)
      # Colonnes catégoriques
      cat_cols = ['genres', 'original_language', 'production_countries', 'spoken_languages']
      one_hot_encoded = pd.get_dummies(df[cat_cols], columns=cat_cols).values
      # Colonnes numériques
      num_cols = ['budget', 'popularity', 'revenue', 'runtime', 'vote_average', 'vote_count']
      scaler = StandardScaler()
      num_scaled = scaler.fit_transform(df[num_cols])
      # Combiner toutes les caractéristiques
      X_combined = np.concatenate([tfidf_combined_dense, one_hot_encoded, num_scaled], axis=1)
      return X_combined
  X_combined = prepare_data(df)
  # Entraîner le modèle KNN
  @st.cache_resource
  def train_knn(X_combined):
      knn_model = NearestNeighbors(metric='cosine', algorithm='brute')
      knn_model.fit(X_combined)
      return knn_model
  knn_model = train_knn(X_combined)
  # Fonction pour recommander des films
  def recommend_movies_knn(movie_id, knn_model, df, X_combined, top_n=10):
      try:
          idx = df[df['imdb_id'] == movie_id].index[0]
          distances, indices = knn_model.kneighbors(X_combined[idx].reshape(1, -1), n_neighbors=top_n + 1)
          similar_movies = df.iloc[indices.flatten()[1:]]  # Exclure le film lui-même
          return similar_movies[['imdb_id', 'title','poster_url','genres', 'actor', 'director']].drop_duplicates()  # Supprimer les doublons
      except IndexError:
          return None

  # Interface Streamlit
  st.title("Recommandation de films")
  st.write("Choississez et entrez un titre ou un(e) acteur/actrice d'un film pour obtenir des recommandations.")
  search_type = st.radio("Rechercher par :", ["Titre", "Acteur(trice)"])

  # Entrée utilisateur pour le titre du film
  if search_type == "Titre":
    movie_title = st.text_input("Titre du film", "")
    if st.button("Recommander des films par le titre"):
        if movie_title.strip() == "":
            st.warning("Veuillez entrer un titre de film.")
        else:
            # Trouver le film dans le DataFrame
            matching_movies = df[df['title'].str.contains(movie_title, case=False, na=False)]
            if matching_movies.empty:
                st.error("Désolé, aucun film trouvé avec ce titre.")
            else:
                # Utiliser le premier résultat correspondant pour la recommandation
                selected_movie = matching_movies.iloc[0]
                st.write(f"Recommandations pour : **{selected_movie['title']}**")
                # Obtenir des recommandations
                imdb_id = selected_movie['imdb_id']
                recommended_movies = recommend_movies_knn(imdb_id, knn_model, df, X_combined, top_n=10)
                movies = recommended_movies['title'].tolist()
                if recommended_movies is not None and not recommended_movies.empty:               
                  def get_movie_poster(movie_name):
                      movie_search = Movie()
                      search_results = movie_search.search(movie_name)  # Rechercher le film
                      if search_results:
                          movie_id = search_results[0].id
                          movie_details = movie_search.details(movie_id)
                          poster_path = movie_details.poster_path
                          if poster_path:
                              return f"https://image.tmdb.org/t/p/w500/{poster_path}"
                      return None
                  def get_movie_comment(movie_name):
                  #Récupère le résumé du film.
                    movie_search = Movie()
                    search_results = movie_search.search(movie_name)
                    if search_results:
                      movie_id = search_results[0].id
                      url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={tmdb.api_key}&language={tmdb.language}"
                      response = requests.get(url)
                      if response.status_code == 200:
                          rep = response.json()
                          return rep.get('overview', 'Aucun résumé disponible.')
                    return "Résumé non disponible."
                  
                  for movie_name in movies:
                    poster_url = get_movie_poster(movie_name)
                    comment = get_movie_comment(movie_name)

                  # Organisation en colonnes : image à gauche, texte à droite
                    col1, col2 = st.columns([1, 2])  # Largeur 1:2
                    with col1:
                      if poster_url:
                        st.image(poster_url, caption=movie_name)
                      else:
                        st.write("Affiche non disponible")
                    with col2:
                      st.write(f"**{movie_name}**")
                      st.write(comment)
                else:
                    st.error("Impossible de générer des recommandations pour ce film.")

  else:
    # Entrée utilisateur pour l'acteur du film
    movie_actor = st.text_input("Acteur(trice) du film", "")
    if st.button("Recommander des films par l'acteur(trice)"):
        if movie_actor.strip() == "":
            st.warning("Veuillez entrer un acteur de film.")
        else:
            # Trouver les films dans le DataFrame où l'acteur correspond
            matching_movies = df[df['actor'].str.contains(movie_actor, case=False, na=False)]
            if matching_movies.empty:
                st.error("Désolé, aucun film trouvé avec cet acteur.")
            else:
                # Utiliser le premier résultat correspondant pour la recommandation
                selected_movie = matching_movies.iloc[0]
                # Extraire la partie de l'acteur correspondant au mot-clé
                actor_names = selected_movie['actor'].split(', ')
                matched_actor = next((actor for actor in actor_names if re.search(movie_actor, actor, re.IGNORECASE)), None)
                # Afficher le nom de l'acteur correspondant
                if matched_actor:
                    st.write(f"Recommandations pour : **{matched_actor}**")
                else:
                    st.write(f"Recommandations pour : **{selected_movie['actor']}**")
                # Afficher les premiers films de l'acteur
                displayed_movies = matching_movies[['imdb_id', 'title','poster_url', 'genres', 'actor', 'director']].head(10)
                movies = displayed_movies['title'].tolist()
                if displayed_movies is not None and not displayed_movies.empty:
                  def get_movie_poster(movie_name):
                      movie_search = Movie()
                      search_results = movie_search.search(movie_name)  # Rechercher le film
                      if search_results:
                          movie_id = search_results[0].id
                          movie_details = movie_search.details(movie_id)
                          poster_path = movie_details.poster_path
                          if poster_path:
                              return f"https://image.tmdb.org/t/p/w500/{poster_path}"
                      return None
                  
                  def get_movie_comment(movie_name):
                  #Récupère le résumé du film.
                    movie_search = Movie()
                    search_results = movie_search.search(movie_name)
                    if search_results:
                      movie_id = search_results[0].id
                      url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={tmdb.api_key}&language={tmdb.language}"
                      response = requests.get(url)
                      if response.status_code == 200:
                          rep = response.json()
                          return rep.get('overview', 'Aucun résumé disponible.')
                    return "Résumé non disponible."
                  
                  for movie_name in movies:
                    poster_url = get_movie_poster(movie_name)
                    comment = get_movie_comment(movie_name)

                  # Organisation en colonnes : image à gauche, texte à droite
                    col1, col2 = st.columns([1, 2])  # Largeur 1:2
                    with col1:
                      if poster_url:
                        st.image(poster_url, caption=movie_name)
                      else:
                        st.write("Affiche non disponible")
                    with col2:
                      st.write(f"**{movie_name}**")
                      st.write(comment)
                else:
                    st.error("Impossible de générer des recommandations pour ce film.")

elif  selection == "Notre Équipe":
   
  # Load the image
  image1 = Image.open("IMG_1.jpg") 
  image2 = Image.open("IMG_2.jpg") 
  image3 = Image.open("IMG_3.jpg") 
  image4 = Image.open("IMG_4.jpg") 

  st.write("""
          Rencontrez l’équipe talentueuse derrière notre succès :
      """)

  # Create a container for the title and image
  col1, col2 = st.columns([1, 2]) 
  with col1:
      st.image(image4) 
  with col2:
      st.text("**Jean Alain Delobelle** : Responsable des études de marché") 

  # Create a container for the title and image
  col3, col4 = st.columns([1, 2]) 
  with col3:
      st.image(image3) 
  with col4:
      st.text("**Laetitia Palogo** : Chef de produit (En contact avec le client et l'équipe marketing)") 

  # Create a container for the title and image
  col5, col6 = st.columns([1, 2]) 
  with col5:
      st.image(image2) 
  with col6:
      st.text("**Sopanha SAO** : Data Analysts (En contact avec l'équipe commerciale et le service financier)") 
      
  # Create a container for the title and image
  col7, col8 = st.columns([1, 2]) 
  with col7:
      st.image(image1) 
  with col8:
      st.text("**Riad Souyad** : Data Analysts (En contact avec le service technique et l'équipe juridique (si nécessaire))") 

elif  selection == "Notre Site":
   
    image5 = Image.open("groupe.jpg") 
    st.image(image5) 

    st.write("Les résultats obtenus depuis le lancement de notre site de recommandations de films sont plus qu'encourageants. Le taux d'engagement des utilisateurs est en constante augmentation, tout comme le nombre de films visionnés suite à nos suggestions. De plus, les sondages de satisfaction montrent que nos utilisateurs sont très satisfaits de la qualité de nos recommandations, ce qui confirme la pertinence de notre approche.")
