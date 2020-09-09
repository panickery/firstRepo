import time

def split(txt) :
    # print("txt :: {}".format(txt))
    num_par = 0
    is_right = 0
    for i in txt :
        num_par +=1
        if i == '(' :
            is_right +=1
        else :
            is_right -=1

        if is_right == 0 :
            # print(txt[0:num_par], txt[num_par:len(txt)])
            return txt[0:num_par], txt[num_par:len(txt)]

def checkRight(text) :
    check = 0
    for i in text :
        if i == '(' :
            check +=1
        else :
            check -=1

        if check < 0 : 
            return False
    return True

def recur(text) :
    if len(text) == 0 :
        return ''

    u, v = split(text)

    if checkRight(u) : 
        return u + recur(v)
    else :
        result = '(' + recur(v) + ')'
        temp = u[1:len(u)-1]
        # 괄호를 제거한 u를 뒤집는게 아니라 괄호 방향을 바꿔야한다.
        # temp = temp[::-1]
        temp=list(temp)
        
        for i in range(len(temp)) :
            if temp[i] == '(' :
                temp[i] = ')'
            else :
                temp[i] = '('
        temp = ''.join(temp)
        return result+temp

def solution(text):
    result = recur(text)
    return result

a = [
    "(()())()",
    ")(",
    "()))((()",
    "()",
    "()()()()",
    ")()()()("
    ")))(())()))(()(((())(()()))()(((()()()(()()()()())()())()())())))(()())()())(((()())()()()))((())())))()))())(()())(())))))))(((()(()()(((()()(()()(((((()(()()))()))(((()())))(((()(())((((((()))()))(("
]

for x in a:
    print(solution(x))

# print(solution(a[0]))
# print(solution(a[1]))
# print(solution(a[2]))

# print(checkRight(''))