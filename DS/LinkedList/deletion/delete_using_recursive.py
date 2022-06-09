from ast import Delete


class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end = " ")
            temp = temp.next

    def push(self, new_data):

        new_node = Node(new_data)

        new_node.next = self.head

        self.head = new_node

    def deleteNode(start, key):

        if (key < 1):
            return start 
        
        if (start == None):
            return None
        
        if (key == 1):

            temp = start.next
            return temp

        start.next = LinkedList.deleteNode(start.next, key - 1)
        return start

if __name__ == '__main__':

    head = None
    Llist = LinkedList()
    Llist.push(3)
    Llist.push(5)
    Llist.push(10)
    Llist.push(11)
    print("The linked list is..")
    Llist.printList()
    Llist.deleteNode(head, 5)
    print("The linked list is..")
    Llist.printList()