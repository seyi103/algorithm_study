#N(1 ≤ N ≤ 1,000)

arr = []
num = int(input())
for i in range(num):
    arr.append(int(input()))

length = len(arr)

def bubble(arr):
    length = len(arr)
    end = len(arr) - 1
    while end > 0:
        last_swap = 0
        for i in range(end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                last_swap = i
        end = last_swap
    return arr

bubble(arr)
for i in range(length):
    print(arr[i])
