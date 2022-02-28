#도시 분할 계획
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [0]*(n+1)
for i in range(n+1):
  parent[i] = i

def union(parent, a, b):
  a = find(parent, a)
  b = find(parent, b)
  if a<b:
    parent[b] = a
  else:
    parent[a] = b

def find(parent, x):
  if parent[x]!=x:
    parent[x] = find(parent, parent[x])
  return parent[x]

edges = []
for _ in range(m):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))
edges.sort()

result = []
for cost, a, b in edges:
  if find(parent, a) != find(parent, b):
    result.append(cost)
    union(parent, a, b)

print(sum(result) - max(result))
