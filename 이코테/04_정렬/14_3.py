#실패율
def solution(N, stages):
    answer = []
    count = [0]*(N+1)
    
    #특정 스테이지에 머물러 있는 사람의 수 카운팅
    for stage in stages:
        if stage==N+1:
            continue
        count[stage] += 1
        
    length = len(stages)
    for i in range(1, len(count)):
        if length==0: #도달한 유저가 없는 경우 실패율 빵
            fail = 0
        else: #해당 스테이지의 실패율 계산
            fail = count[i]/length
        #리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= count[i]
        
    #실패율을 기준으로 내림차순 정렬
    answer = sorted(answer, key=lambda x: -x[1])
    answer = [x[0] for x in answer]
    
    return answer

'''
#다시 풀어봤을 때 풀이
def solution(N, stages):
    answer = []
    array = [0]*(N+2)
    for stage in stages:
        array[stage] += 1
    result = []
    for i in range(1, N+1):
        if array[i]==0: #ZeroDivisionError 에러가 발생할 수 있기 때문에 array[i]==0인 경우에는 따로 처리
            result.append((i, 0))
        else:
            result.append((i, array[i]/sum(array[i:])))
    result.sort(key = lambda x : (-x[1], x[0]))
    for x in result:
        answer.append(x[0])
    return answer
'''
