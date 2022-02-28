#어두운 길
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [0]*n
for i in range(n):
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
total = 0
for _ in range(m):
  a, b, cost = map(int, input().split())
  total += cost
  edges.append((cost, a, b))
edges.sort()

result = 0
for cost, a, b in edges:
  if find(parent, a) != find(parent, b):
    union(parent, a, b)
    result += cost

print(total - result)
