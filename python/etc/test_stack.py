# 데이터를 하나 가지고 다음 주소를 가지는 연결리스트를 만들기 위한 Node 클래스 생성
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack 자료 구조를 이용하기 위해 Node를 가지는 Stack 구조를 만드는 클래스.
class Stack:
    def __init__(self):
        self.head = None

# Stack이 비었는지 아닌지를 판단하는 메소드
    def is_empty(self):
        if not self.head:
            return True
        return False

# Stack에 Node데이터를 하나 넣는 메소드
    def push(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

# Stack에서 Node데이터를 하나 가져오는 메소드
    def pop(self):
        if self.is_empty():
            return None

        pop_data = self.head.data
        self.head = self.head.next
        return pop_data

# Stack에서 가장 최근에 쌓인 데이터를 조회하는 메소드
    def peek(self):
        if self.is_empty():
            return None

        return self.head.data

# Stack에 쌓인 데이터를 처음부터 리스트 형태로 조회하는 메소드
    def peek_all(self) :
        list_tmp = []
        if self.is_empty() :
            return None

        temp = self.head
        while temp : 
            list_tmp.append(temp.data)
            temp = temp.next

        return list_tmp

# 입력한 식에서 숫자. 기호 등을 나눌때 사용하는 함수
def separator(sent) :
    # 공백으로 1차 나누고(공백으로 구분 되어 있지 않더라고 추후 단계에서 구분됨)
    sent = ''.join(sent.split())
    # +-*/()로 나누기 위해 변수에 집어넣음.
    sep_char = '+-*/()'
    tmp = ''
    tmp_arr = []

    # 숫자와 연산자(+-*/())를 나누어 배열에 저장합니다.
    for char in sent :
        if char not in sep_char :
            tmp += char
        else :
            if tmp != '' :
                tmp_arr.append(tmp)
            tmp = ''
            tmp_arr.append(char)

    if tmp != '' :
        tmp_arr.append(tmp)
    
    # 배열을 반환합니다.
    return tmp_arr

if __name__ == "__main__":
    # 스택을 두개 생성
    s = Stack()
    s2 = Stack()

    prior = {}
    # 연산자마다 우선순위가 또 다르기때문에 이런식으로 우선순위를 지정해줍니다.
    prior["*"], prior["/"], prior["+"], prior["-"], prior["("] = 2, 2, 1, 1, 0

    suf_arr = []
    arr_formula = []

    # 키보드의 입력을 inf_formula 변수에 입력받는다.
    inp_formula = input()
    # 입력 받은 데이터를 숫자와 문자로 나누기 위해 separator 메소드에 전달합니다.
    arr_formula = separator(inp_formula)
    # print('tokenized formula :: {}'.format(arr_formula))

    # 전체 나눠진 arr_formula에서 for 문 진행
    for char in arr_formula :
        # 나누어진 숫자와 연산자 배열에서 +-/* 일 경우 
        if char == '+' or char == '-' or char == '/' or char == '*' : 
            # stack이 비어있지 않고 스택에 남아있는 연산자의 우선순위가 클떄 :: ex ::  +( -( *( /( *+ *- /+ /-
            while (not s.is_empty()) and (prior[s.peek()] >= prior[char]) :
                suf_arr.append(s.pop())
            s.push(char)
        elif char =='(' :
            s.push(char)
        elif char == ')' :
            temp = s.pop()
            while temp != '(' and not s.is_empty() : 
                suf_arr.append(temp)
                temp = s.pop()
        else :
            suf_arr.append(char)

    # 위 과정이 다 지나고도 스택에 남아 있는 데이터는 POP한다.
    while not s.is_empty() :
        suf_arr.append(s.pop())

    # suf_arr에 들어 있는 데이터를 공백으로 연결 (ex :: 78.2 33.3 * 23 124.5 46 - * +)
    final_sentence = ' '.join(suf_arr)
    final_arr = suf_arr
    print('Postfix Formula :: {}'.format(final_sentence))

    # 실제 후위연산식으로 변환된 데이터를 계산하는 부분
    # S1에 저장되어 있는 부분을 S2로 Push Pop 하며 계산.
    for token in suf_arr :
        if token in '+-/*' :
            num1 = s2.pop()
            num2 = s2.pop()
            if token == '+' : s2.push(num2 + num1)
            elif token == '-' : s2.push(num2 - num1)
            elif token == '*' : s2.push(num2 * num1)
            elif token == '/' : s2.push(num2 / num1)

        else :
            s2.push(float(token))
    
    # 결국 계산된 데이터 출력하는 부분
    print('Final Result    :: {}'.format(s2.pop()))

# 34.5 * 23.4 + 23 * (32 + 46) = 2601.3
# 34*23.4 + 37/(32-46) = 792.957142857
# 78.2*33.3 + 23*(124.5 - 46) = 4409.559999
# 75.3/23.4 + 25.6/(44+46) = 3.5023931623931626
# 72.5/34.5 + 23*(32 - 78) = -1055.8985507246377

# 807.3 + 1794
# 795.6 + -2.642857142857143
# 2604.06 + 1805.5
# 3.217948717948718 + 0.2844444
# 2.101449275362319 -1058


