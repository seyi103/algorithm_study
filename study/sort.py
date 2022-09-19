'''def Sort():
    arr = [9, 3, 5, 4, 1, 10, 8, 6, 7, 2]
    arr.sort(reverse=True) #reverse=True이면 내림차순 정렬/ 기본 오름차순
    print(arr)

Sort()'''

class student:
    def __init__(self, name, score) -> None:
        self.name = name
        self.score = score
    
    def __repr__(self):
        return repr((self.name, self.score))

student_objects = [
    student("이홍기", 90),
    student("김정도", 93),
    student("강요한", 97),
    student("이중구", 87),
    student("박평호", 92),
]

sorted_myclass = sorted(student_objects, key=lambda student: student.score) # sort by score
print(sorted_myclass)

'''
sorted()
 
Prototype
sorted( <list> , key = <function> , reverse = <bool>)
# <list> 뿐 아니라, <Tuple>, <Dictionary>, <Str>에도 사용 가능하다.
원본 내용을 바꾸지 않고, 정렬한 값을 반환한다.
List, tuple, Dictionary, str에 모두 사용 가능하다.
key 를 통하여 정렬할 기준을 정할 수 있다.
reverse 가 True이면 내림차순, False이면 오름차순으로 정렬된다.

sort()
 
Prototype
<list>.sort(key = <function>, reverse = <bool>)
원본 자체를 수정한다.
반환값은 None
Tuple , Dictionary, Str 에는 사용이 불가하다.
key값을 사용하면 여러가지 기준으로 정렬을 실행할 수 있다.
'''