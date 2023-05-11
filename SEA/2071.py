#평균값 구하기
T = int(input())
for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    print("#"+str(test_case), round(sum(numbers)/len(numbers)))
    
'''
파이썬에서 반올림을 사용하고 싶을 때는 내장된 round() 함수를 사용하면 된다.

원래 2개의 인자를 받는데, 두 번째 인자가 생략되면 소수 첫째 자리에서 반올림한다.
print(round(1.2345, 1))		# result : 1.2
print(round(1.2345, 2))		# result : 1.23
print(round(1.2345, 3))		# result : 1.234

round() 함수는 사사오입 원칙을 따른다.
반올림할 자리의 수가 5이면 반올림 할 때 앞자리의 숫자가 짝수면 내림하고 홀수면 올림을 한다.
print(round(4.5))		# result : 4
print(round(3.5))		# result : 4
'''
