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

# TRICKY PROBLEM: Below we have provided two lists of numbers, L1 and L2. Using zip and list comprehension, create a new list, L3, that sums the two numbers if the number from L1 is greater than 10 and the number from L2 is less than 5. This can be accomplished in one line of code.


L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

print(zip(L1, L2) )

L3 = [ x1 + x2 for (x1, x2) in list(zip(L1, L2)) if x1 > 10 and x2 < 5 ]

