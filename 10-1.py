

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
# Find the sum of all the primes below two million

max = 2000000
min = 2

def is_prime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


# primenumbs = [2,3]
surtotal = 0

for i in range(min,max):
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