# une grille de 20 par 20
# possible de se deplacer seulement par le bas et par la droite
from random import randint
import time
largeur = 2

possibilite = []
liste_possibilites = []
#          x,y
current = [0,0]

def goright():
    global current, largeur, liste_possibilites
    if current[0] == largeur :
        godown()
    else:
        current[0]+=1

def godown():
    global current, largeur, liste_possibilites
    if current[1] == largeur :
        goright()
    else:
        current[1]+=1

def check_already_made(liste):
    global liste_possibilites
    for i in liste_possibilites :
        if liste == i :
            return False
    print "new item !", liste
    liste_possibilites.append(liste)

def finished():
    global largeur, current
    if current == [largeur,largeur] :
        return True
    else:
        return False

