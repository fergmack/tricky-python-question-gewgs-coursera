from collections import defaultdict

s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1
    
print(d.items())
# Output: dict_items([('m', 1), ('i', 4), ('s', 4), ('p', 2)])
