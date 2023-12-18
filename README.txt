# chatbot
Projet python : création d'un chatbot

Aude LABAT
Jessica GAD

lien Githhub : https://github.com/alalab12/pychatbot-LABAT-GAD--TPB/tree/main

Afin d'accéder aux différentes fonctions rendez vous dans le fichier main et entrer la fonction de vous souhaiter utiliser parmi celle-ci :


Partie I :

- list_of_files
- nom_presidents
- textes_minuscule
- textes_caractere
- tf
- idf
- TF_IDF
- mot_less
- mot_strong
- Chirac
- mot_nation
_ first_climat
- autres





fonctionnalités de l'application :

Partie I :

- Aperçu clair des fichiers (nom et prénom des présidents)
- Convertion en minuscule et nettoyage des caractères indésirables dans les fichiers
- Calcul du TF
- Calcul de l'IDF
- Calcul de TF-IDF
- Trouve les mots avec le TF-IDF le plus faible
- Trouve le mot avec le TF-IDF le plus fort
- Trouve les mots les utilisés par Chirac
- Montre les présidents qui ont utilisés le mot Nation et celui qui l'a le plus répété
- Montre le premier président à parler d'écologie (non réussi)
- Montre les autres mot non important utilisés par les présidents (non réussi)

* Certaines les fonctions ne fonctionnent pas encore correctement

Partie II :

- "tokenisation" du texte, on enlve les accents et transforme la question posé en liste de caractère
-  recherche des termes à la fois présent dans le corpus et dans la question posé.
- composition de la matrice
- calcul des tf_idf des mots présents dans la question et dans le corpus
- calcul de la norme
- calcul du produit scalaire
- calcul de simalirité entre la question et chaque document
- choix du texte le plus pertinent pour répondre à la question
- recherche du mot ayant le tf idf le plus élevé dans la question
- renvoie la réponse à la question
