# We will generally use an alternative way of sorting, the function sorted rather than the method sort. Because it is a function rather than a method, it is invoked on a list by passing the list as a parameter inside the parentheses, rather than putting the list before the period. More importantly, sorted does not change the original list. Instead, it returns a new list.

L2 = ["Cherry", "Apple", "Blueberry"]

L3 = sorted(L2)
print(L3)
print(sorted(L2))
print(L2) # unchanged

print("----")

L2.sort()
print(L2)
print(L2.sort())  #return value is None

# Sort the list, lst from largest to smallest. Save this new list to the variable lst_sorted.

lst = [3, 5, 1, 6, 7, 2, 9, -2, 5]
lst_sorted = sorted(lst, reverse=True)

# If you want to sort things in some order other than the “natural” or its reverse, you can provide an additional parameter, the key parameter. For example, suppose you want to sort a list of numbers based on their absolute value, so that -4 comes after 3? Or suppose you have a dictionary with strings as the keys and numbers as the values. Instead of sorting them in alphabetic order based on the keys, you might like to sort them in order based on their values.

# First, let’s see an example, and then we’ll dive into how it works.
# First, let’s define a function absolute that takes a number and returns its absolute value. (Actually, python provides a built-in function abs that does this, but we are going to define our own, for reasons that will be explained in a minute.)

L1 = [1, 7, 4, -2, 3]

def absolute(x):
    if x >= 0:
        return x
    else:
        return -x

print(absolute(3))
print(absolute(-119))

for y in L1:
    print(absolute(y))
    
# Now, we can pass the absolute function to sorted in order to specify that we want the items sorted in order of their absolute value, rather than in order of their actual value.
# Here we have passed a function object: absolute is a variable name whose value is the function. When we pass that function object, it is not automatically invoked. Instead, it is just bound to the formal parameter key of the function sorted. What the sorted function does is call that key function once for each item in the list that’s getting sorted.
# Think of those associated values as being little post-it notes that decorate the original values. The value 4 has a post-it note that says 4 on it, but the value -2 has a post-it note that says 2 on it. Then the sorted function rearranges the original items in order of the values written on their associated post-it notes.
# Note that this code never explicitly calls the absolute function at all. It passes the absolute function as a parameter value to the sorted function. Inside the sorted function, whose code we haven’t seen, that function gets invoked.
L1 = [1, 7, 4, -2, 3]

def absolute(x):
    if x >= 0:
        return x
    else:
        return -x

L2 = sorted(L1, key=absolute)
print(L2)

#or in reverse order
print(sorted(L1, reverse=True, key=absolute))

# You will be sorting the following list by each element’s second letter, a to z. Create a function to use when sorting, called second_let. It will take a string as input and return the second letter of that string. Then sort the list, create a variable called sorted_by_second_let and assign the sorted list to it. Do not use lambda.

ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

def second_let(s):
    return s[1]

sorted_by_second_let = sorted(ex_lst, key=second_let)

# Below, we have provided a list of strings called nums. Write a function called last_char that takes a string as input, and returns only its last character. Use this function to sort the list nums by the last digit of each number, from highest to lowest, and save this as a new list called nums_sorted.

nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

def last_char(s):
    return s[-1]
    
#  Once again, sort the list nums based on the last digit of each number from highest to lowest. However, now you should do so by writing a lambda function. Save the new list as nums_sorted_lambda.

nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']
nums_sorted_lambda = sorted(nums, key = lambda x: x[-1], reverse=True)
nums_sorted = sorted(nums, key = last_char, reverse=True)


