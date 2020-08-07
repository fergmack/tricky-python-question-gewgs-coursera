# We will generally use an alternative way of sorting, the function sorted rather than the method sort. Because it is a function rather than a method, it is invoked on a list by passing the list as a parameter inside the parentheses, rather than putting the list before the period. More importantly, sorted does not change the original list. Instead, it returns a new list.

L2 = ["Cherry", "Apple", "Blueberry"]

L3 = sorted(L2)
print(L3)
print(sorted(L2))
print(L2) # unchanged

print("----")

L2.sort()
print(L2)
print(L2.sort())  #return value is None

# Sort the list, lst from largest to smallest. Save this new list to the variable lst_sorted.

lst = [3, 5, 1, 6, 7, 2, 9, -2, 5]
lst_sorted = sorted(lst, reverse=True)

