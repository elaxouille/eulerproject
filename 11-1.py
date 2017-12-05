# horizontal, vertical ou diagonal, 4 de longueur
# le plus grand produit possible

# 08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
# 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
# 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
# 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
# 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
# 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
# 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
# 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
# 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
# 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
# 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
# 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
# 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
# 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
# 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
# 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
# 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
# 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
# 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
# 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

# 2d array, 20 par 20
# les 0n sont transfromes en n, les 00 en 0

import time

grande_liste = [[8,2,22,97,38,15,0,40,0,75,4,5,7,78,52,12,50,77,91,8],[49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,4,56,62,0],[81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,3,49,13,36,65],[52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91],[22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80],[24,47,32,60,99,3,45,2,44,75,33,53,78,36,84,20,35,17,12,50],[32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70],[67,26,20,68,2,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21],[24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72],[21,36,23,9,75,0,76,44,20,45,35,14,0,61,33,97,34,31,33,95],[78,17,53,28,22,75,31,67,15,94,3,80,4,62,16,14,9,53,56,92],[16,39,5,42,96,35,31,47,55,58,88,24,0,17,54,24,36,29,85,57],[86,56,0,48,35,71,89,7,5,44,44,37,44,60,21,58,51,54,17,58],[19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,4,89,55,40],[4,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66],[88,36,68,87,57,62,20,72,3,46,33,67,46,55,12,32,63,93,53,69],[4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36],[20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16],[20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54],[1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67,48]]

# 10 11 12
# 13 14 15
# [1][0] 13
# [1][1] 14
# [rangee][colonne]
# methode : (si ca marche pas, rajouter 1 pour eviter le 0 en offset sur les bords)
# horizontal#  #-1 faire la liste de [rangee][colonne, ... ,colonne + 3]
            # *=-2 les multiplier entre eux et les assigner a  tmpscore
            #  ?-3 si record < tmpscore ,record = tmpscore
            #-  -4 colonne += 1, si colonne + 3 > 19 : rangee += 1 et colonne = 0
            #  ?-5 si colonne == 19 et rangee == 19 passer a 6 sinon retour a 1
            #-- -6 colonne = 0 et rangee = 0
# vertical  #  #-7 faire la liste de [rangee, ... ,rangee + 3][colonne]
            # *=-8 les multiplier entre eux et les assigner a tmpscore
            #  ?-9 si record < tmpscore, record = tmpscore
            #-  -10 rangee += 1, si rangee + 3 > 19 : rangee = 0 et colonne += 1
            #  ?-11 si rangee == 19 et colonne == 19 passer a 12 sinon retour a 7
            #   -12 colonne = 0 et rangee = 0
# diagonal1 #   -13 faire la liste de [rangee][colonne], ... ,[rangee + 3][colonne + 3]
            #   -14 les multiplier entre eux et les assigner a tmpscore
            #   -15 si record < tmpscpre, record = tmpscore
            #   -16 colonne += 1, si colonne + 3 > 19 : rangee += 1 et colonne = 0
            #   -17 si colonne == 19 et rangee == 19 passer a 18 sinon retour a 13
            #   -18 rangee = 19 et colonne = 0
# diagonal2 #   -19 faire la liste de [rangee, ... ,rangee - 3][colonne, ... , colonne + 3]
            #   -20 les multiplier entre eux et les assigner a tmpscore
            #   -21 si record < tmpscore : record = tmpscore
            #   -22 rangee -= 1, si rangee + 3 > 19 : colonne += 1 et rangee = 0
            #   -23 si rangee == 0 et colonne == 19 passer a 24
            #   -24 print record



# [rangee][colonne]

ran, col, record = 0,0,0
l,m,n,o = 0,0,0,0



def produit(a,b,c,d):
    # print "nouvelle operation :",a,b,c,d
    print a,'*',b,'*',c,'*',d,'=',a*b*c*d
    return a * b * c * d

def compare(score, rec):
    if score > rec :
        print "new record ! :\t\t\t\t", score,'\n'
        
        return score
    else:
        return rec
 
def horizontal():
    global ran
    global col
    if col == 19 :
        ran += 1
        col = 0
    else :
        col += 1

def vertical():
    global ran
    global col
    if ran == 19 :
        col += 1
        ran = 0
    else:
        ran += 1

def diagonal_b() :
    global ran
    global col
    if ran == 0 :
        col += 1
        ran = 19
    else:
        ran -= 1

