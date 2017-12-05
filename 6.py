# somme des carres, carre des sommes

total1 = 0
total2 = 0
for i in range(1,101):
    total1 += i
    total2 += i ** 2

total1 = total1 ** 2

print total1,total2
print total1 - total2