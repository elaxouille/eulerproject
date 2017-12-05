# 4 chose 2

# 4 * 3
# 2 * 1

# 40 * 39 ... * 20
# 20 * 19 ... * 2

a = 1
b = 1
for i in range(40,20,-1):
    a *= i
    print i

for i in range(1,21):
    b *= i

print a/b