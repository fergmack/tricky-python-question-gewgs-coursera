 # Now that you’ve learned about optional and keyword parameters, we can introduce a new way to use the format method.

names_scores = [("Jack",[67,89,91]),("Emily",[72,95,42]),("Taylor",[83,92,86])]
for name, scores in names_scores:
    print("The scores {nm} got were: {s1},{s2},{s3}.".format(nm=name,s1=scores[0],s2=scores[1],s3=scores[2]))
  
  
# Sometimes, you may want to use the .format method to insert the same value into a string multiple times. You can do this by simply passing the same string into the format method, assuming you have included {} s in the string everywhere you want to interpolate them. But you can also use positional passing references to do this! The order in which you pass arguments into the format method matters: the first one is argument 0, the second is argument 1, and so on.

# this works - not you're putting in each name 3 times usingt this
names = ["Jack","Jill","Mary"]
for n in names:
    print("'{}!' she yelled. '{}! {}, {}!'".format(n,n,n,"say hello"))

# but this also works!
names = ["Jack","Jill","Mary"]
for n in names:
    print("'{0}!' she yelled. '{0}! {0}, {1}!'".format(n,"say hello"))

#   What value will be printed for z? Ans = 7
# ✔️ the default value for z is determined at the time the function is defined; at that time initial has the value 0.
initial = 7
def f(x, y = 3, z = initial):
    print ("x, y, z are:", x, y, z)
initial = 0
f(2)

# What will be printed?
#  'Catalina!' she yelled. 'Come here, Catalina! Alexey, Misuki, and Pablo are here!'

names = ["Alexey", "Catalina", "Misuki", "Pablo"]
print("'{first}!' she yelled. 'Come here, {first}! {f_one}, {f_two}, and {f_three} are here!'".format(first = names[1], f_one = names[0], f_two = names[2], f_three = names[3]))

#  Define a function called multiply. It should have one required parameter, a string. It should also have one optional parameter, an integer, named mult_int, with a default value of 10. The function should return the string multiplied by the integer. (i.e.: Given inputs “Hello”, mult_int=3, the function should return “HelloHelloHello”)
def multiply(s, mult_int=10):
    return s*mult_int

multiply("Hello", 3)

