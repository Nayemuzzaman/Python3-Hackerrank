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

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    #Add Before the value in given node
    def add_before(self,data,x):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
                n = n.ref
        if n.ref is None:
            print("Node is not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

LL1 = LinkedList()

LL1.add_end(30)
LL1.add_end(60)
LL1.add_end(90)
LL1.add_before(77, 30)
LL1.print_LL()
