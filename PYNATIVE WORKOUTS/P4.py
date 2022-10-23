"""Write a program to remove characters 
from a string starting from zero up to n and return a new string."""

def txt(word, n):
    x = word[n:]
    return x

print(txt("pynative", 4))
print(txt("Pynative", 2))