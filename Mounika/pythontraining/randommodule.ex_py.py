import random
print(random.randint(1,6))
print(random.randint(100,999))
#display a company name ABCXXXX where XXXX is a random user id
print("ABC"+str(random.randint(1000,9999)))
#To display even numbers form 1 to 10
print(random.randrange(1,11,2))
#random.choice function picking randomly for a sequence ,it can be either list or tuple or set
fruits = ["Apple","banana","orange","kiwi","pears","muskmelon"]
print(random.choice(fruits))
#random.shuffle function
cards = [1,2,3,4,5,6,7,8,9,"king","queen","jack"]
random.shuffle(cards)
print(cards)