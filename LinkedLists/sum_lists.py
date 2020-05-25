class Node: 
    def __init__(self, data, next_node=False):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_into_ll(self,data):
        new_node = Node(data)

        if self.head:
            cur_node = self.head
            while cur_node.next_node:
                cur_node = cur_node.next_node
            cur_node.next_node = new_node
        else: 
            self.head = new_node

    def print_ll(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next_node

def add_lists(LL1, LL2, rev=True):
    """Returns value of list integers

       Args:
           LL1: Linked List Object
           LL2: Linked List Object
           rev: boolean
       Returns:
           int
    """
    ll1_int = process_list(LL1,rev=rev)
    ll2_int = process_list(LL2,rev=rev)

    final_val = ll1_int + ll2_int
    return final_val

def process_list(LL,rev=True):
    """Returns integer made from nodes

       Args:
           LL: Linked List Object
       Returns:
           int
               integer is in reverse order as LL object
    """
    cur_node = LL.head

    ll_list = []
    while cur_node:
        ll_list.append(cur_node.data)
        cur_node = cur_node.next_node

    if rev:
        ll_list.reverse()

    strings = (str(i) for i in ll_list)
    string = "".join(strings)
    return int(string)

     
def sum_lists(ll1=None, ll2=None, rev=True):
    """Prompt: Write a function that adds two numbers and returns the sum as a linked list

       Further details: Two numbers represented as a linked list, where each node contains a single digit. 

       Args:
           ll1, ll2: LinkedList
           rev: boolen
               if revered is True, then the values or linked lists provided are assumed 
               to be in reverse order of the digits of the integer. The returned Linked List 
               Nodes will also be in reverse order of the sum
    """

    if not ll1 and ll2:
        print("Plz gib values")

    LL_val = add_lists(ll1,ll2,rev=rev)
    LL_sum = process_list(LL_val,rev=rev)
    LL_sum.print_ll()
