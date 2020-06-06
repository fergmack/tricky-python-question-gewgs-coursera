# Write a function named string_processing that takes a list of strings as input and returns an all-lowercase string with no punctuation.

# There should be a space between each word. You do not have to check for edge cases.


import string
def string_processing(string_list):
  str1 = ""
  for ele in string_list:
    str1 += ele
    str1 += " "
  str2 = str1.lower().strip()
  table = str.maketrans(dict.fromkeys(string.punctuation))
  return str2.translate(table)
  
  
