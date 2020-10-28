# 1. The variable nested contains a nested list. Assign ‘snake’ to the variable output using indexing.

nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]

print(len(nested))
for list in nested:
    for i in list:
        if i == 'snake':
            output = 'snake'
            
print(output)
