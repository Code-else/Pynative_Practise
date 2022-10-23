"""Calculate income tax for the given income by adhering to the below rules"""

def income_tax(Amount, ROT):

    tax = (Amount*ROT) / 100

    return tax

print(income_tax(10000, 10))