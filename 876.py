class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        # 测试基本功能，输出字符串
        return str(self.data)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

# def printList(node):
#     while node:
#         print(node)
#         node = node.next

def reverseList( head):
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev



print(reverseList(node1))