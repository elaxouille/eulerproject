# une grille de 20 par 20
# possible de se deplacer seulement par le bas et par la droite


from random import randint
import time
largeur = 2

def goright(crt):
    global largeur
    if crt[0] == largeur or crt[0] > largeur :
        pass
    else:
        crt[0] += 1

def godown(crt):
    global largeur
    if crt[1] == largeur or crt[1] > largeur :
        pass
    else:
        crt[1] += 1
        
def roll():
    return randint(0,1)

current = [0,0]

if roll() == 0 :
    goright(current)
else:
    godown(current)

