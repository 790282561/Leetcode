# 链表的节点和索引结构是分开的
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Singlelinklist:
    def __init__(self, node=None):
        self.__head = node

    def headadd(self, val):
        node = Node(val)
        node.next = self.__head  # 在开头未改变前，先next指引到该开头。顺序不能乱
        self.__head = node

    def tailadd(self, val):
        node = Node(val)
        cur = self.__head
        if cur is None:
            self.headadd(val)
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def middleadd(self, val, pos):
        node = Node(val)
        base_pos = 1
        if pos <= 0:
            self.headadd(val)
        else:
            cur = self.__head
            while base_pos < pos:
                cur = cur.next
                base_pos += 1
                if cur == None:
                    self.tailadd(val)
                    return
            node.next = cur.next
            cur.next = node

    def walkthrough(self):
        cur = self.__head
        while cur != None:
            print(cur.val, end=" ")
            cur = cur.next


sll = Singlelinklist()
for i in range(10):
    if i % 2 == 1:
        sll.headadd(i)
    else:
        sll.tailadd(i)
sll.middleadd(7, 100)
sll.walkthrough()
