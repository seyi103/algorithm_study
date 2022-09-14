def quick_sort(arr):
    def sort(low, high):
        if (high >= low):
            return
        mid = partition(low, high)
        sort(high, mid-1)
        sort(mid, low)

    def partition(low, high):
        pivot = arr[(low+high)//2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if(low <= high):
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return high 
    return sort(0, len(arr) - 1)

arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
quick_sort(arr)
print(arr)
'''
파이썬의 list.sort() 함수나 자바의 Arrays.sort()처럼 프로그래밍 언어 차원에서 기본적으로 지원되는 내장 정렬 함수는 대부분은 퀵 정렬을 기본으로 합니다.
일반적으로 원소의 개수가 적어질수록 나쁜 중간값이 선택될 확률이 높아지기 때문에, 원소의 개수에 따라 퀵 정렬에 다른 정렬을 혼합해서 쓰는 경우가 많습니다.
병합 정렬과 퀵 정렬은 분할 정복과 재귀 알고리즘을 사용한다는 측면에서는 유사해보이지만, 내부적으로 정렬을 하는 방식에서는 큰 차이가 있습니다.
병합 정렬은 항상 정 중앙을 기준으로 단순 분할 후 병합 시점에서 값의 비교 연산이 발생하는 반면, 퀵 정렬은 분할 시점부터 비교 연산이 일어나기 때문에 그 이후 병합에 들어가는 비용이 매우 적거나 구현 방법에 따라서 아예 병합을 하지 않을 수도 있습니다.

시간 복잡도: O(nlog(n))
공간 복잡도: in-place sorting 방식으로 구현을 사용할 경우, O(log(n))
중앙값(median)에 가까운 pivot 값을 선택할 수 있는 전략 필요
이미 정렬이 되어있거나 거의 정렬이 되어있는 경우O(n^2)
'''
