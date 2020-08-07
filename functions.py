# Write a function, test, that takes in three parameters: a required integer, an optional boolean whose default value is True, and an optional dictionary, called dict1, whose default value is {2:3, 4:5, 6:8}. If the boolean parameter is True, the function should test to see if the integer is a key in the dictionary. The value of that key should then be returned. If the boolean parameter is False, return the boolean value “False”.

def test(x, y=True, dict1 = {2:3, 4:5, 6:8}):
    if y == True:
        if x in dict1.keys():
            return dict1[x]
    else:
        return False
    
# Write a function called checkingIfIn that takes three parameters. The first is a required parameter, which should be a string. The second is an optional parameter called direction with a default value of True. The third is an optional parameter called d that has a default value of {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}. Write the function checkingIfIn so that when the second parameter is True, it checks to see if the first parameter is a key in the third parameter; if it is, return True, otherwise return False.

# But if the second paramter is False, then the function should check to see if the first parameter is not a key of the third. If it’s not, the function should return True in this case, and if it is, it should return False.

def checkingIfIn (s, direction=True, 
                  d={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 
                     'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction==True:
        if s in d.keys():
            return True
        else:
            return False
    else:
        if s not in d.keys():
            return True
        else:
            return False
       
# We have provided the function checkingIfIn such that if the first input parameter is in the third, dictionary, input parameter, then the function returns that value, and otherwise, it returns False. Follow the instructions in the active code window for specific variable assignmemts.


def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

# Call the function so that it returns False and assign that function call to the variable c_false
c_false = checkingIfIn('cow')
# Call the fucntion so that it returns True and assign it to the variable c_true
c_true =  checkingIfIn('cow', False)
# Call the function so that the value of fruit is assigned to the variable fruit_ans
fruit_ans =  checkingIfIn('fruit')
# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check
param_check =  checkingIfIn('raspberry', d={'raspberry':8})