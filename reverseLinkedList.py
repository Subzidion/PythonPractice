class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def __str__(self):
        s = ''
        if self.head is None:
            return s
        currentNode = self.head
        while currentNode.nextNode is not None:
            s += str(currentNode) + ' -> '
            currentNode = currentNode.nextNode
        s += str(currentNode)
        return s

    def reverse(self):
        prevNode = None
        currentNode = self.head
        while currentNode is not None:
            nextNode = currentNode.nextNode
            currentNode.nextNode = prevNode
            prevNode = currentNode
            currentNode = nextNode
        self.head = prevNode

class Node:
    def __init__(self, data=0, nextNode=None):
        self.nextNode = nextNode
        self.data = data

    def __str__(self):
        return str(self.data)

n1 = Node()

n2 = Node(5, n1)

n3 = Node(6, n2)

n4 = Node(7, n3)

n5 = Node(15, n4)

n6 = Node(17, n5)


l1 = LinkedList(n6)

print(l1)

l1.reverse()

print(l1)
