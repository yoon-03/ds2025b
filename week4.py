class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link


class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.link:
            current = current.link
        current.link = Node(data)


    def remove(self, target):
        if self.head.data == target:
            self.head = self.head.link
            return
        current = self.head
        previous = None
        while current:
            if current.data == target:
                previous.link = current.link
                current.link = None
            previous = current
            current = current.link


    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return f"{target}을(를) 찾았습니다"
            else:
                current = current.link
        return f"{target}은(는) 링크드리스트 안에 존재하지 않습니다"


    def __str__(self):
        node = self.head
        out_texts = ""
        while node is not None:
            out_texts = out_texts + f"{node.data} -> "
            node = node.link
        return out_texts + "end"


ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)
print(ll)
print(ll.search(100))
print(ll.search(-9))
ll.remove(90)
ll.remove(-9)
print(ll)