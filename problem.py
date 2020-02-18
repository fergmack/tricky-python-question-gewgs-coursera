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
