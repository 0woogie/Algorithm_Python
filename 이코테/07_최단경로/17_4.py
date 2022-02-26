#숨바꼭질
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
  a, b = map(int, input().split())
  #a번 노드와 b번 노드의 이동 비용은 1 (양방향)
  graph[a].append((b, 1))
  graph[b].append((a, 1))

q = []
#1번 헛간이 시작 노드, 다익스트라 알고리즘 수행
heapq.heappush(q, (0, 1))
distance[1] = 0
while q:
  dist, now = heapq.heappop(q)
  if distance[now] < dist:
    continue
  for i in graph[now]:
    cost = dist + i[1]
    if cost < distance[i[0]]:
      distance[i[0]] = cost
      heapq.heappush(q, (cost, i[0]))

max_value = 0
for i in range(1, n+1):
  max_value = max(max_value, distance[i])

print(distance.index(max_value), max_value, distance.count(max_value))
