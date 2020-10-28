# 1. The variable nested contains a nested list. Assign ‘snake’ to the variable output using indexing.

nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]

print(len(nested))
for list in nested:
    for i in list:
        if i == 'snake':
            output = 'snake'
            
print(output)

# 2. Below, a list of lists is provided. Use in and not in tests to create variables with Boolean values. See comments for further instructions.

lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]
print(len(lst))
#Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
if 'yellow' in lst[2]:
    yellow = True
else:
    yellow = False

#Test to see if 4 is in the second list of lst. Save to variable ``four``
if 4 in lst[1]:
    four = True
else:
    four = False

#Test to see if 'orange' is in the first element of lst. Save to variable ``orange``
if 'orange' in lst[0]:
    orange = True
else: 
    orange = False

 
# NOTE USING A SUPER SHORT WAY
# Use in statements to create variables with Boolean values - see the ActiveCode window for further directions.

L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
test1 = 'hola' in L
            
# Test if [5, 8, 7] is in the list L. Save to variable name test2
test2 = [5, 8, 7] in L
# Test if 6.6 is in the third element of list L. Save to variable name test3
test3 = 6.6 in L[2]



    
