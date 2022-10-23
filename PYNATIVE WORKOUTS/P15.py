"""Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp."""


def exponent(base, exp):
    x = base ** exp
    print(base , 'raises to the power of ', exp, ': = ' , x)
    

print(exponent(2, 5))