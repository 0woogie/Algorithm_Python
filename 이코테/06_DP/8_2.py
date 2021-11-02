#개미 전사
n = int(input())
array = list(map(int, input().split()))

d = [0]*100
d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
  a = array[i] + d[i-2]
  b = d[i-1]
  d[i] = max(a, b)

print(d[n-1])
