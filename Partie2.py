# *** LAMGARMEL Raja : Etudiante Master 1 Informatique ***
# Partie 2 : Chiffrement de César

# La fonction de chiffrement de César

# Définir deux listes, alp_clair et alp_chiff, contenant toute les lettres dans l’ordre alphabétique.
alp_clair = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q'
    , 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alp_chiff = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q'
    , 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Implémentation 1 : La fonction de chiffrement de César avec la méthode des listes

def cesar_list(n, texte):
    msg_déchiff = ''  # variable qui va contenir le message chiffré
    texte = texte.lower()  # transformer le message chiffré en minuscule
    for c in texte:
        if c not in alp_clair: # Gérer les espaces et les caractères spéciaux
            msg_déchiff += c # si la lettre c n'exite pas dans la liste on la considére comme
            # espace ou caractére spéciale, on la rajoute donc au message déchiffré.
        else:
            index = alp_clair.index(c)  # récupérer la position de la lettre dans la liste alp_clair
            indice = index + n  # définire le décalage
            if indice > 25:  # s'il y un dépassement de la lettre z
                indice = indice % 26
            msg_déchiff += alp_clair[indice]
    return msg_déchiff


print("******************** Implémentation  1 ********************")
print(cesar_list(3, "Je suis d'accord, OK"))


# Implémentation 2 : La fonction de chiffrement de César avec la méthode Ascii
def cesar_ascii(n, texte):
    msg_chiff = ''  # variable qui va contenir le message chiffré
    texte = texte.lower()  # transformer le message claire en minuscule
    for c in texte:
        index = ord(c) + n  # récupérer le code Ascii de la lettre et dfinire le décalage.

        if 97 <= ord(c) <= 122:  # cadrer les lettre minuscule
            if index > 122:  # si il y a un dépassement de lettre z
                index = index % 26
            msg_chiff += chr(index)
        else:  # Gérer les espaces ainsi que les caractères spéciaux
            msg_chiff += c
    return msg_chiff


# Tester le fonction
print("********************  Implémentation  2 avec Ascii ********************")
print(cesar_ascii(3, "Je suis d'accord, OK"))


# Implémentation de la focntion pour décoder le message chiffré
def dechiffrement_cesar(n, texte):
    msg_déchiff = ''  # variable qui va contenir le message déchiffré
    texte = texte.lower()  # transformer le message chiffré en minuscule
    for c in texte:
        index = ord(c) - n  # récupérer le code Ascii de la lettre et dfinire le décalage.

        if 97 <= ord(c) <= 122:  # cadrer les lettre minuscule
            if index > 122:  # si il y a un dépassement de lettre z
                index = index % 26
            msg_déchiff += chr(index)
        else:  # Gérer les espaces ainsi que les caractères spéciaux
            msg_déchiff += c
    return msg_déchiff


# Tester le fonction
print("********************  Déchiffrement du message qu'on a chiffré ********************")
print(dechiffrement_cesar(3, "mh vxlv g'dffrug, rn"))



# 4 : Proposer une méthode de résolution, et casser le code.

# la faiblesse de l'algorithme Cesar réside dans le fait qu'il ya que 26 clés possibles.
# L'idée donc est de trouver la bonne clé (le nombre n)
# on va donc boucler tout les clés possible au total 26 clé possibles
def casser_cesar(txt_chiff):
    for cle in range(26):
        msg_déchiff = ''
        texte = txt_chiff.lower()  # transformer le message chiffré en minuscule
        for c in texte:
            index = ord(c) - cle  # récupérer le code Ascii de la lettre et définir le décalage avec la clé.
            if 97 <= ord(c) <= 122:  # cadrer les lettre minuscule
                if index > 122:  # s'il y a un dépassement de lettre z
                    index = index % 26
                msg_déchiff += chr(index)
            else:  # Gérer les espaces ainsi que les caractères spéciaux
                msg_déchiff += c
        print(" Le message clair possible est : " + msg_déchiff + " avec la clé : [" + format(cle) + "]")


# tester la fonction, en analysant les résultats possibles, on voit clairement le message clair 'je suis d'accord, ok'
# avec la clé 3
print("******************** Casser l'algorithme Cesar  ********************")
casser_cesar("mh vxlv g'dffrug, rn")
print("******************** ")