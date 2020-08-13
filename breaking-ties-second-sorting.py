# In the code below, we are going to sort a list of fruit words first by their length, smallest to largest, and then alphabetically to break ties among words of the same length. To do that, we have the key function return a tuple whose first element is the length of the fruit’s name, and second element is the fruit name itself.

fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name))
for fruit in new_order:
    print(fruit)
