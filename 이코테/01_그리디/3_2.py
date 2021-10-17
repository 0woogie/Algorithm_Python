#큰 수의 법칙
n, m, k = map(int, input().split())
array = list(map(int, input().split()))

array.sort()
first = array[n-1]
second = array[n-2]

blockNum = m//(k+1)
sum = 0
sum += first*k + second
sum *= blockNum
sum += first*(m%(k+1))

print(sum)
