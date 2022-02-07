#경쟁적 전염
from collections import deque

n, k = map(int, input().split())

graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

s, a, b = map(int, input().split())

data = []
for i in range(n):
  for j in range(n):
    #해당 위치에 바이러스가 존재하는 경우
    if graph[i][j]!=0:
      #(바이러스 종류, 위치 x, 위치 y) 삽입
      data.append((graph[i][j],i,j))

#정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
queue = deque(data)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(s):
  
  #s+1초에 증식할 바이러스가 s초에 증식하는 것을 방지함
  t = len(queue)

  #큐가 빈 경우, 밑에 있는 반복문은 실행되지 않음
  #즉, 정확히 s초가 지나거나 큐가 빌 때까지 BFS를 수행함
  for _ in range(t):
    k, x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx<0 or nx>=n or ny<0 or ny>=n:
        continue

      #아직 방문하지 않은 위치 발견, 해당 위치에 바이러스 증식됨
      if graph[nx][ny]==0:
        graph[nx][ny] = k
        queue.append((k, nx, ny))

print(graph[a-1][b-1])
