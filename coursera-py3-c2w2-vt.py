# very tricky 
# Write a program that finds the key in a dictionary that has the maximum value. If two keys have the same maximum value, it’s OK to print out either one. Fill in the skeleton code

d = {'a': 1, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}

ks = d.keys()
best_key_so_far = list(ks)[0]  # Have to turn ks into a real list before using [] to select an item
for k in ks:
    if d[k] > d[best_key_so_far]:
        best_key_so_far = k

print("key " + best_key_so_far + " has the highest value, " + str(d[best_key_so_far]))

# 1. Create a dictionary called d that keeps track of all the characters in the string placement and notes how many times each character was seen. Then, find the key with the lowest value in this dictionary and assign that key to min_value.

placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."

# count letters
d = {}
for c in placement:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1
        
keys = d.keys()
min_value = list(keys)[0]

for k in keys:
    if d[k] < d[min_value]:
        min_value = k 
        
print(min_value)

# Create a dictionary called lett_d that keeps track of all of the characters in the string product and notes how many times each character was seen. Then, find the key with the highest value in this dictionary and assign that key to max_value.

product = "iphone and android phones"

lett_d = {}
for c in product:
    if c not in lett_d:
        lett_d[c] = 1
    else:
        lett_d[c] += 1

d = lett_d.keys()
max_value = list(d)[0]

for k in d:
    if lett_d[k] > lett_d[max_value]:
        max_value = k

# Now that you have experience using lists and dictionaries, you will have to decide which one is best to use in each situation. The following guidelines will help you recognize when a dictionary will be beneficial:

# When a piece of data consists of a set of properties of a single item, a dictionary is often better. You could try to keep track mentally that the zip code property is at index 2 in a list, but your code will be easier to read and you will make fewer mistakes if you can look up mydiction[‘zipcode’] than if you look up mylst[2].

# When you have a collection of data pairs, and you will often have to look up one of the pairs based on its first value, it is better to use a dictionary than a list of (key, value) tuples. With a dictionary, you can find the value for any (key, value) tuple by looking up the key. With a list of tuples you would need to iterate through the list, examining each pair to see if it had the key that you want.

# On the other hand, if you will have a collection of data pairs where multiple pairs share the same first data element, then you can’t use a dictionary, because a dictionary requires all the keys to be distinct from each other.
