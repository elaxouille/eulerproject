# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
# Find the sum of all the primes below two million

max = 1999999
min = 5

def is_prime(n):
    for i in range(3,n):
        if n % i == 0 :
            return False
    # print(n)
    return True

# primenumbs = [2,3]
surtotal = 0

for i in range(max, min, -2):
    if is_prime(i):
        surtotal += i
        print surtotal, " /// (",i,")"
        # primenumbs.append(i)


# print(primenumbs)

def sum_list(l):
    tot = 0
    for it in l :
        tot += it
    return tot

print("TOTAL : ...")
print(surtotal)
# print sum_list(primenumbs)