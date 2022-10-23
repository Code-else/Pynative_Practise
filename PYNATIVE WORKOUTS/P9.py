"""Write a program to check if the given number is a palindrome number.

A palindrome number is a number that is same after reverse. 
For example 545, is the palindrome numbers"""


number_1 = "121"
number_2 = "125"

def palindrome(x):
    if x[::-1] == x:
        return "Yes, given number is Palindrome"
    else: 
        return "No. given number is not palindrome number"

print(palindrome(number_1))
print(palindrome(number_2))