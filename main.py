from fonction import *
from fonction2 import *


# choix entre les différentes fonctionnalités
choix = input("Quelles fonctionnalités souhaités vous utilisez (fonctions/question) : ")


#Etude de tous les cas possible
if choix == "fonctions":
    fonctions = input("Saisir la fonction désirée: ")

    if fonctions == "list_of_files":
        print(list_of_files)

    elif fonctions == "nom_presidents":
        print(nom_presidents())

    elif fonctions == "textes_minuscule":
        print(textes_minuscule())

    elif fonctions == "textes_caractere":
        print(textes_caractere())

    elif fonctions == "tf":
        for fichier in files_names:
            with open("cleaned2\\" + fichier, "r", encoding="utf-8") as f:
                text = f.read()
        print(tf(text))

    elif fonctions == "idf":
        print(idf())

    elif fonctions == "TF_IDF":
        print(TF_IDF())

    elif fonctions == "mot_less":
        print(mot_less())

    elif fonctions == "mot_strong":
        print(mot_strong(text))

    elif fonctions == "Chirac":
        print(Chirac())

    elif fonctions == "mot_nation":
        print(mot_nation())

    elif fonctions == "first_climat":
        print(first_climat())

    elif fonctions == "autres":
        print("Nous n'avons pas reussi à faire cette fonction")

    else:
        print("Cette fonction n'existe pas")
        print(fonctions)

if choix == "question":
    question = input("Posez votre question :")
    print(print(reponse(question)))

else:
    print("Erreur")
    choix = input("Quelles fonctionnalités souhaités vous utilisez (fonctions/question) : ")































































































