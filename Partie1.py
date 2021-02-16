# *** LAMGARMEL Raja : Etudiante Master 1 Informatique ***

# Partie 1 : Outils mathématiques pour la cryptographie

# Exercice 1: Nombre premier

# La fonction 'nb_premier' affiche les nombres premiers inférieurs à un nombre n
# en utilisant la méthode par division
def nb_premier(n):
    p = [] # définir la liste qui va contenir les nombres premiers
    for k in range(1, n):
        for i in range(2, k):
            if (k % i) == 0:
                break
        else:
            p.append(k) # Si le nombre est premier on le rajoute à la liste
    print(p)


# tester la fonction
m = int(input("Entrez le nombre n : "))
nb_premier(m)
