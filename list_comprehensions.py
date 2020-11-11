# alternative to mapping and filter. The if clause does the fitering

[ <transformer_experession> 
                            for 
                                <loop_var> 
                                              in <sequence> 
                                                            if <filtration_expression> ]
                                                            
def keep_evens(nums):
    new_list = [num for num in nums if num % 2 == 0]
    return new_list

print(keep_evens([3, 4, 6, 7, 0, 1]))

# You can also combine map and filter operations by chaining them together, or with a single list comprehension.
things = [3, 4, 6, 7, 0, 1]
#chaining together filter and map:
# first, filter to keep only the even numbers
# double each of them
print(map(lambda x: x*2, filter(lambda y: y % 2 == 0, things)))

# equivalent version using list comprehension
print([x*2 for x in things if x % 2 == 0])

# The for loop below produces a list of numbers greater than 10. Below the given code, use list comprehension to accomplish the same thing. Assign it the the variable lst2. Only one line of code is needed.

L = [12, 34, 21, 4, 6, 9, 42]
lst = []
for x in L:
    if x > 10:
        lst.append(x)
print(lst)

# rewritten 
lst2 = [x for x in L if x > 10]
