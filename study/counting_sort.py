array = [1, 3, 2, 4, 2, 5, 3, 1, 2, 3, 4, 4, 3, 5, 1, 2, 3, 5, 2, 3, 1, 4, 3, 5, 1, 2, 1, 1, 1]

# 계수정렬: 크기를 기준으로 세는 알고리즘
# 범위 조건이 필요, 빠름, 크기한정 필요
def counting_sort(array):
    count = [0] * (max(array) + 1) # 모든 범위를 포함하는 리스트
    #  각 값에 해당하는 인덱스의 값(개수) 증가
    for i in range(len(array)):
        count[array[i]] += 1
    # 인덱스 출력
    for i in range(len(count)):
        if (count[i] != 0):
            for j in range(len(count)):
                print(i, end=" ")

counting_sort(array)

'''
계수정렬은 크기를 기준으로 갯수를 세는 것을 통해 정렬하는 알고리즘

매우 빠르게( O(n+k) ) 정렬
1. array 내 모든 범위를 포함하는 리스트를 만들어 줌. 초기상태는 모든 값이 0인 상태

2. array의 원소를 하나씩 보면서, 해당되는 인덱스의 값(갯수)을 증가시킴

3. 증가된 갯수 리스트에서 0인 값을 제외하고, 인덱스와 인덱스 값(갯수)만큼 출력
'''