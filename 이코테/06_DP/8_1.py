#1로 만들기
x = int(input())
d = [0]*30001

for i in range(2, x+1):
  array  = []
  if i%5==0:
    array.append(d[i//5])
  if i%3==0:
    array.append(d[i//3])
  if i%2==0:
    array.append(d[i//2])
  array.append(d[i-1])
  d[i] = min(array) + 1

print(d[x])
