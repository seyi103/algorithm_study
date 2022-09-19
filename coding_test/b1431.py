n = int(input())
array = []
for i in range(n):
    array.append(input())

def sum_num(inputs):
    result = 0
    for i in inputs:
        if i.isdigit():
            result+=int(i)
    return result

array.sort(key = lambda x:(len(x), sum_num(x), x))

Len = len(array)
for i in range(Len):
    print(array[i])