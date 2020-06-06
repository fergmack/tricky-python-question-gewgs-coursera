import string

s = "string. With. Punctuation?"
table = str.maketrans(dict.fromkeys(string.punctuation))  # OR {key: None for key in string.punctuation}
new_s = s.translate(table) 
