def is_prime(n):
    for i in range(3,n):
        if num % i == 0:
            return False
    return True
num = 0
arr = []

while len(arr) < 10010:

    if is_prime(num):
        arr.append(num)
        if len(arr) % 1000 == 0 :
            print len(arr),"eme"
        num += 1
    else :
        num += 1

print "9999 " , arr[9999]
print "10000 ", arr[10000]
print "10001 ", arr[10001]
print "10002 ", arr[10002]
print "10003 ", arr[10003]