# 두 배열의 원소 교체
n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse = True)

for i in range(k):
  if A[i] < B[i]:
    A[i], B[i] = B[i], A[i]
  else:
    break #더 이상 반복문을 수행하더라도 바꿔치기 연산이 일어날 일이 없기에 반복문 탈출

print(sum(A))
