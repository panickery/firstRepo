import re

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

        ret_data = self.head.data
        self.head = self.head.next
        return ret_data

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
    re.sub(,"" ,sent)



if __name__ == "__main__":
    s = Stack()

    suf_arr = []

    inp_formula = input()
    arr_formula = []
    inp_formula = ''.join(inp_formula.split())
    arr_formula = separator(inp_formula)
    print(arr_formula)

    # for char in inp_formula :
    #     if char == '+' or char == '-' or char == '/' or char == '*' : 
    #         s.push(char)
    #     elif char =='(' :
    #         s.push(char)
    #     elif char == ')' :
    #         temp = s.pop()
    #         while temp != '(' and not s.is_empty() : 
    #             suf_arr.append(temp)
    #             temp = s.pop()
    #     else :
    #         if len(suf_arr) == 0 :
    #             suf_arr.append(char)
    #         elif str(suf_arr[-1]) not in '+-/*' : 
    #             suf_arr.append(int(suf_arr[-1]) * 10 + int(char))
    #         else :
    #             suf_arr.append(char)

    # while not s.is_empty() :
    #     suf_arr.append(s.pop())

    # print(suf_arr)
    # print(s.peek_all())