def tourne1():
    global ran
    global col
    global record
    finished = False
    
    print "\n\n\n\n\n\nHORIZONTAL"
    while not finished : 
        # time.sleep(0.5)
        print "checking :\t", grande_liste[ran][col]  
        print "rangee :\t", ran, "\ncolonne :\t", col
        print ""

        # premiere etape

        l = grande_liste[ran][col]

        try:
            m = grande_liste[ran][col + 1]
        except IndexError:
            m = 1
        
        try:
            n = grande_liste[ran][col + 2]
        except IndexError:
            n =1
        
        try :
            o = grande_liste[ran][col + 3]
        except IndexError:
            o = 1

        # deuxieme etape
        tmpscore = produit(l,m,n,o)

        # troisieme etape
        record = compare(tmpscore,record)

        # cinquieme etape
        if ran == 19 and col == 19 :
            finished = True

        # quatrieme etape
        horizontal()
    
    # sixieme etape
    print "\nreinitialisation du curseur rangee colonne\n"
    ran = 0
    col = 0

    finished = False
    print "\n\n\n\n\n\nVERTICAL"
    while not finished:
        # time.sleep(0.5)
        print "checking :\t", grande_liste[ran][col]  
        print "rangee :\t", ran, "\ncolonne :\t", col
        print ""
        # septieme etape

        l = grande_liste[ran][col]

        try:
            m = grande_liste[ran + 1][col]
        except IndexError:
            m = 1
        
        try:
            n = grande_liste[ran + 2][col]
        except IndexError:
            n =1
        
        try :
            o = grande_liste[ran + 3][col]
        except IndexError:
            o = 1

        # huitieme etape
        tmpscore = produit(l,m,n,o)

        # neuvieme etape
        record = compare(tmpscore,record)

        # onzieme etape
        if ran == 19 and col == 19 :
            finished = True

        # dixieme etape
        vertical()

    # douzieme etape
    print "reinitialisation du curseur rangee colonne"
    ran = 0
    col = 0

    finished = False
    
    print "\n\n\nDIAGONAL 1"

    while not finished :
        # time.sleep(0.5)
        print "checking :\t", grande_liste[ran][col]  
        print "rangee :\t", ran, "\ncolonne :\t", col
        print ""

        #  treizieme etape
        l = grande_liste[ran][col]

        try:
            m = grande_liste[ran + 1][col + 1]
        except IndexError:
            m = 1
        
        try:
            n = grande_liste[ran + 2][col + 2]
        except IndexError:
            n = 1
        
        try :
            o = grande_liste[ran + 3][col + 3]
        except IndexError:
            o = 1

        # 14eme etape
        tmpscore = produit(l,m,n,o)

        # 15eme etape
        record = compare(tmpscore,record)

        # 17eme etape
        if ran == 19 and col == 19 :
            finished = True

        # 16eme etape
        horizontal()
    
    #  18eme etape
    print "\n\n\nreinitialisation du curseur rangee colonne"
    ran = 19
    col = 0

    finished = False

    print "\n\n\nDIAGONAL 2"

    while not finished :
        # time.sleep(0.5)
        print "checking :\t", grande_liste[19][0]  
        print "rangee :\t", ran, "\ncolonne :\t", col
        print ""

        #  19 etape
        try :
            l = grande_liste[ran][col]
        except IndexError :
            l = 1
        try:
            m = grande_liste[ran - 1][col + 1]
        except IndexError:
            m = 1
        
        try:
            n = grande_liste[ran - 2][col + 2]
        except IndexError:
            n = 1
        
        try :
            o = grande_liste[ran - 3][col + 3]
        except IndexError:
            o = 1

        # 20 etape
        tmpscore = produit(l,m,n,o)

        # 21 etape
        record = compare(tmpscore,record)

        # 23 etape
        if ran == 0 and col == 19 :
            finished = True

        # 22 etape
        diagonal_b()
    
    #  24
    print "\n\n\n\n\n\n\n\t\t\t\tRECORD :",record



def routine_a():
    global ran
    global col
    global record
    if col > 19 and ran > 19 :
        print "finished !"
        return True
    elif col + 2 == 19 :
        print "col + 2 == 19"
        o = 1
    elif col + 1 == 19 :
        print "col + 1 == 19"
        o = 1
        n = 1

    l = grande_liste[ran][col]
    m = grande_liste[ran][col + 1]
    n = grande_liste[ran][col + 2]
    o = grande_liste[ran][col + 3]

    tmpscore = produit(l,m,n,o)
    record = compare(tmpscore,record)
    horizontal()

tourne1()
print "fini", record