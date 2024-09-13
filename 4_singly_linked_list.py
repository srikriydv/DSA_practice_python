class Node:
    def __init__(self, item=None , next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self, data):
        n = Node(data, self.start)
        self.start = n

    def insert_at_last(self, data):
        n = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    def insert_after(self, target_data, data):
        temp = self.search(target_data)
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n
        return None
    # def delete_all(self):
    #     while self is not None:

    
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
        print()


# Driver Code
myList2 = SLL()
myList2.insert_at_start(50)
myList2.insert_at_last(60)
myList2.print_list()