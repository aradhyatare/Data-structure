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

    def push(self, new_data):

        new_node = Node(new_data)

        new_node.next = self.head

        self.head = new_node

    def deleteNode(self, key):

        temp = self.head

        # If head iteself contains the key to be deleted. 
        if (temp.data == key):
            self.head = temp.next
            temp = None
            return

        #If head does not contains the key , then we need to use loop to find out where the key is located

        while(temp is not None):
            if temp.data == key:
                break
            prev = temp 
            temp = temp.next

        if (temp == None):
            return

        prev.next = temp.next
        temp = None



if __name__ == '__main__':

    Llist = LinkedList()

    Llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    Llist.head.next = second
    second.next = third 

    Llist.push(4)
    Llist.push(5)

    print("BEfore deleting")
    Llist.printList()

    Llist.deleteNode(2)
    
    print("AFter deleting")
    Llist.printList()