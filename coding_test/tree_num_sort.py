numbers = list(map(int, input().split()))
numbers.sort()
print(numbers[0], numbers[1], numbers[2])

'''
list(map(함수, 리스트))
sort
sort : 정렬, 기본값은 오름차순 정렬, reverse옵션 True는 내림차순 정렬
sort의 key 옵션, key 옵션에 지정된 함수의 결과에따라 정렬, 아래는 원소의 길이
'''
