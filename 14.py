# n est pair : n /= 2
# n est impair : n = n * 3 + 1
# 
#
# 
# 
# 
# 

# globale de record
record = 0
init_number_for_record = 0

def collatz(n):
    # finds the next collatz number
    nn = n
    if n % 2 == 0 :
        nn /= 2
    else :
        nn = nn * 3 + 1
    
    return nn


def autocollatz(n):
    global record
    global init_number_for_record
    test = n
    incr = 0
    while test > 1 :
        incr += 1
        test = collatz(test)
    if record < incr :
        record = incr
        init_number_for_record = n
        print "nouveau record : ", init_number_for_record,"=>",record

for i in range(1000000):
    autocollatz(i)

print record, init_number_for_record