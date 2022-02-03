#특정 거리의 도시 찾기
from collections import deque
import sys

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
#모든 도시에 대한 최단 거리 초기화
distance = [-1]*(n+1)
distance[x] = 0

for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)

queue = deque([x])

#BFS 수행
count = 0
while queue:
  now = queue.popleft()
  if distance[now]==k:
    count += 1
    break
  for i in graph[now]:
    if distance[i]==-1: #아직 방문하지 않은 도시인 경우
      queue.append(i)
      distance[i] = distance[now] + 1 #최단 거리 갱신
  
if count==1:
  for i in range(1, n+1):
    if distance[i]==k:
      print(i)
else:
  print(-1)
