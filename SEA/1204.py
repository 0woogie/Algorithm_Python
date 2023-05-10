#[S/W 문제해결 기본] 1일차 - 최빈수 구하기
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    array = list(map(int, input().split()))
    grade = [0]*101
    for value in array:
        grade[value] += 1
    record = 0
    result = 0
    for i in range(len(grade)):
        if record <= grade[i]:
            record = grade[i]
            result = i
    print("#"+str(test_case), result)
