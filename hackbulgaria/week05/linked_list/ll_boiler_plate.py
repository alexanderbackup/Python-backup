class Node(object):

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.list_size = 0

    def add_element(self, data):
        new = Node(data)
        if self.head == None:
            self.head = new
        else:
            cur = self.head.next                
            prev = self.head
            while cur != None:
                prev.next = cur
                cur.prev = prev
                prev = cur
                cur = cur.next
                #
            cur = new
            prev.next = cur
            cur.prev = prev
        self.list_size += 1
        return new

    def set_element(self, index, data):
        if index >= self.list_size:
            raise IndexError
        el_for_setting = self.index(index)
        el_for_setting.data = data

    def index(self, index):
        current = self.head
        if index >= self.list_size:
            raise IndexError
        while index:
            current = current.next
            index -= 1
        return current # current.data

    def size(self):
        return self.list_size

    def remove(self, index):
        if index >= self.list_size:
            raise IndexError
        el_for_remove = self.index(index)
        if el_for_remove == self.head:
            if self.list_size == 1:
                self.head = None
                self.list_size -= 1
                return el_for_remove
            self.head = self.head.next
            self.head.prev = None
            self.list_size -= 1
            return el_for_remove
        cur = self.head.next
        prev = self.head
        while cur != None:
            if cur == el_for_remove:
                prev.next = cur.next
                self.list_size -= 1
                if prev.next:
                    prev.next.prev = prev # if there is element after
                return el_for_remove      # the one we removed we
            prev = cur                    # we change its prev pointer
            cur = cur.next
            prev.next = cur
            cur.prev = prev

    def pprint(self):
        result = '['
        if self.list_size == 1:
            return result + self.check_if_string(self.head.data) + ']'
        elif self.list_size == 0:
            return '[]'
        comma_check = self.list_size
        for i in range(self.list_size):
            result += self.check_if_string(self.index(i).data)
            if comma_check > 1:
                result += ', '
            comma_check -= 1
        return result + ']'

    def check_if_string(self, item):
        if isinstance(item, str):
            return '"' + item + '"'
        elif callable(item):
            return item.__name__
        return str(item)


    def to_list(self):
        pass

    def add_at_index(self, index, data):
        if index >= self.list_size:
            raise IndexError
        el_for_adding = self.index(index)
        if index == 0:
            return self.add_first(data)
        new = Node(data)
        cur = el_for_adding
        prev = cur.prev
        cur.prev = new
        prev.next = new
        new.prev = prev
        new.next = cur
        self.list_size += 1

    def add_first(self, data):
        new = Node(data)
        cur = self.head
        self.head = new
        self.head.next = cur
        cur.prev = self.head
        self.list_size += 1

    def add_list(self, list: list):
        pass

    def add_linked_list(self, Linkedlist: "LinkedList"):
        pass

    def ll_from_to(self, start_index, end_index):
        pass

    def pop(self):
        pass

    def reduce_to_unique(self):
        pass

foo = LinkedList()
foo.add_element(0)
foo.add_element(1)
foo.add_element(2)
foo.add_element(3)






