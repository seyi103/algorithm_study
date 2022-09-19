array = [["잭", 90,  19961212], ["이중구", 85, 19960222] , ["레이", 82, 19961111], ["강요한", 98, 19961225], ["김정도", 90, 19961014]]
array.sort(key = lambda x:(x[1], x[2]))
print(array)

print(sorted(array, key = lambda x: (x[1], x[2])))


'''
튜플을 사용
example_tuples = [ ('A', 3, 'a'), ('B', 1, 'b'), ('C', 2, 'c') ]

# 정렬
# 튜플의 2번째 원소 기준으로 정렬
example_tuples.sort(key = lambda element : element[1])

print(example_tuples)

객체를 사용
class Example:
	def __init__(self, big, number, small):
		self.big = big
		self.number = number
		self.small = small

example_objects = [ Example('A', 3, 'a'), Example('B', 1, 'b'), Example('C', 2, 'c') ]

# 정렬
# 객체의 number 속성을 기준으로 정렬
example_objects.sort(key = lambda object : object.number)

for example_object in example_objects:
    print(example_object.big
          + " " + str(example_object.number)
          + " " + example_object.small)
'''