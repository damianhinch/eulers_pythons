'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example,  3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

a = 0  # starting values considering that a < b < c
b = 1
c = 2
product = 1000
found = False

while (c in range(2, 500)) and ((found != True)):  # if abc = 1000 c can't be more than 500
    c += 1
    b = 1 # reset b
    while (b < c-1) and ((found != True)):  # b must be less than c and more than a
        b += 1
        cPow2 = pow(c, 2)
        bPow2 = pow(b, 2)
        if (pow(product - b - c, 2) + bPow2) == cPow2:
            a = product - b -c
            found = True

if (found):
    print("Triplet is a:{} b:{} c:{} with product:{}".format(a, b, c, a*b*c))
else:
    print("Not found")
