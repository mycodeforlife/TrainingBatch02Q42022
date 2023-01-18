i =  input("enter a number:")

print(i)

#l: int = len(str(i))

l: int = len(str(i))

print(l)

k: int = l-1
print(k)

n = False

if l == 0:
    print("enter a value")
elif l > 0:
       #print(j)
        if i[k] == '0':
            # print("number ends with zero ")
            n = True

print(n)
if not n:
    print("number does not with zero")
else:
    print("number ends with zero")


