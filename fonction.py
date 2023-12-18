import math
import os



#crée un repertoire contenant les fichiers
def list_of_files(directory, extension):

    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

directory = "discours\\"
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
            cleaned.write(contenu_propre)



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
            cleaned2.write(contenu_propre)


#calculer le TF
def tf(text):
    mots = text.split(" ")
    Tf = {}
    for mot in mots:
        if mot in Tf.keys():
            Tf[mot] += 1
        else:
            Tf[mot] = 1
    return Tf


#calculer l'Idf
def idf():
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
        Idf[value] = math.log(nombre_fichier/Idf[value])
    return Idf

#calcul de la matrice tf idf
def TF_IDF():
    tf_list = []
    idf_liste = idf()
    mat = []
    l_file = list_of_files("./cleaned2","txt")
    for file in l_file:
        with (open("./cleaned2/"+file, "r") as f):
            tf_fichier = tf(f.read())
            tf_list.append(tf_fichier)
    j=0
    for val in idf_liste:
        mat.append([])
        for i in range(len(l_file)):
            if val in tf_list[i]:
                mat[j].append(tf_list[i][val]*idf_liste[val])
            else:
                mat[j].append(0)
        j+=1
    return mat


#Afficher les mots avec le score tf-idf le plus faible
def mot_less():
    idf_liste = idf()
    Mot_less = []
    for mot in idf_liste:
        if idf_liste[mot] == 0:
            Mot_less.append(mot)
    return Mot_less



#afficher le mot avec le score tf-idf le plus élevé
def mot_strong(text):
    tf_idf_liste = TF_IDF(text)
    key = list(TF_IDF(text).keys())
    mot = 0
    id = 0
    id_max = 0
    for i in tf_idf_liste:
        if tf_idf_liste[i] > mot:
            mot = tf_idf_liste[i]
            id_max=id
        id +=1
    return mot,key[id_max]


#Trouve les mots les utilisés par Chirac
def Chirac():
    with open("cleaned2/Nomination_Chirac1.txt", "r") as f, open("cleaned2/Nomination_Chirac2.txt", "r") as f2:
        fichier1 = tf(f.read())
        fichier2 = tf(f2.read())
        mot = 0
        id_max = 0
        for i in fichier2:
            print(fichier2[i], i)
            if fichier2[i] > mot and fichier2[i]!="\n":

                mot = fichier2[i]
                id_max = i
        for i in fichier1:
            if fichier1[i] > mot and fichier2[i]!="\n":
                mot = fichier1[i]
                id_max = i
        return mot, id_max

#Montre les présidents qui ont utilisés le mot Nation et celui qui l'a le plus répété
def mot_nation():
    l = []
    mot = "nation"
    with open("cleaned2/Nomination_Giscard dEstaing.txt") as f:
        if mot in f.read():
            l.append("Giscard")

    with open("cleaned2/Nomination_Chirac1.txt") as f, open("cleaned2/Nomination_Chirac2.txt") as v :
        if mot in f.read() or mot in v.read():
            l.append("Chirac")

    with open("cleaned2/Nomination_Hollande.txt") as f:
        if mot in f.read():
            l.append("Hollande")

    with open("cleaned2/Nomination_Macron.txt") as f:
        if mot in f.read():
            l.append("Macron")

    with open("cleaned2/Nomination_Sarkozy.txt") as f:
        if mot in f.read():
            l.append("Sarkozy")


    with open("cleaned2/Nomination_Mitterrand1.txt") as f, open("cleaned2/Nomination_Mitterrand2.txt") as v :
        if mot in f.read() or mot in v.read():
            l.append("Mitterand")
    return l

print(mot_nation())



# trouve le premier président à parler à évoquer le climat ou l'écologie
def first_climat() :
    for fichier in files_names:
        with open("cleaned2\\" + fichier, "r", encoding='utf-8') as cleaned2 :
            contenu = cleaned2.readlines()
            for ligne in contenu:
                for caractere in ligne :
                    if caractere == "climat" or caractere == "ecologie":
                        print(fichier)

    return fichier




#def autres():

#nous n'avons pas compris comment faire cette fonction






max = 0
for fichier in files_names:
    with open("cleaned2\\" + fichier, "r", encoding = "utf-8") as f:
        text = f.read()


