class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def length(self):
        counter_len = 0
        cur_node = self.head

        while cur_node is not None:
            counter_len += 1
            cur_node = cur_node.next

        return counter_len

    def append(self, data):
        new_node = Node(data)
        # If  linked list is empty:
        if self.head is None:
            self.head = new_node
            return
        # If linked list in not empty
        last_node = self.head
        while last_node.next != None:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def find(self, data):
        cur_node = self.head
        while cur_node != None and cur_node.data != data:
            cur_node = cur_node.next

        return cur_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist.")
            return
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def swap(self, data1, data2):
        prev1, node1 = self.find_with_prev(data1)
        prev2, node2 = self.find_with_prev(data2)

        prev1.next, prev2.next = prev2.next, prev1.next
        node1.next, node2.next = node2.next, node1.next

        return

    def reverse_linked_list(self):
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

    def del_node(self, data):
        # Linked list is empty
        if self.head is None:
            return

        cur_node = self.head
        prev_node = None

        # Finding the node and prev_node that want to delete
        while cur_node is not None and cur_node.data != data:
            prev_node = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        # If the node is first one(head)
        if prev_node is None:
            self.head = cur_node.next
            cur_node = None
            return

        # The node is middel or last
        prev_node.next = cur_node.next
        cur_node = None

    # Delete node base on position (if position is in 0 or not in 0)
    def del_pos(self, pos):
        if self.head is None:
            return

        prev_node = None
        cur_node = self.head
        counter = 0

        while cur_node is not None and counter < pos:
            counter += 1
            prev_node = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        if prev_node is None:
            self.head = cur_node.next
            cur_node = None
            return

        prev_node.next = cur_node.next
        cur_node = None

    def find_with_prev(self, data):
        if self.head is None:
            return (None, None)

        prev = None
        cur = self.head

        while cur.data != data and cur is not None:
            prev = cur
            cur = cur.next

        if cur is None:
            return (None, None)

        return (prev, cur)
