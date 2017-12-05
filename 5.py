number = 1

def is_divisible(n):
    for i in range(1,20):
        if n % i != 0 :
            return False
    return True

while True:
    if not(is_divisible(number)):
        number += 1
    else:
        print(number,is_divisible(number))
        break
