#               # 00 10 20
#               # 01 11 21
#               # 02 12 22
#
# [
#       ['00','10','20','21','22']
#       ['00','10','11','21','22']
#       ['00','01','11','12','22']
#       ['00','01','02','12','22']
#       ['00','01','11','21','22']
#       ['00','10','11','12','22']
# ]

# part de '00'

from random import randint

largeur = 2

def randomly_next(current):
    global largeur
    #  si 0 : a droite
    #  si 1 : en bas
    current_x, current_y = int(current[0]), int(current[1])

    if randint(0,1) == 0 :
        if current_x < largeur :
            new_x = current_x + 1
            new_pos = str(new_x)+str(current_y)
    elif current_y < largeur:
        new_y = current_y + 1
        new_pos = str(current_x)+str(new_y)
    else:
        print "wtf"
        return 'xx'

    return new_pos
    

