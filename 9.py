# triplette pythagoreenne
# a**2 + b**2 == c**2
# trouver la triplette pour laquelle a+b+c = 1000


total = 1000

a = 1
b = 1
c = 1

def check_sum(a,b,c):
    a = a**2
    b = b**2
    c = c**2
    if c == a + b :
        return True
    return False

def square(x):
    return x ** 2

for i in range(1000):
    for j in range(1000):
        for k in range(1000):
            if check_sum(i,j,k) :
                if i+j+k == 1000 :
                    print i,j,k