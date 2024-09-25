class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next


class cdsll:
    def __init__(self):
        self.start = None

    def insert_at_first(self, data):
        n = Node(item=data)
        if self.start is None:
            n.next = n
            n.prev = n
            self.start = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n
            self.start = n

    def insert_at_last(self, data):
        n = Node(item=data)
        if self.start is None:
            n.next = n
            n.prev = n
            self.start = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n

    def insert_after(self, tempd, data):
        n = Node(item=data)
        if self.start is None:
            return
        else:
            temp = self.start
            while temp != self.start.prev:
                if temp.item == tempd:
                    n.next = temp.next
                    n.prev = temp
                    temp.next.prev = n
                    temp.next = n
                    break
                temp = temp.next
            if tempd == self.start.prev.item and temp == self.start.prev:
                self.insert_at_last(data)

    def delete_first(self):
        if self.start is None:
            return
        if self.start.next == self.start:
            self.start = None
        else:
            self.start.prev.next = self.start.next
            self.start.next.prev = self.start.prev
            self.start = self.start.next

    def delete_last(self):
        if self.start is None:
            return
        if self.start.next == self.start:
            self.start = None
        else:
            self.start.prev.prev.next = self.start
            self.start.prev = self.start.prev.prev

    def delete_item(self, data):
        if self.start is None:
            return

        if self.start.next == self.start and self.start.item == data:
            self.start = None
            return

        if self.start.item == data:
            self.start.prev.next = self.start.next
            self.start.next.prev = self.start.prev
            self.start = self.start.next
            return

        temp = self.start
        while temp != self.start.prev:
            if temp.item == data:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                return
            temp = temp.next

        if temp.item == data and temp == self.start.prev:
            self.delete_last()

    def print_list(self):
        if self.start is None:
            print("laalhai sara thela laal hai")
        else:
            temp = self.start
            while True:
                print(temp.item, end="<>")
                if temp.next == self.start:
                    break
                temp = temp.next
            print()  # Move to a new line after the list is printed

    def __iter__(self):
        return xll(self.start)


class xll:
    def __init__(self, start):
        self.current = start
        self.start = start
        self.is_ok = True  # Used to check if the first node was visited

    def __iter__(self):
        return self

    def __next__(self):
        if self.start is None:
            raise StopIteration

        if not self.is_ok and self.current == self.start:
            raise StopIteration

        data = self.current.item
        self.current = self.current.next
        self.is_ok = False
        return data
q = cdsll()
q.insert_at_first(10)
q.insert_at_first(20)
q.insert_at_first(30)

q.delete_item(20)  # Delete a middle node
q.print_list()  # Outputs: 30<>10<>

q.delete_item(30)  # Delete the start node
q.print_list()  # Outputs: 10<>

q.delete_item(10)  # Delete the last remaining node
q.print_list()  # Outputs: laalhai sara thela laal hai
