
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

arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
bubble(arr)
print(arr)
'''
공간 복잡도: O(1)
시간 복잡도: O(N^2)
완전히 정렬되어 있는 배열이 들어올 경우, O(N)까지도 시간 복잡도를 향상시킬 수 있음
'''
