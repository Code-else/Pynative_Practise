"""Write a Program to extract each digit from an integer in the reverse order."""


num = 4567

def extract(x):
    x = str(x)
    x = x[::-1].split(" ")
    return x

print(extract(num))