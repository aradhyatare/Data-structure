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

    def insertAtEnd(self, new_data):

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while(temp.next):
            temp = temp.next
        
        temp.next = new_node
        # new_node.next = None

        # self.head = new_node

if __name__ == '__main__':

    Llist = LinkedList()

    Llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    Llist.head.next = second
    second.next = third 

    Llist.insertAtEnd(4)

    Llist.printList()