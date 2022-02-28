#팀 결성
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

for _ in range(m):
  op, a, b = map(int, input().split())
  if op==0:
    union(parent, a, b)
  elif op==1:
    if find(parent, a) == find(parent, b):
      print("YES")
    else:
      print("NO")
