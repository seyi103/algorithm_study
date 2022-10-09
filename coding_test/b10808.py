#b10808번 알파벳 개수
from collections import defaultdict
arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ans = []
cnt = defaultdict(int)
alphabet = list(input())
alphabet.sort()
temp = defaultdict(int)
for i in alphabet:
    temp[i] += 1

for i in arr:
    cnt[i] = temp[i]

for i in cnt:
    ans.append(cnt[i])

print(*ans)