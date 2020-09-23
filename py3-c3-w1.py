# -- 1 
nested2 = [{'a': 1, 'b': 3}, {'a': 5, 'c': 90, 5: 50}, {'b': 3, 'c': "yes"}]

#write code to print the value associated with key 'c' in the second dictionary (90)
print(nested2[1]['c'])
#write code to print the value associated with key 'b' in the third dictionary
print(nested2[2]['b'])
#add a fourth dictionary add the end of the list; print something to check your work.
nested2.append( {'a': 'yo'})
print(nested2[3])
#change the value associated with 'c' in the third dictionary from "yes" to "no"; print something to check your work
nested2[2]['c'] = 'no'
print(nested2)

# -- 2 - you can have functions in a list and call them. Note that L[0] picks out the function square, L[0](3) calls the function square, passing it the parameter 3.
def square(x):
    return x*x

L = [square, abs, lambda x: x+1]

print("****names****")
for f in L:
    print(f)

print("****call each of them****")
for f in L:
    print(f(-2))

print("****just the first one in the list****")
print(L[0])
print(L[0](3))

# 1. Below, we have provided a list of lists. Use indexing to assign the element ‘horse’ to the variable name idx1.
animals = [['cat', 'dog', 'mouse'], ['horse', 'cow', 'goat'], ['cheetah', 'giraffe', 'rhino']]
idx1 = animals[1][0]

# 2. Using indexing, retrieve the string ‘willow’ from the list and assign that to the variable plant.
data = ['bagel', 'cream cheese', 'breakfast', 'grits', 'eggs', 'bacon',
        [34, 9, 73, []],
        [['willow', 'birch', 'elm'],
         'apple', 'peach', 'cherry']]
plant = data[7][0][0]




