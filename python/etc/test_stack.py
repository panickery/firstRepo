class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if not self.head:
            return True
        return False

    def push(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None

        pop_data = self.head.data
        self.head = self.head.next
        return pop_data

    def peek(self):
        if self.is_empty():
            return None

        return self.head.data

    def peek_all(self) :
        list_tmp = []
        if self.is_empty() :
            return None

        temp = self.head
        while temp : 
            list_tmp.append(temp.data)
            temp = temp.next

        return list_tmp

def separator(sent) :
    sent = ''.join(sent.split())
    sep_char = '+-*/()'
    tmp = ''
    tmp_arr = []

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
    
    return tmp_arr

if __name__ == "__main__":
    s = Stack()
    s2 = Stack()

    prior = {}
    prior["*"], prior["/"], prior["+"], prior["-"], prior["("] = 2, 2, 1, 1, 0

    suf_arr = []
    arr_formula = []

    inp_formula = input()
    arr_formula = separator(inp_formula)
    # print('tokenized formula :: {}'.format(arr_formula))

    for char in arr_formula :
        if char == '+' or char == '-' or char == '/' or char == '*' : 
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

    while not s.is_empty() :
        suf_arr.append(s.pop())

    final_sentence = ' '.join(suf_arr)
    final_arr = suf_arr
    print('Postfix Formula :: {}'.format(final_sentence))

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


