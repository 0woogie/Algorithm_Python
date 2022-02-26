#화성 탐사
#내가 짠 코드라 업로드하긴 했지만 이코테 답안이 더 깔끔하다..다익스트라 개선 알고리즘 외워놓자
from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

t = int(input())
for _ in range(t):
  n = int(input())
  graph = []
  for _ in range(n):
    graph.append(list(map(int, input().split())))
  distance = [[INF]*n for _ in range(n)]

  q = deque([])
  q.append((0,0))
  distance[0][0] = graph[0][0]
  while q:
    x, y = q.pop()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<n and 0<=ny<n:
        if distance[x][y] + graph[nx][ny] < distance[nx][ny]:
          distance[nx][ny] = distance[x][y] + graph[nx][ny]
          q.append((nx, ny))

  print(distance[n-1][n-1])
