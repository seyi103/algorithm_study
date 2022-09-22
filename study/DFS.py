graph = dict()
 
graph[1] = [2, 3]
graph[2] = [1, 3, 4, 5]
graph[3] = [1, 6, 7]
graph[4] = [2, 5]
graph[5] = [2, 4]
graph[6] = [3, 7]
graph[7] = [3, 6]


def dfs_recursive(graph, start, visited = []):
## 데이터를 추가하는 명령어 / 재귀가 이루어짐 
    visited.append(start)
    print(start, end='')

    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited

dfs_recursive(graph, 1)

'''
Q1. 음료수 얼려 먹기
# 세로n, 가로m
n, m = map(int, input().split())

# 2차원 맵정보 입력받기
graph=[]
for i in range(n):
  graph.append(list( map(int, input()) ))

# dfs로 특정한 방문한 뒤에 인접 노드들도 방문
def dfs(x,y):
  # 주어진 범위를 벗어날시에 종료
  if x<0 or y<0 or x>n-1 or y>m-1:
    return False

  # 방문할 수 있는 노드라면 방문
  if graph[x][y]==0:
    graph[x][y]=1 # 방문처리
  
    # 인접한 노드들(상하좌우)에 대해 반복 수행
    dfs(x-1,y) # 상
    dfs(x+1,y) # 하
    dfs(x,y-1) # 좌
    dfs(x,y+1) # 우
    return True

  return False

# 아이스크림 수 세기
result = 0
for i in range(n):
  for j in range(m):
    # 현재 위치에서 DFS 수행
    # 애초에 1이였거나 방문하여 1이되었거나 범위를 벗어난 경우라면
    # false를 리턴한다.
    # 만약 True라면 이전에 방문하지 않은 새로운 아이스크림이다
    if dfs(i,j) == True:
      result +=1

print(result)

Q1. 왕실의 나이트
position = input()

# 이동방향 정의
move_col = [2, 2, -2, -2, 1, 1, -1, -1]
move_row = [1, -1, 1, -1, 2, -2, 2, -2]

# 이동 가능한 방향의 갯수 구하기
count = 0
for i in range(len(move_col)):
  next_col = ord(position[0]) + move_col[i]
  next_row = int(position[1]) + move_row[i]

  # 해당 방향으로 이동 가능 여부
  if ord('a')<=next_col<=ord('h') and 1<=next_row<=8:
    count += 1

print(count)
'''