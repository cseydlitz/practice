class Node: 
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

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
            new_node.prev_node = active_node
        else:
            self.head = new_node
            
    def print_ll(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next_node

    def partition(self, p):
        """ Prompt: Write code to partition a linked list around a value p
        
            Parameters: 
                p: integer
                    Partition value 
            Requirements:
                All nodes less than partition value p come before all nodes greater
                than or equal to partition value p
        """
        cur_node = self.head
        end_node = self.head

        while end_node.next_node:
            end_node = end_node.next_node
        
        end_ref = end_node
        while end_node.prev_node:  
            while end_node.data < p:
                active_node = end_node
                next_node = end_node.next_node
                prev_node = end_node.prev_node
                if end_node.next_node:
                    next_node.prev_node = prev_node
                if end_node.prev_node:
                    prev_node.next_node = next_node
                active_node.next_node = cur_node.next_node
                cur_node.next_node = active_node
                end_node = prev_node
            end_node = end_node.prev_node

        while end_node.next_node:
            end_node = end_node.next_node

        active_node = self.head
        if not active_node.data < p:
            next_node = active_node.next_node
            next_node.prev_node = None
            active_node.next_node = None
            end_node.next_node = active_node
            active_node.prev_ref = end_node
            self.head = next_node
        
    def palindrome(self):
        """Prompt: Implement a function to check if a linked list is a palindrome

           Returns boolean
        """
        front_node = self.head
        end_node = self.head
        while end_node.next_node:
            end_node = end_node.next_node

        while not end_node == front_node:
            if end_node.data == front_node.data:
                if end_node.prev_node == front_node.next_node:
                    return True
                end_node = end_node.prev_node
                front_node = front_node.next_node
            else:
                return False

def manipulate_ll(vals, p=None, pal=False):
    """ Function to manipulate linked list

        Parameters:
            vals: list of integers
                build linked list out of these integers
            p: Integer
                if a p value is passed, it will run the partition function
            pal: Boolean
                If pal, test if Linked list is a palindrome
    """
    LL = LinkedList()
    for val in vals:
        LL.insert_into_ll(val)

    print("Linked List for reference:")
    LL.print_ll()

    if p:
        LL.partition(p)
        print("partitioned:")
        LL.print_ll()

    if pal:
        return LL.palindrome()

