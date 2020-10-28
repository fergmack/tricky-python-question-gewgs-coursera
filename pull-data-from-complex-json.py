

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
