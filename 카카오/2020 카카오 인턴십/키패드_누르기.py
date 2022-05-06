def solution(numbers, hand):
    answer = ''
    dict_num = {1:(0,0), 2:(0,1), 3:(0,2),
                4:(1,0), 5:(1,1), 6:(1,2),
                7:(2,0), 8:(2,1), 9:(2,2),
                '*':(3,0), 0:(3,1), '#':(3,2)}
    left = [1, 4, 7]
    right = [3, 6, 9]
    left_now = '*'
    right_now = '#'
    for number in numbers:
        if number in left:
            answer += 'L'
            left_now = number
        elif number in right:
            answer += 'R'
            right_now = number
        else:
            number_pos = dict_num[number]
            left_pos = dict_num[left_now]
            right_pos = dict_num[right_now]
            left_distance = abs(left_pos[0]-number_pos[0]) + abs(left_pos[1]-number_pos[1])
            right_distance = abs(right_pos[0]-number_pos[0]) + abs(right_pos[1]-number_pos[1])
            if left_distance<right_distance:
                answer += 'L'
                left_now = number
            elif left_distance>right_distance:
                answer += 'R'
                right_now = number
            else:
                if hand=="left":
                    answer += 'L'
                    left_now = number
                else:
                    answer += 'R'
                    right_now = number
            
    return answer
