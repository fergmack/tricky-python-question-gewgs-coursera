# Create a shopping list counter 
# In a grocery store, there’s a little plastic bar that you put after your last item to separate your groceries from those of the person behind you; that’s how the clerk knows you have no more items. We don’t have a “little plastic bar” data type in Python, so we’ll do the next best thing: we will use a price of zero to mean “this is my last item.” In this program, zero is a sentinel value, a value used to signal the end of the loop. Here’s the code:

# If you enter a negative number, it will be added to the total and count. Modify the code so that negative numbers give an error message instead (but don’t end the loop) Hint: elif is your friend.

# If you enter zero the first time you are asked for a price, the loop will end, and the program will try to divide by zero. Use an if/else statement outside the loop to avoid the division by zero and tell the user that you can’t compute an average without data.

# This program doesn’t display the amounts to two decimal places. You’ll be introduced to that in another chapter.

def checkout():
    total = 0
    count = 0
    moreItems = True
    average = 0
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price != 0 and price > 0:
            count = count + 1
            total = total + price
            print('Subtotal: $', total)    
        elif price < 0:
            print("Please enter a positive amount")
        else:
            moreItems = False
    if price ==  0:
        print("Cannot compute average without data")
    else:
        average = total / count
    print('Total items:', count)
    print('Total $', total)
    print('Average price per item: $', average)

checkout()
