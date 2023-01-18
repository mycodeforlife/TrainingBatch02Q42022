import sys

global_x = 10
def add(num1,num2):
    x = num1+num2
    print(global_x)
    return x

def subtract(num1, num2):
    print(x)
    y = num1 - num2
    print(global_x)
    return y


a = int(sys.argv[1])
b = int(sys.argv[2])

sum_val = add(a,b)
diff = subtract(sum_val,3)
print(diff)


