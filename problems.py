# if size = 1 then the blocks size will be 4096, if over 4096 then the blocks size will be 2xblock_size etc
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block = filesize % block_size
    # Depending on whether there's a remainder or not, return the right number.
    if filesize < 4096:
        return block_size
    elif partial_block > 0:
        return full_blocks * block_size + block_size    
    return full_blocks * block_size


print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192

# Calculate smallest prime factor
def smallest_prime_factor(x):
    """Returns the smallest prime number that is a divisor of x"""
    # Start checking with 2, then move up one by one
    n = 2
    while n <= x:
        if x % n == 0:
            return n
        n += 1

print(smallest_prime_factor(12)) # should be 2
print(smallest_prime_factor(15)) # should be 3

# Fill in the blanks to make the print_prime_factors function print all the prime factors of a number. A prime factor is a number that is prime and divides another without a remainder.
# Note the instructions on this are a bit confusing
def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor += 1
  return "Done"

print_prime_factors(100) # Should print 2,2,5,5

# The following code can lead to an infinite loop. Fix the code so that it can finish successfully for all numbers.
# Note: Try running your function with the number 0 as the input, and see what you get!
# FIXED
def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  while n % 2 == 0 and n != 0:
    n = n / 2
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False
  
is_power_of_two(0)

# Fill in the empty function so that it returns the sum of all the divisors of a number, without including it. A divisor is a number that divides into another without a remainder.
def sum_divisors(n):
  i = 1
  sum_no = 0
  while i < n:
    if n % i == 0:
      sum_no += i
    i += 1
  return sum_no


print(sum_divisors(6)) # Should be 1+2+3=6
print(sum_divisors(12)) # Should be 1+2+3+4+6=16

# -- Week 3 Practice: For Loops
# Fill in the blanks to make the factorial function return the factorial of n. Then, print the first 10 factorials (from 0 to 9) with the 
# corresponding number. Remember that the factorial of a number is defined as the product of an integer and all integers before it. 
# For example, the factorial of five (5!) is equal to 1*2*3*4*5=120. Also recall that the factorial of zero (0!) is equal to 1.

def factorial(n):
    result = 1
    if n ==0:
      n=1
    for x in range(1, n+1):
        result = result*x
    return result

for n in range(10):
    print(n, factorial(n))
    
# Write a script that prints the first 10 cube numbers (x**3), starting with x=1 and ending with x=10.
for x in range(1, 11):
  cube = x**3
  print(x, cube)
    
#     Write a script that prints the multiples of 7 between 0 and 100. Print one multiple per line and avoid printing 
#     any numbers that aren't multiples of 7. Remember that 0 is also a multiple of 7.
for x in range(0, 101):
  if x % 7 ==0:
    print(x)

# The retry function tries to execute an operation that might fail, it retries the operation for a number of attempts.
# Currently the code will keep executing the function even if it succeeds. Modify the code so that it stops trying after the
# operation succeeded.

def retry(operation, attempts):
  for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
      break #add a break in here
    else:
      print("Attempt " + str(n) + " failed")
    
retry(create_user, 3)
retry(stop_service, 5)

# Fill in the blanks to make the is_power_of function return whether the number is a power of the given base.
# Note: base is assumed to be a positive number. 
# Tip: for functions that return a boolean value, you can return the result of a comparison.
def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return number == 1
  # Recursive case: keep dividing number by base.
  return is_power_of(number // base, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False

# The count_users function recursively counts the amount of users that belong to a group in the company system, 
# by going through each of the members of a group and if one of them is a group, 
# recursively calling the function and counting the members. But it has a bug! Can you spot the problem and fix it?
def count_users(group):
  count = 0
  for member in get_members(group):
    count += 1
    if is_group(member):
      count += count_users(member)
      count += -1
  return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18

# Implement the sum_positive_numbers function, as a recursive function that returns the sum of
# all positive numbers between the number n received and 1. For example, when n is 3 it should return 1+2+3=6, 
# and when n is 5 it should return 1+2+3+4+5=15.
def sum_positive_numbers(n):
  # the base case is n being smaller than 1
  if n < 1:
    return 0
  
  #  recursive case is adding n to  the function call where n-1
  return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

# Fill in the blanks of this code to print out the numbers 1 through 7.
number = 1
while number != 8:
	print(number, end=" ")
	number += 1
    
# The show_letters function should print out each letter of a word on a separate line. Fill in the blanks to make that happen.
def show_letters(word):
	for l in word:
		print(l)

show_letters("Hello") # Should print one line per letter

# Complete the function digits(n) that returns how many digits the number has. For example: 25 has 2 digits and 144 has 3 digits. 
# Tip: you can figure out the digits of a number by dividing it by 10 once per digit until there are no digits left
def digits(n):
	count = 0
	if n == 0:
	  print (1)
	while (n>0):
		count += 1
		n = n // 10
	return count
	
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1

# This function prints out a multiplication table (where each number is the result of 
#  multiplying the first number of its row by the number at the top of its column). 
# Fill in the blanks so that calling multiplication_table(1, 3) will print out:

# 1 2 3
# 2 4 6
# 3 6 9

def multiplication_table(start, stop):
	for x in range(start, stop+1):
		for y in range(start, stop+1):
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3) # Should print the multiplication table shown above

