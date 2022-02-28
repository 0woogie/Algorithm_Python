#여행 계획
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

for i in range(n):
  tmp = list(map(int, input().split()))
  for j in range(n):
    if tmp[j]==1:
      union(parent, i+1, j+1)

city = list(map(int, input().split()))
result = True
for i in range(m-1):
  if find(parent, city[i]) != find(parent, city[i+1]):
    result = False

if result:
  print("YES")
else:
  print("NO")
