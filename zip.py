 #The zip function takes multiple lists and turns them into a list of tuples (actually, an iterator, but they work like lists for most practical purposes), pairing up all the first items as one tuple, all the second items as a tuple, and so on. Then we can iterate through those tuples, and perform some operation on all the first items, all the second items, and so on.

L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = []

L4 = list(zip(L1, L2)) 

for (x1, x2) in L4:
  L3.append(x1+x2)
  
print(L3)

# Using list comprehension
L1 = [3, 4, 5]
L2 = [1, 2, 3]

L3 = [x1 + x2 for (x1, x2) in list(zip(L1, L2)) ]
print(L3) 

# using map - note map applies a function to each item in the iterable in a loop and returns a new iterator
# note it's a transformation function
L1 = [3, 4, 5]
L2 = [1, 2, 3]

L3 = map( lambda: x: x[0] + x[1], zip(L1, L2) ) 
print(L3) 
