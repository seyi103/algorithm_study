from array import array

def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
selection_sort(arr)
'''
시간 복잡도
10+9+8+...+1
=> 10*(10+1)/2 = 55
=> N*(N+1)/2
=>N*N
=>O(N*N)
=>O(N^2)
'''
