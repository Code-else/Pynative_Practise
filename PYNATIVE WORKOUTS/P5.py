numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def check(listOf):
        if listOf[0] == listOf[-1]:
            print("result is true")
        else: print("result is false")

print(check(numbers_x))
print(check(numbers_y))