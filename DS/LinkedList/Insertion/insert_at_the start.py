# How to insert node at the start of a linked List.

# Node Class
class Node:

    # Function to initialise node object
    def __init__(self, data):
        self.data = data  #to assign data
        self.next = None #head of the default list is null

# Linked List class
class LinkedList:

     # Function to initialise node object
    def __init__(self):
        self.head = None

    # To print the linked List: As head contains teh address of the next node, assign it to a variable.
    # Loop over it till head does not return false.
    # Now the varaible contains data and the address of the next node.
    # Use varaiable_name.data to access the data. 
    # After accessing the data, change the value of the variable using varaible_name = variable_name.next 
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    # To add a new node at the beginning 
    # Step 1: define a object of class Node.
    # Step 2: After new object creation, use .next to move the head of the existing linked list to the start (new_node)
    # Step 3: Now update the head of the list to the newly object that we've created. 
    def push(self, new_data):

        new_node = Node(new_data)

        new_node.next = self.head

        self.head = new_node

if __name__ == '__main__':

    Llist = LinkedList()

    Llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    Llist.head.next = second
    second.next = third 

    Llist.push(4)

    Llist.printList()