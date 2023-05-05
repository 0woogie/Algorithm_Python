#백만 장자 프로젝트
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    array = list(map(int, input().split()))
    array.reverse()
    result = 0
    maxPrice = array[0]
    for number in array:
        if number > maxPrice:
            maxPrice = number
        else:
            result += maxPrice - number
    print("#" + str(test_case) + " " + str(result))
    
'''
# 아이디어는 리스트 거꾸로 접근하기
'''
