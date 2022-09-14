from array import array

def selection_sort():
    min = 0
    index = 0
    temp = 0
    arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
    length = len(arr)
    for i in range(length):
        min = 99
        for j in range(i,length):
            if(min > arr[j]):
                min = arr[j]
                index = j
        #가장 앞 값과 최솟값의 위치 교환        
        temp = arr[i]
        arr[i] = arr[index]
        arr[index] = temp
    for i in range(length):
        print(arr[i])
    return 0

selection_sort()

'''
시간 복잡도
10+9+8+...+1
=> 10*(10+1)/2 = 55
=> N*(N+1)/2
=>N*N
=>O(N*N)
=>O(N^2)
'''