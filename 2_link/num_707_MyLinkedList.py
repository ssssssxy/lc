class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = None


    def get(self, index: int) -> int:
        i = 0
        if not self.head:
            return -1
        cur = self.head
        while cur:
            if i == index:
                return cur.val
            else:
                cur = cur.next
                i += 1
        return -1


    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        return self.head

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        cur = pre = self.head
        if not self.head:
            self.head = node
            return self.head
        while cur.next:
            cur = cur.next
        cur.next = node
        return self.head

    def addAtIndex(self, index: int, val: int) -> None:
        node = Node(val)
        cur = self.head
        if index <= 0:
            self.addAtHead(val)
        else:
            i = 0
            # for i in range(1, index):
            #     cur = cur.next
            # node.next = cur.next
            # cur.next = node
            while cur:
                if i == index - 1:
                    node.next = cur.next
                    cur.next = node
                    return self.head
                else:
                    cur = cur.next
                    i+=1
            if i < index:
                return -1
        return self.head

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return False
        cur = pre = self.head
        i = 0
        if index == 0:
            self.head = self.head.next
            return self.head
        while cur:
            if i == index:
                pre.next = cur.next
                cur = pre.next
                return True
            else:
                pre = cur
                cur = cur.next
                i += 1
        return False




# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
for i in range(1, 5):
    obj.addAtTail(i)
print(obj)
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)