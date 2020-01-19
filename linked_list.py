class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'LinkedList [\n' +str(current.value) +'\n'
            while current.next != None:
                current = current.next
                out += str(current.value) + '\n'
            return out + ']'
        return 'LinkedList []'

    def clear(self):
        self.__init__()

    def add(self, x):
        """
        Добавление элемента в конец списка
        """
        self.length += 1
        if self.first == None:
            # self.first и self.last будут указывать на одну область памяти
            self.last = self.first = Node(x, None)
        else:
            # здесь, уже на разные, т.к. произошло присваивание
            self.last.next = self.last = Node(x, None)

    def push(self, x):
        """
        Добавление элемента в начало списка
        """
        self.length += 1
        if self.first == None:
            self.last = self.first = Node(x, None)
        else:
            self.first = Node(x, self.first)

    def insertNth(self, i, x):
        """
        Вставка элемента в позицию i
        """
        if self.first == None:
            self.last = self.first = Node(x, None)
            return
        if i == 0:
            self.first = Node(x, self.first)
            return
        curr = self.first
        count = 0
        while curr != None:
            count += 1
            if count == i:
                curr.next = Node(x, curr.next)
                if curr.next.next == None:
                    self.last = curr.next
                break
            curr = curr.next

    def len(self):
        """
        Длина списка
        """
        length = 0
        if self.first != None:
            current = self.first
            while current.next != None:
                current = current.next
                length += 1
        return length + 1  # +1 для учета self.first

    def del_elem(self, i):
        """
        Удаление элемента в позиции i
        """
        if (self.first == None):
            return
        curr = self.first
        count = 0
        if i == 0:
            self.first = self.first.next
            return
        while curr != None:
            if count == i:
                if curr.next == None:
                    self.last = curr
                old.next = curr.next
                break
            old = curr
            curr = curr.next
            count += 1

    def sorted_insert(self, x):
        """
        Вставка элемента в отсортированный список
        """
        if self.first == None:
            self.first = Node(x, self.last)
            return
        if self.first.value > x:
            self.first = Node(x, self.first)
            return
        curr = self.first
        while curr != None:
            if curr.value > x:
                old.next = Node(x, curr)
                return
            old = curr
            curr = curr.next
        self.last = old.next = Node(x, None)

    def RemoveDuplicates(self):
        """
        Удаление повторяющихся значений
        """
        if (self.first == None):
            return
        old = curr = self.first
        while curr != None:
            if curr.next != None:
                if old.value == curr.next.value:
                    curr.next = curr.next.next
            else:
                old = curr = old.next
            curr = curr.next


    




if __name__ == "__main__":

    linked_list = LinkedList()
    linked_list.add(56)
    linked_list.add(42)
    x = linked_list.__str__()
    print(x)