# The counter function counts down from start
# to stop when start is bigger than stop, and counts up from start to stop otherwise. 
# Fill in the blanks to make this work correctly.

def counter(start, stop):
	x = start
	if start > stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			x = x-1
			if x >= stop:
				return_string += ","
		return return_string
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x < stop:
				return_string += ","
			x += 1
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"

#####

# The loop function is similar to range(), but handles the parameters somewhat differently: it takes in 3 parameters: the starting point, the stopping point, and the increment step. When the starting point is greater than the stopping point, it forces the steps to be negative. When, instead, the starting point is less than the stopping point, it forces the step to be positive. Also, if the step is 0, it changes to 1 or -1. The result is returned as a one-line, space-separated string of numbers. For example, loop(11,2,3) should return 11 8 5 and loop(1,5,0) should return 1 2 3 4. Fill in the missing parts to make that happen.

def loop(start, stop, step):
	return_string = ""
	if step == 0:
		step = 1
	if start > stop:
		step = abs(step) * -1
	else:
		step = abs(step)
	for count in range(start, stop, step):
		return_string += str(count) + " "
	return return_string.strip()

print(loop(11,2,3)) # Should be 11 8 5
print(loop(1,5,0)) # Should be 1 2 3 4
print(loop(-1,-2,0)) # Should be -1
print(loop(10,25,-2)) # Should be 10 12 14 16 18 20 22 24 
print(loop(1,1,1)) # Should be empty

# Fill in the gaps in the initials function so that it returns the initials of the words contained in the phrase received, in upper case. 
# For example: "Universal Serial Bus" should return "USB"; "local area network" should return "LAN”.
def initials(phrase):
    words = phrase.upper()
    words = words.split(' ')
    result = ""
    for l in words:
        result += l[0]
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS

