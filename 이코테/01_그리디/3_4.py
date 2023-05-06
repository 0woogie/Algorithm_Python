#1이 될 때까지
n, k = map(int, input().split())
count = 0

while n>1:
  if n%k==0:
    n = n//k
  else:
    n -= 1
  count += 1

print(count)

'''
문제에서는 n의 범위가 10만 이하이므로, 이처럼 일일이 1씩 빼도 문제를 해결할 수 있다.
하지만, n이 100억 이상의 큰 수가 되는 경우를 가정했을 때에도 빠르게 동작하려면, 교재 '이코테' p.102를 참고하자.
'''
