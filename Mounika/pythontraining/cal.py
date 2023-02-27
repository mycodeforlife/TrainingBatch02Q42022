import sys

Operator = sys.argv[1]
numbers = sys.argv[2:]
print(Operator)
print(numbers)


total = 0
for num in numbers:
   total = total+int(num)

print(total)


"""
print("select from below operators\n add\n sub\n div\n mul")

operator = (input("enter a opeartor:"))
if (operator == "add") or (operator == "sub") or (operator == "mul") or (operator == "sub") or (operator == "all"):
   print(operator)
   num1 = int(input("enter 1st number:"))
   num2 = int(input("enter 2nd number:"))
   if operator == "add":
     print(num1+num2)
   elif operator == "sub":
      print(num1 - num2)
   elif operator == "div":
      print(num1 / num2)
   elif operator == "mul":
     print(num1 * num2)
else:
    print("invalid operator")
    exit(1)


def add_num(x, y):
   pass


def subtract_num(x, y):
   pass

"""