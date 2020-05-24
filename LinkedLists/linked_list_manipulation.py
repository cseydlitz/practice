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

    def find_k_to_last(self, k):
        """ Prompt: Implement an algorithm to find the kth to last element of a singly linked list

            Parameters:
                k: integer
        """
        count = 1
        active_node = self.head
        target_node = self.head
        while active_node.next_node is not None:
            active_node = active_node.next_node
            if count < k:
                count +=1
            else:
                target_node = target_node.next_node

        return target_node.data

    def dedup_ll(self):
        """ Prompt: Write code to remove duplicates form an unsorded linked list

            Secondary requirement: How would you solve this problem if a temporary 
            buffer is not allowed?
        """
        active_node = self.head
        while active_node:
            prev_node = active_node
            cur_node = active_node.next_node
            while cur_node:
                if active_node.data == cur_node.data:
                    prev_node.next_node = cur_node.next_node
                else: 
                    prev_node = cur_node
                cur_node = cur_node.next_node

            active_node = active_node.next_node

    def delete_middle_node(self, node):
        """ Prompt: Write a function to delete specific node from list

            Parameters:
                node: int
            Restrictions:
                Cannot delete first or last item in list
        """

        if node == self.head.data:
            return False

        prev_node = self.head
        active_node = prev_node.next_node

        while active_node:
            if prev_node.next_node is None and prev_node.data == node:
                return False
            if active_node.data == node:
                prev_node.next_node = active_node.next_node
            else:
                prev_node = prev_node.next_node

            active_node = prev_node.next_node

def manipulate_ll(vals, k=None, n=None, dedupe=False):
    """ Function to execute desired manipulation. 
    
        Parameters: 
             vals: list of integers
            Optional:
                 k: integer
                     If a value of k is provided, it will find the kth to the last value of the list
                 dedupe: boolean
                     If dedupe=True, it will remove duplicates
                 n: integer
                     If a value of n is provided, it will delete that node from the list as long as it
                     is not the first or last node in the list
    """
    LL = LinkedList()
    for val in vals:
        LL.insert_into_ll(val)
    
    print("Linked List for reference:")
    LL.print_ll()

    if dedupe:
        LL.dedup_ll()
        print("Deduped:")
        LL.print_ll()

    if k:
        val = LL.find_k_to_last(k)
        print(f"{k}-to-last value of list: {val}")

    if n:
        if LL.delete_middle_node(n): 
            print(f"Removed {n} from the list:")
            LL.print_ll() 
        else:
            print(f"Can't remove first of last item from the list (you tried to return {n})")
