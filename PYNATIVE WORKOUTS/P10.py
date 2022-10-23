list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]


def odd_list(x, y):
    result_list = []


    for i in x:
        if i % 2 != 0:
             result_list.append(i)

    for i in y:
        if i % 2 == 0:
         result_list.append(i)

    return result_list

print(odd_list(list1, list2))  