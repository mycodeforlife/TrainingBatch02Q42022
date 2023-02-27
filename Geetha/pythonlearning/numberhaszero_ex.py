i = input("enter a number:")

print(i)

#l: int = len(str(i))

l: int = len(str(i))

print(l)


n = False

if l == 0:
    print("enter a value")
elif l > 0:
    for j in range(0, l):
        #print(j)
        print(i[j])
        if i[j] == '0':
            print("number has a zero ")
            n = True
            break

print(n)
if not n:
    print("number has NO zero")
else:
    print("number has zero")
