# A function, whether named or anonymous, can be called by placing parentheses () after it.
# The lambda expression had to go in parentheses just for the purposes of grouping all its contents together. 
# Without the extra parentheses around it on line 10, the interpreter would group things differently and make a function of x that returns x - 2(6).

# In the typical function, we have to use the keyword return to send back the value. In a lambda function, that is not necessary - whatever is placed after the colon is what will be returned.


# Example of lambda
# Regular function...
def last_char(s):
    return s[-1]

last_char("hello")

#...in lambda
last_char = (lambda s: s[-1])
last_char("hello")


## A closer look 
# Regular
def f(x):
    return x - 1

print(f)
print(type(f))
print(f(3))

# Lambda
print(lambda x: x-2)
print(type(lambda x: x-2))
print((lambda x: x-2)(6))
