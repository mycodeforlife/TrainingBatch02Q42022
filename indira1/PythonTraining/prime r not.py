# Given number prime or not

num = int(input("Enter a number : "))
if num<=1 :
    print (num, "is not a prime number")

else:
    for j in range(2,num):
        if (num%j)==0:
            print (num, "is not a prime number")
            break
    else:
        print (num, "is a prime number")




