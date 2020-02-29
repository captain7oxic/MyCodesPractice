class Node:
    def __init__(self):
        self.data = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None

    def create(self):
        while True:
            newnode = Node()
            newnode.data = int(input("Enter the data of the node: "))

            if self.start == None:
                self.start = newnode
                current = newnode
            else:
                current.next = newnode
                current = newnode

            print("-"*45)
            n = input(
                "Select Y/N if you want to continue -\n Enter your Choice :")
            if n == 'N':
                break

    def Display(self):
        ptr = self.start
        while ptr != None:
            print(ptr.data, end='  --> ')
            ptr = ptr.next
        print()

    def insertion_at_first(self, d):
        newnode = Node()
        newnode.data = d
        newnode.next = self.start
        self.start = newnode

    def insertion_at_last(self, data):
        newnode = Node()
        newnode.data = data
        ptr = self.start
        while ptr != None:
            ptr = ptr.next
        ptr.next = newnode

    def insert_after_data(self, pos_data, data):
        newnode = Node()
        newnode.data = data
        ptr = self.start
        ptr2 = self.start.next
        while ptr.data != pos_data:
            ptr = ptr.next
            ptr2 = ptr2.next
        ptr.next = newnode
        newnode.next = ptr2

    def reverse(self):
        ptr = self.start
        ptr2 = self.start.next
        while ptr2 != None:
            ptr = ptr.next
            ptr2 = ptr2.next
            next = ptr2.next
            ptr2 = ptr
            ptr = next
        self.start = ptr


if __name__ == '__main__':
    l = LinkedList()
    l.create()
    l.Display()
    l.insertion_at_first(15)
    l.Display()
    l.insert_after_data(4, 10)
    l.Display()
    l.reverse()
    l.Display()
