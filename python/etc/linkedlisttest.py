class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

class LinkedList :
    def __init__(self) :
        dummy = Node("dummy")
        self.head = dummy
        self.tail = dummy

        self.current = None
        self.before = None

        self.num_of_data = 0

    def append(self, data) :
        new_node = Node(data)
        self.tail.next = new_node #?
        self.tail = new_node

        self.num_of_data += 1

    def delete(self) :
        pop_data = self.current.data

        if self.current is self.tail :
            self.tail = self.before

        self.before.next = self.current.next
        self.current = self.before

        self.num_of_data -= 1

        return pop_data

    def first(self) :
        if self.num_of_data == 0: # 데이터가 없는 경우 첫번째 노드도 없기 때문에 None 리턴
            return None

        self.before = self.head
        self.current = self.head.next

        return self.current.data

    # next 메소드 (search2 - current 노드의 다음 노드 검색, 이전에 first 메소드가 한번은 실행되어야 함)
    def next(self):
        if self.current.next == None:
            return None

        self.before = self.current
        self.current = self.current.next

        return self.current.data

    def print_all(self) :
        self.list_result = []
        temp = self.head.next
        while temp != None : 
            self.list_result.append(temp.data)
            temp = temp.next
        return self.list_result

    def size(self):
        return self.num_of_data

if __name__ == "__main__" : 
    l_list = LinkedList()
    l_list.append(5)
    l_list.append(2)
    l_list.append(1)
    
    print(l_list.print_all())
    l_list.delete()
    print(l_list.print_all())
