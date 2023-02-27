n = 5
for i in range (n):
    for j in range(i,n):
        print(" ", end = " ")
    for j in range(i):
        print("*",end = " ")
    for j in range(i+1):
        print("*",end = " ")
    print()
m = 3
for row2 in range(m):

    for col2 in range(row2+1):
        print(" ", end = " ")
    for col2 in range(row2,m):
        print(" ",end = " ")
    for col2 in range(row2+1):
        print("*", end=" ")
    for col2 in range(row2,m):
        print("*", end =" ")

    print()