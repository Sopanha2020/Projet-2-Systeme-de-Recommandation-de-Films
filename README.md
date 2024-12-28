# 🎥 Projet-2-Group-Moving-Frame-Systeme-de-Recommandation-de-Films

C'est le résultat du deuxième projet réalisé lors de ma formation en tant que _DATA ANALYST_ à la **Wild Code School** à Lille.

## 🎯 Objectif du Projet :

Le système de recommandation de films est mis en place pour le compte d'un gérant de cinéma de la Creuse afin de lui aider à choisir des films pour ses clients locaux.
Les KPIs sont définis pour évaluer les films susceptibles de correspondre aux goûts locaux.

1. Période de sortie des films :

Films sortis entre 1975 et 1995.

2. Nationalité des films :

Origine : Française et Américaine.

3. Catégories :

Films appartenant aux genres :
     Comédie,
     Famille,
     Drama
   
4. Notes des films :

Score supérieur ou égal à 7 /10 sur les plateformes de notation (e.g., IMDb, TMDB).

5. Durée des films :

À définir selon les préférences locales (proposer des durées moyennes entre 80 min et 240 min).

## ✅ Etapes : 

#### Semaine 1 :  
Appropriation et première exploration des données     
Outils principaux : jupyter, pandas, gzip   

![Capture1](https://github.com/user-attachments/assets/a3a81c9a-873c-497a-9610-2f5fd72a80a6)

![Capture2](https://github.com/user-attachments/assets/95597d23-bb75-4230-9a31-08faff664343)

![Capture3](https://github.com/user-attachments/assets/0885c1f6-8e1f-4b33-946d-4572f9d3db3f)

![Capture4](https://github.com/user-attachments/assets/c3f91bd0-06c3-4590-93de-23c83437e821)

#### Semaine 2 : 
Jointures, filtres, nettoyage,     
Outils principaux : jupyter, Pandas



[LIEN ANALYSE DES DONNEES SOUS DATAPANE 💡 📊](https://cloud.datapane.com/reports/VkGQlN3/exploration-des-donn%C3%A9es/)

#### Semaine 3 : 
Recherche de corrélation, visualisation     
Outils principaux : jupyter, Pandas, Seaborn, matplotlib

[LIEN ANALYSE DES DONNEES SOUS DATAPANE 💡 📊](https://cloud.datapane.com/reports/VkGQlN3/exploration-des-donn%C3%A9es/)

#### Semaine 4 :   
Machine learning, recommandations    
Outils principaux : scikit-learn, Streamlit, jupyterLab, GitHub 

[LIEN APPLICATION UTILISATEUR SOUS STREMLIT ⭐ ♥️ ](https://camillemagnette-systeme-de-recommandation-ma-app-acteurs-k992u6.streamlit.app/)

#### Semaine 5 :  
Affinage, présentation et Demo Day
Outils principaux : power-point, DataPane, Streamlit 

[LIEN PRESENTATION](https://drive.google.com/file/d/1OIF1iphDbTM9wzEyo2xPHQg5SVK1z_EW/view?usp=sharing)


## 🎬 Source des données :  
-[Données IMDb](https://datasets.imdbws.com/)   
-[Données TMDB](https://drive.google.com/file/d/1VB5_gl1fnyBDzcIOXZ5vUSbCY68VZN1v/view)   
-[Explication datasets](https://www.imdb.com/interfaces/)  


## 📎 Méthodologie technique :

1) [Nettoyage de l'ensemble des fichiers sources](https://github.com/CamilleMagnette/Systeme_de_recommandation_machine_learning/blob/main/JupyterlabNotebooks/Projet%202%20-%20Nettoyage%20des%20donn%C3%A9es.ipynb) pour n'en former que deux : 
-  un premier très macro pour réaliser notre analyse,
-  un second pour réaliser notre algorithme

2) [Analyse de la base de données](https://github.com/CamilleMagnette/Systeme_de_recommandation_machine_learning/blob/main/JupyterlabNotebooks/Projet%202%20-%20Graphiques%20Plotly%20avec%20donn%C3%A9es%20nettoy%C3%A9es.ipynb) via le 1er fichier nettoyé : mise en forme de graphiques via [datapane](https://cloud.datapane.com/reports/VkGQlN3/exploration-des-donn%C3%A9es/)

3) [Préparation de notre 2nd fichier nettoyé pour le machine learning](https://github.com/CamilleMagnette/Systeme_de_recommandation_machine_learning/blob/main/JupyterlabNotebooks/Projet%202-%20Pr%C3%A9paration%20du%20fichier%20pour%20le%20machine%20learning.ipynb) : transformation en format pickle et split des colonnes non numériques 

4) [Tests de machine learning](http://localhost:8891/lab/tree/Documents/FORMATION%20DATA%20ANALYST/COURS%20DATA%20ANALYST/PROJET%202/JUPITERLAB%20NOTEBOOKS/Projet%202%20-%20Machine%20learning%20TEST%20ACTEURS.ipynb) : normalisation des données et mise en place d'un algorithme basé sur les plus proches voisins (algorithme K-nearest neighbors (kNN))

5) [Mise en place de l’application utilisateur Streamlit](https://github.com/CamilleMagnette/Systeme_de_recommandation_machine_learning/blob/main/app_acteurs.py)

6) [Publication de l'interface utilisateur Streamlit](https://camillemagnette-systeme-de-recommandation-ma-app-acteurs-k992u6.streamlit.app/)
