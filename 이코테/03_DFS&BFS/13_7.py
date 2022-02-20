#인구 이동
from collections import deque

n, l, r = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
  visit[i][j] = 1 #방문 처리
  union = [] #연합 국가를 위한 리스트
  union.append((i,j))
  queue = deque() #BFS 수행을 위한 큐
  queue.append((i,j))
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx<0 or nx>=n or ny<0 or ny>=n:
        continue
      if visit[nx][ny]==0 and l<=abs(graph[x][y]-graph[nx][ny])<=r: #연합에 추가할 국가라면
        visit[nx][ny] = 1 #방문 처리
        queue.append((nx,ny))
        union.append((nx,ny))
  value = 0
  for x, y in union:
    value += graph[x][y]
  value = value//len(union)
  for x, y in union:
    graph[x][y] = value #인구 분배

day = 0

while True:
  visit = [[0]*n for _ in range(n)]
  count = 0
  for i in range(n):
    for j in range(n):
      if visit[i][j]==0:
        bfs(i,j)
        count += 1
  if count==n*n: #더 이상의 인구 이동이 없다는 뜻
    break
  day += 1

print(day)
