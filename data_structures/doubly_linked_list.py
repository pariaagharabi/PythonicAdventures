class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    # Find index of node in linked list
    def pos(self, key):
        cur_node = self.head
        counter_pos = 0

        while cur_node is not None:
            if cur_node.data == key:
                return counter_pos

            cur_node = cur_node.next
            counter_pos += 1

        return -1

    def length(self):
        cur_node = self.head
        counter = 0

        while cur_node is not None:
            cur_node = cur_node.next
            counter += 1
        return counter

    def append(self, data):
        new_node = Node(data)
        cur = self.head

        if self.head is None:
            self.head = new_node
            return

        while cur.next is not None:
            cur = cur.next
        cur.next = new_node
        new_node.prev = cur

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def add_after_node(self, key, data):
        cur_node = self.head

        while cur_node is not None and cur_node.data != key:
            cur_node = cur_node.next

        if cur_node is None:
            return

        new_node = Node(data)
        cur_node_next = cur_node.next

        cur_node.next = new_node
        new_node.next = cur_node_next
        if cur_node_next is not None:
            cur_node_next.prev = new_node
        new_node.prev = cur_node

    def add_before_node(self, key, data):
        cur_node = self.head

        while cur_node is not None and cur_node.data != key:
            cur_node = cur_node.next

        if cur_node is None:
            return

        new_node = Node(data)
        prev_node = cur_node.prev

        if prev_node is not None:
            prev_node.next = new_node
        new_node.next = cur_node
        cur_node.prev = new_node
        new_node.prev = prev_node

    def reverse(self):
        if(self.head is None or self.head.next is None):
            return

        curr = self.head
        after = curr.next

        while(after.next is not None):
            temp = after.next
            after.next = curr
            curr = after
            after = temp

        after.next = curr
        self.head.next = None
        self.head = after
