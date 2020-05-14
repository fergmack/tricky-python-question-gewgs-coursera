# sum the numbers up using a while loop

def sumTo(aBound):
  ''' The sum of 1+2+3...n'''
  theSum = 0 
  aNumber = 1
  while aNumber <= aBound:
    theSum = theSum + aNumber
    aNumber = aNumber + 1
  return theSum
