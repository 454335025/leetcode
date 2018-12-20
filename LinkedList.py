class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList():
    def __index__(self):
        self._head = None

    def isEmpty(self):
        return self._head == None

    def size(self):
        current = self._head
        count = 0
        while current != Node:
            count += 1
            current = current.next
        return count

    def travel(self):
        current = self._head
        while current != None:
            print(current.val)
            current = current.next

    def add(self, val):
        temp = Node(val)
        temp.next = self._head
        self._head = temp

    def append(self, val):
        temp = Node(val)
        if self.isEmpty():
            self._head = temp
        else:
            current = self._head

            while current.next != None:
                current = current.next
            current.next = temp

    def search(self, val):
        current = self._head
        while current.next != None:
            if current.val == val:
                return True
            else:
                current = current.next
        return False


