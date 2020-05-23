class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_into_ll(self, data):
        new_node = Node(data)
        if self.head:
            active_node = self.head
            while active_node.next_node:
                active_node = active_node.next_node
            active_node.next_node = new_node
        else: 
            self.head = new_node

    def print_ll(self):
        active_node = self.head
        while active_node:
            print(active_node.data)
            active_node = active_node.next_node

    def dedup_ll(self):
        """ Prompt: Write code to remove duplicates form an unsorded linked list

            Secondary requirement: How would you solve this problem if a temporary 
            buffer is not allowed?
        """
        active_node = self.head
        while active_node.next_node:
            next_val = active_node.next_node
            while next_val:
                if active_node.data == next_val.data:
                    skip_node = next_val.next_node
                    active_node.next_node = skip_node
                    next_val = skip_node
                else: 
                    next_val = next_val.next_node
            active_node = active_node.next_node

def create_and_dedupe_ll(vals):
    LL = LinkedList()
    for val in vals:
        LL.insert_into_ll(val)
    LL.print_ll()
    LL.dedup_ll()
    print("Deduped:")
    LL.print_ll()

