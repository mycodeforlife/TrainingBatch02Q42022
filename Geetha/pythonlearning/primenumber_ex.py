n1 = int(input("enter first number:"))

print(n1)
n = False

if n1 == 1:
    print("1 is not a prime")
elif n1 > 1:
    for i in range(2, n1):
        if n1 % i == 0:
            #print("not a prime number")
            n = True
            print("not a prime number")
            break

print(n)
if not n:
    print("prime number")
else:
    pass
