from fonction import *
from math import *



# "tokenisation" du texte, on enlève les accents et transforme la question posé en liste de caractère
def token(text):
    liste_e = ["é", "è", "ê", "ë"]
    liste_a = ["à", "â"]
    liste_u = ["ù","û"]
    ch = ""
    for i in range(len(text)):
        if "a" <= text[i] <= "z":
            ch += text[i]
        else:
            if text[i] == "'":
                ch += " "
                
            elif text[i] in liste_e:
                ch += "e"

            elif text[i] in liste_a:
                ch += "a"

            elif text[i] in liste_u:
                ch += "u"

            elif text[i] == "ç":
                ch += "c"

            elif text[i] == "ô":
                ch += "o"

            else:
                ch += " "
    return ch.split(" ")


# recherche des termes à la fois présent dans le corpus et dans la question posé.
def recherche(text):
    document = list(idf().keys())
    question = token(text)
    l = []
    for i in question:
        if i in document:
            l.append(i)
    return l



#composition de la matrice
def compose(matrice):
    nouvelle_mat =[]
    for i in range(len(matrice[0])):
        nouvelle_mat.append([])
        for j in range(len(matrice)):
            nouvelle_mat[i].append(0)
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            nouvelle_mat[j][i] = matrice[i][j]
    return nouvelle_mat




#calcul des tf_idf des mots présents dans la question
def TF_IDF_question(text):
    M = []
    list_mots_Question = token(text)
    tf_motQuestion = tf(" ".join(token(text)))
    idf_motCorpus = idf()
    for i in list(idf_motCorpus.keys()):
        if i in list_mots_Question:
            M.append(tf_motQuestion[i] * idf_motCorpus[i])
        else:
            M.append(0)
    return M


# calcul de la norme
def norme(vecteur):
    s = 0
    for val in vecteur:
        s += val**2
    return sqrt(s)



# calcul du produit scalaire
def scalaire(V1, V2):
    s = 0
    for i in range(len(V1)):
        s += V1[i] * V2[i]
    return s


# calcul de simalirité entre la question et chaque document
def similair(matrice_q, matrice):
    l_similair = []
    l_norme = []
    norme_q = norme(matrice_q)
    
    for i in range(len(compose(TF_IDF()))):
        l_norme.append([])

    for i in range(len(matrice)):
        l_norme[i] = norme(matrice[i])

    
    for i in range(len(matrice)):
        l_similair.append(scalaire(matrice_q, matrice[i]) / norme_q * l_norme[i])
    
    return l_similair




# choix du texte le plus pertinent pour répondre à la question
def pertinent(matrice_question):
    l_fichier = list_of_files("cleaned2\\", "txt")
    
    matrice = compose(TF_IDF())
    l_similair = similair(matrice_question, matrice)
    max = [0, 0]
    for i in range(len(l_similair)):
        if l_similair[i] > max[0]:
            max[0] = l_similair[i]
            max[1] = i
    return l_fichier[max[1]]


#recherche du mot ayant le tf idf le plus élevé dans la question
def mot_plus_impo(text):
    max = 0
    val = 0
    question = TF_IDF_question(text)
    for i in range(len(question)):
        if question[i] > max:
            max = question[i]
            val = i
    return list(idf().keys())[val]


#
def reponse(text):
    txt = token(text)
    text = ""
    for i in txt:
        text += i + " "
    mot_impo = mot_plus_impo(text)
    phrase = ""
    found = False
    with open("discours\\" + pertinent(TF_IDF_question(text)), "r", encoding= "utf-8") as f:
        fichier = f.readlines()
        for ligne in fichier:
            for mot in ligne.split(" "):
                phrase += mot + " "
                if mot_impo in token(mot):
                    found = True
                elif "." in mot :
                    if found:
                        return phrase
                    else:
                        phrase = ""











