## exercice 1/2

def nombre_present(mot,x):
    nombre = 0
    for i in mot:
        if i == x:
            nombre +=1
    return nombre



def scrabble():
    liste=[]# liste de tous les mots du lexique
    tirage=['r','a','l','e']
    f = open("frenchssaccent.dic",'r')
    for ligne in f:
        liste.append(ligne[0:len(ligne)-1])
    # liste est complète sans retour à la ligne
    f.close()
    count=[0]*len(liste) # compte nombre de lettre du tirage dans chaque mot

    i=0 ; j_max =0
    plus_grand_count = 0
    for mot in liste:
        for lettre in tirage:
            if nombre_present(mot,lettre) == nombre_present(tirage,lettre) and nombre_present(mot,lettre) != 0 :
                count[i] += 1
        if count[i] == len(mot) and count[i]>=plus_grand_count:
            # vérifie que le mot est composé uniquement des lettres du tirage
            j_max = i
            plus_grand_count = count[i]
        i+=1

    return(liste[j_max])

# Debug "count out of range" : il faut que len(count) = len(liste"

# variante : tirage random

## exercice 3
# maximiser le nombre de points pour un mot

un_point = ['a','e','i','l','n','o','r','s','t','u']
deux_points = ['d','g','m']
trois_points=['b','c','p']
quatre_points=['f','h','v']
huit_points=['j','q']
dix_points=['k','w','x','y','z']

# score : donne nombre de points pour le mot
# max_score : prend une liste de mots et renvoie le mot avec le score maximum
# scrabble_bis : renvoie le mot du lexique qui maximise le nombre de points

def score(mot):
    count = 0
    for lettre in mot:
        if lettre in un_point:
            count+=1
        if lettre in deux_points:
            count+=2
        if lettre in trois_points:
            count+=3
        if lettre in quatre_points:
            count+=4
        if lettre in huit_points:
            count+=8
        if lettre in dix_points:
            count+=10
    return count


def max_score(liste):
    j_max = 0; plus_grand_count = 0
    count=[0]*len(liste) # compte nombre de points dans chaque mot
    for i in range(0,len(liste)):
        count[i] = score(liste[i])
        if count[i]>= plus_grand_count :
            j_max=i
            plus_grand_count = count[i]
    return (liste[j_max], score(liste[j_max]))


def scrabble_bis():
    liste=[]# liste de tous les mots du lexique

    f = open("frenchssaccent.dic",'r')
    for ligne in f:
        liste.append(ligne[0:len(ligne)-1])
    # liste est complète sans retour à la ligne
    f.close()

    return max_score(liste)

## exercice 4
# pas fait


















