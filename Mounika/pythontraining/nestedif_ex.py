import sys

x = int(sys.argv[1])
if x == 10:
    print("Given number is equal to 10,")
if x > 10:
     print("Above 10,")
     if x > 20:
         print("and also above 20")
     else:
         print("but not above 20")
else:
     print("It not a valid number")