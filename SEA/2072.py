#홀수만 더하기
T = int(input())
for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    result = 0
    for number in numbers:
        if number%2 != 0:
            result += number
    print("#" + str(test_case) + " " + str(result))
    
'''
#다른 방식으로 출력하기
print(f"#{i}", result)
'''
