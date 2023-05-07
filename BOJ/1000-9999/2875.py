#대회 or 인턴
n, m, k = map(int, input().split())
count = 0
while True:
    if n>=2 and m>=1 and n+m-3>=k:
        n -= 2
        m -= 1
        count += 1
    else:
        break
print(count)

'''
다른 풀이(덜 직관적)
n, m, k = map(int, input().split())
count = 0

while True:
  if count>=k:
    break
  if n>m*2:
    count += n - m*2
    n = m*2
  elif m*2>n:
    count += m - n//2
    m = n//2
  else: # n == m*2
    count += 3
    n -= 2
    m -= 1

print(m)
'''
