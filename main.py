from fonction import *

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
    print(TF_IDF(text))

elif fonctions == "mot_less":
    print(mot_less())

elif fonctions == "mot_strong":
    print(mot_strong())

else:
    print("Cette fonction n'existe pas")
    print(fonctions)












































































