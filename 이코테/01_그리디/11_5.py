#볼링공 고르기
n, m = map(int, input().split())
balls = list(map(int, input().split()))
result = 0

for i in range(n):
  for j in range(i+1, n):
    if balls[i] != balls[j]:
      result += 1

print(result)

'''
#개선된 풀이(이중루프 피하기, 최대 무게 m 활용하기)
n, m = map(int, input().split())
balls = list(map(int, input().split()))
result = 0

weight_list = [0]*(m+1)
for ball in balls:
  weight_list[ball] += 1

for i in range(1, m+1):
  n -= weight_list[i]
  result += weight_list[i]*n

print(result)
'''
