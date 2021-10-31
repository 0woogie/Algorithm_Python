#부품 찾기
def binary_search(array, target, start, end):
  if start>end:
    return False
  mid = (start+end)//2
  if array[mid]==target:
    return True
  elif array[mid]>target:
    return binary_search(array, target, start, mid-1)
  else:
    return binary_search(array, target, mid+1, end)

n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
demand = list(map(int, input().split()))

for target in demand:
  result = binary_search(array, target, 0, n-1)
  if result==True:
    print("yes", end=' ')
  else:
    print("no", end=' ')
