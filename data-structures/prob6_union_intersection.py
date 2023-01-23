class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        
    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size

    def get_as_set(self):
        out_set = set()
        node = self.head
        while node:
            out_set.add(node.value)
            node = node.next
        return out_set

    def get_as_list(self):
        out_list = []
        node = self.head
        while node:
            out_list.append(node.value)
            node = node.next
        return out_list

def llist_from_list(lst: list) -> LinkedList:
    llist = LinkedList()
    for i in lst:
        llist.append(i)

    return llist
        

def set_to_linkedlist(in_set: set) -> LinkedList:
    out = LinkedList()

    for val in in_set:
        out.append(val)

    return out


def union(llist_1, llist_2):
    return set_to_linkedlist(llist_1.get_as_set() | llist_2.get_as_set())

def intersection(llist_1, llist_2):
    return set_to_linkedlist(llist_1.get_as_set() & llist_2.get_as_set())


