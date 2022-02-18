#괄호 변환
def check(p): #올바른 괄호 문자열인지 판단하는 함수
    count = 0
    for x in p:
        if x=='(':
            count += 1
        else:
            if count==0:
                return False
            count -= 1
    return True
    
def change(p): #괄호 뒤집는 함수
    q = ''
    for i in range(len(p)):
        if p[i]=='(':
            q += ')'
        else:
            q += '('
    return q

def solution(p):
    answer = ''
    if p=='':
        return ''
    count1 = 0
    count2 = 0
    for i in range(len(p)): #균형잡힌 문자열 index 찾기
        if p[i]=='(':
            count1 += 1
        else:
            count2 += 1
        if count1==count2:
            break
    if check(p[:count1*2]):
        answer = p[:count1*2] + solution(p[count1*2:])
    else:
        answer = '(' + solution(p[count1*2:]) + ')' + change(p[1:count1*2-1])
    return answer
