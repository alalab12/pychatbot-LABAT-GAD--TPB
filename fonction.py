import math
import os


#crée un repertoire contenant les fichiers
def list_of_files(directory, extension):

    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

directory = "./discours"
files_names = list_of_files(directory, "txt")



#afficher les noms complets des présidents sous forme de liste
def nom_presidents():
    nom_president = []
    for i in files_names:
        fichier = i
        n = fichier[11:-4]
        for j in fichier:
            if j == "1" or j =="2":
                n= n[:-1]
        nom_president.append(n)

    nom_complet =[]
    prenom = ["Jacques", "Jacques", "Valerie", "François", "Emanuelle", "François", "François", "Nicolas"]
    for i in range(len(nom_president)):
        p = prenom[i] + " " + nom_president[i]
        if p not in nom_complet:
            nom_complet.append(p)

    return nom_complet





#convertir le texte en minuscule
def textes_minuscule():
    if not os.path.isdir("cleaned"):
        os.mkdir("cleaned")
    for fichier in files_names:
        with open("discours\\" + fichier, "r", encoding='utf-8') as original, open("cleaned\\" + fichier, "w+", encoding='utf-8') as cleaned:
            contenu_original = original.readlines()
            contenu_propre = ""
            for ligne in contenu_original:
                for caractere in ligne:
                    if 65 <= ord(caractere) <= 90:
                        contenu_propre += chr(ord(caractere) + 32)
                    else:
                        contenu_propre += caractere
            return cleaned.write(contenu_propre)




#modifier les caractères indésirables
def textes_caractere():
    if not os.path.isdir("cleaned2"):
        os.mkdir("cleaned2")
    for fichier in files_names:
        with open("cleaned\\" + fichier, "r", encoding='utf-8') as cleaned, open("cleaned2\\" + fichier, "w", encoding= "utf-8") as cleaned2:
            contenu = cleaned.readlines()
            contenu_propre = ""
            for ligne in contenu:
                for caractere in ligne:
                    if caractere == "-" or caractere == "'" or caractere == "_" or caractere == " " or caractere =="`":
                        contenu_propre += " "
                    elif (caractere == "é") or (caractere == "ê") or (caractere == "è") or (caractere == "ë"):
                        contenu_propre += "e"
                    elif caractere == "à" or caractere == "â":
                        contenu_propre += "a"
                    elif caractere == "ù" or caractere == "û":
                        contenu_propre += "u"
                    elif caractere == "ô":
                        contenu_propre += "o"
                    elif caractere == "î" or caractere == "ï":
                        contenu_propre += "i"
                    elif caractere not in [".", ",","?",":",";","!"]:
                        contenu_propre += caractere
            return cleaned2.write(contenu_propre)


#calculer le TF
def tf(text):
    global Tf
    mots = text.split(" ")
    Tf = {}
    for mot in mots:
        if mot in Tf.keys():
            Tf[mot] += 1
        else:
            Tf[mot] = 1
    return(Tf)


#calculer l'Idf
def idf():
    global Idf
    Idf = {}
    nombre_fichier = 0
    for file in list_of_files("./cleaned", ".txt"):
        with open("./cleaned2" + "/" + file, "r") as f:
            mot_fichier = tf(f.read())
            mot_dico = []
            for mot in mot_fichier.keys():
                if mot not in mot_dico:
                    mot_dico.append(mot)
                    if mot in Idf.keys():
                        Idf[mot] += 1
                    else:
                        Idf[mot] = 1
        nombre_fichier += 1
    for value in Idf:
        Idf[value] = math.log(1 / (Idf[value] / nombre_fichier))
    return(Idf)
print(idf())

#calculer le TF-IDF
def TF_IDF(text):
    global tf_idf
    for i in Idf:
        tf_idf = {key: Idf[key] * Tf.get(key, 0) for key in Idf.keys()}
        return tf_idf

for fichier in files_names:
    with open("cleaned2\\" + fichier, "r", encoding = "utf-8") as f:
        text = f.read()
print(TF_IDF(text))





#Afficher les mots avec le score tf-idf le plus faible
def mot_less():
    Mot_less = []
    for mot in tf_idf:
        if tf_idf[mot] == 0:
            Mot_less.append(mot)
    return Mot_less



#afficher le mot avec le score tf-idf le plus élevé
def mot_strong():
        return max(tf_idf)
