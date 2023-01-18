import sys

try:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
except:
    print("call script with command line inputs: python ex4.py number1 number2")
else:
    print(x+y)


