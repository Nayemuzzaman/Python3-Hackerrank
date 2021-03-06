#create Node
class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None
    #travesal part
    def print_LL(self):
        if self.head is None:
            print("Linked list empty")
        #when inside have value
        else:
            n = self.head
            #loop continue until null
            while n is not None:
                print(n.data,"-->",end=" ")
                n = n.ref
    #add value in node at the beginning
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    #Add after the value in given node
    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x==n.data:
                break
            n = n.ref
        if n is None:
            print("Node is not present in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

LL1 = LinkedList()

LL1.add_begin(30)
LL1.add_begin(60)
LL1.add_begin(90)
LL1.add_after(600, 90)
LL1.print_LL()
