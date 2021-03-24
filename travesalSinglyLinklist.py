# create Node
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    # travesal part
    def print_LL(self):
        if self.head is None:
            print("Linked list empty")
        # when inside have value
        else:
            n = self.head
            # loop continue until null
            while n is not None:
                print(n.data)
                n = n.ref


LL1 = LinkedList()
# print empty value because not input here
LL1.print_LL()
