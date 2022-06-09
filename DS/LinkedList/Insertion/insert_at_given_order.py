class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next

    def insertAfter(self, prev_node, new_data):

        prev_node = self.find(prev_node)
        print(f"The value of previous node is {prev_node}")
        if prev_node is None:
            print("The given previous node must be in LinkedList")
            return
        
        new_node = Node(new_data)

        new_node.next = prev_node.next

        prev_node.next = new_node

if __name__ == '__main__':

    Llist = LinkedList()

    Llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    Llist.head.next = second
    second.next = third 

    Llist.insertAfter(2,5)

    Llist.printList()