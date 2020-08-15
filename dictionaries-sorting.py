# sort a dict
L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1
for x in d.keys():
    print("{} appears {} times".format(x, d[x]))

# We can force the results to be displayed in some fixed ordering, by sorting the keys.
d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1
y = sorted(d.keys())

for k in y:
    print("{} appears {} times".format(k, d[k]))
    
# With a dictionary that’s maintaining counts or some other kind of score, we might prefer to get the outputs sorted based on the count rather than based on the items. The standard way to do that in python is to sort based on a property of the key, in particular its value in the dictionary.

L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

y = sorted(d.keys(), key=lambda k: d[k], reverse=True)
for k in y:
    print("{} appears {} times".format(k, d[k]))

# An example using a named function
d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

def g(k):
    return d[k]

# so below the key is passed into g() and it returns d[key] which gives us the value, the list is then sorted on this 
y =(sorted(d.keys(), key=g, reverse=True))

# now loop through the keys
for k in y:
    print("{} appears {} times".format(k, d[k]))
    
# When you pass a dictionary to something that is expecting a list, its the same as passing the list of keys.
# The function sorted is invoked. Its first parameter value is a dictionary, which really means the keys of the dictionary. The second parameter, the key function, decorates the dictionary key with a post-it note containing that key’s value in dictionary d. The last parameter, True, says to sort in reverse order.

L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

# now loop through the sorted keys
for k in sorted(d, key=lambda k: d[k], reverse=True):
      print("{} appears {} times".format(k, d[k]))

# Sort the following dictionary’s keys based on the value from highest to lowest. Assign the resulting value to the variable sorted_values.

dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}

sorted_values = sorted(dictionary, key= lambda k: dictionary[k], reverse=True)

# The property we want to sort by is the number of cities that begin with the letter ‘S’.
def s_cities_count(city_list):
    ct = 0
    for city in city_list:
        if city[0] == "S":
            ct += 1
    return ct

states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}

print(sorted(states, key=lambda state: s_cities_count(states[state])))
