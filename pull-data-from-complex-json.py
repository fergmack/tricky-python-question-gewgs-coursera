# Follow the system described below and you will have success with extracting nested data. The process involves the following steps:

# Understand the nested data object.

# Extract one object at the next level down.

# Repeat the process with the extracted object

# Understand. Extract. Repeat.

# Print the entire object. If it’s small enough, you may be able to make sense of the printout directly. If it’s a little bit larger, you may find it helpful to “pretty-print” it, with indentation showing the level of nesting of the data. We don’t have a way to pretty-print in our online browser-based environment, but if you’re running code with a full Python interpreter, you can use the dumps function in the json module. For example:

import json
print(json.dumps(res, indent=2))

# If printing the entire object gives you something that’s too unwieldy, you have other options for making sense of it.

# Copy and paste it to a site like https://jsoneditoronline.org/ which will let you explore and collapse levels

# Print the type of the object.

# If it’s a dictionary:
# print the keys

# If it’s a list:
# print its length

# print the type of the first item

# print the first item if it’s of manageable size

import json
print(type(res)) # check type
print(res.keys()) # it's a dictionary so print keys. note it returns a list of the dict's keys
res2 = res['statuses'] # select the key you want (this will get it's values)
print("----Level 2: a list of tweets-----") # jump into level 2
print(type(res2)) # check type. it's a list!
print(len(res2))  # check it's length. looks like one item representing each of the three tweets
for res3 in res2: # because it's a list, sequence through it to get to level 3
   print("----Level 3: a tweet----") 
   print(json.dumps(res3, indent=2)[:30]) # print it to check. looks like we want user
   res4 = res3['user'] # grab user to go down one more level
   print("----Level 4: the user who wrote the tweet----")
   print(type(res4)) # check type. it's a dictionary. it returns a list of the dict's keys
   print(res4.keys()) # as it's a dictionary, check keys. it returns a list of the dict's keys
   print(res4['screen_name'], res4['created_at']) # grab the valaues in these keys 'screen_name' etc
