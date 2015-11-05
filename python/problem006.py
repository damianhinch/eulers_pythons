"""
The sum of the squares of the first ten natural numbers is,

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

"""
If we convert the series of numbers 1..n squared and the series of number 1..n^2 and subract the 2 we simply
the calculation hugely and it becomes simply a matter of evaluating the formula:

DifferenceOfSums = n(3n + 2)(n-1)(n+1)/12
"""

n = 100

differenceOfSums = n*(3*n+2)*(n-1)*(n+1)/12

print "Difference is:", differenceOfSums