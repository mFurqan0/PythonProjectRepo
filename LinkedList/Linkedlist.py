# A simple Python program to introduce a linked list

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialize next as null

class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

if __name__=='__main__':

    # Start with the empty list
    list = LinkedList()

    list.head = Node(1)
    second = Node(2)
    third = Node(3)

    list.head.next = second; # Link first node with second

    second.next = third; # Link second node with the third node
