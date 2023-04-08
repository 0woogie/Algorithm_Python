#날짜 계산
E, S, M = map(int, input().split())
e = s = m = count = 1

while True:
  if e==E and s==S and m==M:
    break
  e += 1
  s += 1
  m += 1
  count += 1
  if e==16:
    e = 1
  if s==29:
    s = 1
  if m==20:
    m = 1

print(count)
