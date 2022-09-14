def insertion_sort(arr):
    length = len(arr)
    for end in range(1, len(arr)):
        to_insert = arr[end]
        i = end
        while i > 0 and arr[i - 1] > to_insert:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = to_insert
    return arr

arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
insertion_sort(arr)
print(arr)
'''
선택/거품 정렬은 패스가 거듭될 수록 탐색 범위가 줄어드는 반면에 삽입 정렬은 오히려 점점 정렬 범위가 넚어짐 
큰 크림에서 보았을 때 바깥 쪽 루프는 순방향, 안 쪽 루프는 역방향으로 진행

공간 복잡도: O(1)
시간 복잡도: O(N^2)
최적화를 통해서 부분적으로 정렬된 배열에 대해서 성능을 대폭 개선할 수 있으며, 특히 완전히 정렬되어 있는 배열이 들어올 경우, O(N)까지도 시간 복잡도를 향상시킬 수 있습니다.
거의 정렬된 상태라면 어떤 알고리즘보다 빠름
'''
