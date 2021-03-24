#check all functions part by part
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
    #add value in node at the End
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
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
    #When linked list empty Empty linklist
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty")

    #begin item delete
    def delete_begin(self):
        if self.head is None:
            print("LL is empty so we cant delete nodes beta!")
        else:
            self.head = self.head.ref
    #Last node delete
    def delete_end(self):
        if self.head is None:
            print("Linked List is empty, so i can't delete beta!")
        elif self.head.ref is None:
            self.head = None

        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None
    def delete_by_value(self, x):
        if self.head is None:
            print("can't delete the Linked list is empty")
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not present!")
        else:
            n.ref = n.ref.ref
LL1 = LinkedList()
LL1.add_begin(1)
LL1.insert_empty(10)
LL1.insert_empty(190) #singly linkedlist when its not empty
LL1.add_end(30)
LL1.add_end(60)
LL1.add_end(90)
LL1.add_after(600, 90)
LL1.add_before(77, 30)
LL1.delete_begin()
LL1.delete_end()
LL1.delete_by_value(90)
LL1.print_LL()
