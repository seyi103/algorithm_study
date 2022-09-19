n = int(input())
array = []
for i in range(n):
    array.append(input())

set_word = list(set(array))
set_word.sort()
set_word.sort(key=len)
Len = len(set_word)
for i in range(Len):
    print(set_word[i])