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
Outils principaux : jupyter, pandas

![Capture5](https://github.com/user-attachments/assets/36e0fd44-b3bb-4b4c-b310-765e2a7c83b2)

![Capture6](https://github.com/user-attachments/assets/2e458362-855b-4472-bf58-49f938247165)

![Capture7](https://github.com/user-attachments/assets/41220518-930b-4845-a233-4eae2dccb772)

#### Semaine 3 : 
Recherche de corrélation, visualisation     
Outils principaux : google colab, pandas, seaborn, matplotlib

![Capture8](https://github.com/user-attachments/assets/36532d5f-4911-40dc-9952-b392ee903287)

![Capture9](https://github.com/user-attachments/assets/ec2d184d-192e-4dc2-925f-c3b156f2e11e)

![Capture10](https://github.com/user-attachments/assets/14c38f5b-e38d-4d75-9f58-c77aa0c49f11)

![Capture11](https://github.com/user-attachments/assets/a695aed4-a6b9-45d4-935c-abec6825b53f)

![Capture12](https://github.com/user-attachments/assets/52c5e3be-8604-46f9-8f0c-5c0a952a6543)

![Capture13](https://github.com/user-attachments/assets/e386ddfa-554d-41dd-bb8f-40f2b33be90e)

![Capture14](https://github.com/user-attachments/assets/9aeba95f-8231-4c65-9b40-2ed3e28d32fa)

#### Semaine 4 :   
Machine learning, recommandations    
Outils principaux : goole colab, scikit-learn, nlptk




#### Semaine 5 :  
Affinage, présentation et Demo Day
Outils principaux : google colab, google slide, streamlit 



## 🎬 Source des Données :  
-[Données IMDb](https://datasets.imdbws.com/)   
-[Données TMDB](https://drive.google.com/file/d/1VB5_gl1fnyBDzcIOXZ5vUSbCY68VZN1v/view)   
-[Explication datasets](https://www.imdb.com/interfaces/)  


## 📎 Livrables

* Exploration et infiltrage des données : ouvrez les notebooks correspondants dans Jupyter : [Notebook](https://github.com/Dim2960/flixoucreuse/exploration_visualisation).
* Nettoyage et visualisation des données : ouvrez les notebooks correspondants dans Google Colab : [Notebook](https://github.com/Dim2960/flixoucreuse/exploration_visualisation).
* Application : ouvrez à partir de l'url suivante : [appli-streamlit](https://flixoucreuse.streamlit.app/)

## 📡 Installation

0. Prérequis d'installation
    
    Python >= 2.12
    
1. Clonez le dépôt:
    ```sh
    git clone https://github.com/Sopanha2020/Projet-2-Group-Moving-Frame-Systeme-de-Recommandation-de-Films.git
    ```
2. Allez dans le répertoire du projet:
    ```sh
    cd Projet-2-Group-Moving-Frame-Systeme-de-Recommandation-de-Films
    ```
3. Installez les dépendances:
    ```sh
    pip install -r requirements.txt
    ```
4. Ajouter la clé API tmdb pour utilisation en local:  
    ```
    Copier votre clé API tmdb dans le fichier api.txt
    ```
5. Lancer l'application en local:
    ```sh
    streamlit run index.py
    ```
