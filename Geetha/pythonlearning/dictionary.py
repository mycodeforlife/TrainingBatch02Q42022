
# each element or value should have a key
#keys should be unique and immutable
#keys can be a string or numbers

# data={1:'geetha', 2:'indu', 4:'monika'}
# print(data)

# to fetch some value

# print(data[4])
# print(data[1])
# print(data[3])

# also can use get to fetch the value
# print(data.get(1))
# print(data.get(3))
# print(data.get(3, 'not found')) # returning a dta where we don't have any key

# dictionary with list

keys= ['geetha', 'indu', 'monika']
values= ['apple', 'banana', 'cherry']
data= dict(zip(keys, values)) # merging 2 lists into a dictionary
print(data)

data['venkat'] = "orange" # adding a key and value to the dictionary
print(data)













