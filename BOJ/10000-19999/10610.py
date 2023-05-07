#30
s = input()
numbers = []
for x in s:
    numbers.append(int(x))
if sum(numbers)%3!=0 or 0 not in numbers:
    print(-1)
else:
    numbers.sort(reverse=True)
    print(''.join(list(map(str,numbers))))
    
'''
#30의 배수가 되는 조건
1. 일의 자리수가 0이여야 함.
2. 각 자리의 숫자들을 더했을때 3으로 나누어 떨어져야함.
'''