# Modify the student_grade function using the format method, so that it returns the phrase "X received Y% on the exam". 
# For example, student_grade("Reed", 80) should return "Reed received 80% on the exam".
def student_grade(name, grade):
	return "{name} received {grade}% on the exam".format(name=name, grade=grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

# The group_list function accepts a group name and a list of members, and returns a string with theformat: group_name: member1, member2,… 
# For example, group_list("g", ["a","b","c"]) returns "g: a, b, c". Fill in the gaps in this function to do that.
def group_list(group, users):
  members = group +":" + ",".join(users)
  return members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

# The skip_elements function returns every other element from the list, 
# starting from the first. Complete this function to do that.
def skip_elements(elements):
  second_elements = []
  for e in elements:
    if elements.index(e) % 2 == 0:
      second_elements.append(e)
  return second_elements

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []

# The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints the sentence
# "Guest is X years old and works as __." for each one. 
# For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out:
# Ken is 30 years old and works as Chef.
# Pat is 35 years old and works as Lawyer.
# Amanda is 25 years old and works as Engineer.

def guest_list(guests):
	for i in guests:
		name, age, job = i
		print("{} is {} years old and works as {}.".format(name, age, job))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

# Try out the enumerate function for yourself in this quick exercise. Complete the skip_elements function to return every other 
# element from the list, this time using the enumerate function to check if an element is on an even position or an odd position.

def skip_elements(elements):
  skipped =[]
  for index, element in enumerate(elements):
    if index % 2 == 0:
      skipped.append(element)
  return skipped

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

# Complete the skip_elements function to return every other element from the list, this time using a 
# list comprehension to generate the new list based on the previous one, where elements in odd positions are skipped.
def skip_elements(elements):
  return [element for index, element in enumerate(elements) if index % 2 == 0 ]

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

# ---- From the Coursera Michigan Python3 Specilization ---- #
# Count how many times a character occurs in a body of text
f = open('scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
letter_counts = {} # start with an empty dictionary
for c in txt:
    if c not in letter_counts:
        # we have not seen this character before, so initialize a counter for it
        letter_counts[c] = 0

    #whether we've seen it before or not, increment its counter
    letter_counts[c] = letter_counts[c] + 1

for c in letter_counts.keys():
    print(c + ": " + str(letter_counts[c]) + " occurrences")

# The "toc" dictionary represents the table of contents for a book. Fill in the blanks to do the following: 
# 1) Add an entry for Epilogue on page 39. 2) Change the page number for Chapter 3 to 24. 3)
# Display the new dictionary contents. 4) Display True if there is Chapter 5, False if there isn't.

toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
# Epilogue starts on page 39
# Chapter 3 now starts on page 24
# What are the current contents of the dictionary?
# Is there a Chapter 5?

toc['Epilogue'] = 39
toc['Chapter 3'] = 24
print(toc)
print('Chapter 5' in toc)
# ---------------------------
# Lists - quite tricky problems
# Given a list of filenames, we want to rename all the files with the extension hpp to the extension h by generating a list of tuples of the form (old_name, new_name).

# That is, given the following list of filenames

# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

# complete the starter code to generate the following newfilenames list of tuples

# newfilenames = [('program.c', 'program.c'), ('stdio.hpp', 'stdio.h'), ('sample.hpp', 'sample.h'), ('a.out', 'a.out'), ('math.hpp', 'math.h'), ('hpp.out', 'hpp.out')]
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = [] 

for orig in filenames:
  tuple_file = ()
  if '.hpp' in orig:
    new = orig.replace('.hpp', '.h')
    tuple_file = (orig, new)
    newfilenames.append(tuple_file)
  else:
    tuple_file = (orig, orig)
    newfilenames.append(tuple_file)
    

print (newfilenames) # Should be [('program.c', 'program.c'), ('stdio.hpp', 'stdio.h'), ('sample.hpp', 'sample.h'), ('a.out', 'a.out'), ('math.hpp', 'math.h'), ('hpp.out', 'hpp.out')]

# ** go over again!
# The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute for the owner, group, and others.
# Each of the three values can be expressed as an octal number summing each permission, with 4 corresponding to read, 2 to write, 
# and 1 to execute. Or it can be written with a string using the letters r, w, and x or - when the permission is not granted. 
# For example: 640 is read/write for the owner, read for the group, and no permissions for the others; 
# converted to a string, it would be: "rw-r-----" 755 is read/write/execute for the owner, and read/execute for group and others;converted to a 
# string, it would be: "rwxr-xr-x" Fill in the blanks to make the code convert a permission in octal format into a string format.

def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for p in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if p >= value:
                result += letter
                p -= value
            else:
                result += "-"
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------


# Let's create a function that turns text into pig latin: a simple text transformation
# that modifies each word moving the first character to the end and appending "ay" to the end. 
# For example, python ends up as ythonpay.
def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split(" ")
  for word in words:
    # print(word)
    # Create the pig latin word and add it to the list
    x = word[:1]
    # Turn the list back into a phrase
    y = word[1:] + x
    y = y + 'ay'
    y = y + " "
    say += y
  return (say)
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

# -- Dictionaries 
# Now, it's your turn! Have a go at iterating over a dictionary!

# Complete the code to iterate through the keys and values of the cool_beasts dictionary. 
# Remember that the items method returns a tuple of key, value for each element in the dictionary.
cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for key, value in cool_beasts.items():
    print("{} have {}".format(key, value))

# In Python, a dictionary can only hold a single value for a given key. To workaround this, our single value can be a list
# containing multiple values. Here we have a dictionary called "wardrobe" with items of clothing and their colors. 
# Fill in the blanks to print a line for each item of clothing with each color, for example: "red shirt", "blue shirt", and so on.

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for item in wardrobe:
  for color in wardrobe[item]:
    print("{} {}".format(color, item))

# *** Go over this - cause a lot of trouble ***
# The groups_per_user function receives a dictionary, which contains group names with the list of users.
# Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list
# of their groups as values.
def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
		  if user in user_groups.keys():
		    user_groups[user].append(group)
		  else:
		    user_groups[user] = [group]

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

# -- Week 4 course 1: Works but not the best solution probably -- 
# The format_address function separates out parts of the address string into new strings: house_number and street_name, and returns:
# "house number X on street named Y". The format of the input string is: numeric house number, followed by the street name which 
# may contain numbers, but never by themselves, and could be several
# words long. For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". 
# Fill in the gaps to complete this function.

def format_address(address_string):
  # Declare variables
  num = 0
  street = ''

  # Separate the address string into parts
  address_parts = address_string.split(' ')

  # Traverse through the address parts
  for part in address_parts:
    # Determine if the address part is the
    # house number or part of the street name
    if part == address_parts[0]:
      num = str(part)
    else:
      street += part 
      street += ' ' 
    

  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
  return "house number {} on street named {}".format(num, street)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

# Question 2
# The highlight_word function changes the given word in a sentence to its upper-case version. 
# For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". 
# Can you write this function in just one line?

def highlight_word(sentence, word):
	return(sentence.replace(word, word.upper()))

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

# A professor with two assistants, Jamie and Drew, wants an attendance list of the students, in the order that they arrived in the classroom.
# Drew was the first one to note which students arrived, and then Jamie took over. After the class, they each entered their lists into the 
# computer and emailed them to the professor, who needs to combine them into one, in the order of each student's arrival. Jamie emailed a
# follow-up, saying that her list is in reverse order. Complete the steps to combine them into one list as 
# follows: the contents of Drew's list, followed by Jamie's list in reverse order, to get an accurate list of the students as they arrived.
def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  # reverse the list using [::-1]
  list1_reversed = list1[::-1]
  full_list = list2 + list1_reversed
  return full_list

Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

# Use a list comprehension to create a list of squared numbers (n*n). The function receives the variables start and end, 
# and returns a list of squares of consecutive numbers between start and end inclusively. For example, squares(2, 3) should return [4, 9].
def squares(start, end):
  squares = []
  for i in range(start, end+1):
    sq = i * i
    squares.append(sq)
  return squares

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Complete the code to iterate through the keys and values of the car_prices dictionary, printing out some information about each one.
def car_listing(car_prices):
  result = ""
  for key, value in car_prices.items():
    result += "{} costs {} dollars".format(key, value) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

# Taylor and Rory are hosting a party. They sent out invitations, and each one collected responses into dictionaries, with names of their
# friends and how many guests each friend is bringing. Each dictionary is a partial list, but Rory's list has more current information 
# about the number of guests. Fill in the blanks to combine both dictionaries into one, with each friend listed only once, and the number
# of guests from Rory's dictionary taking precedence, if a name is included in both dictionaries. Then print the resulting dictionary.
def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence
  # code below makes guests1 take precedence over guests2
  return (dict(guests2, **guests1))

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))

# Use a dictionary to count the frequency of letters in the input string. Only letters should be counted, not blank spaces,
# numbers, or punctuation. Upper case should be considered the same as lower case. For example, count_letters("This is a sentence.")
# should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.

def count_letters(text):
    result = {}
    # text = text.replace(' ', '')
    # text = text.replace('.', '')
    # text = text.replace('!', '')
    # text = text.replace(',', '')
  # Go through each letter in the text
    # Add or increment the value in the dictionary
    for letter in text.lower():
      # isalpha() checks to see if it's an alphabetic letter
        if letter.isalpha() and letter not in result:
            result[letter] = 1
        elif letter.isalpha():
            result[letter] += 1
    return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

# What does the list "colors" contain after these commands are executed?
colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
# productes red, white, yellow, blue

# What do the following commands return?
host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
host_addresses.keys()
# prints the keys router, localhost, google
