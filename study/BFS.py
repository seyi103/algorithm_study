from collections import deque

# BFS
def bfs(graph, start, visited):
  # 큐 구현을 위해 deque라이브러리 사용
  queue = deque([start])

  # 탐색 시작 노드를 방문 처리
  visited[start] = True

  # 큐가 빌 때까지 반복
  while queue:
    # 큐에서 하나의 원소를 꺼내서 출력
    n = queue.popleft()
    print(n, end='')

    # 꺼낸 원소와 인접노드 확인
    for i in graph[n]:
      # 아직 방문하지 않은 노드라면
      if not visited[i]:
        queue.append(i)
        visited[i]=True

# 2차원 맵정보 입력받기
graph=[
  [], # 0번 노드 비우기
  [2,3], #1번 노드와 연결된 2,3,8노드
  [1,4,5],
  [1,6,7],
  [2,4],
  [2,5],
  [3,6],
  [3,7]
]

# 방문 정보
visited = [False]*(8+1) #(총 노드의 갯수)+인덱스 0
# bfs호출
bfs(graph, 1, visited)