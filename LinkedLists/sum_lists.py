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

     
def process_vals(data, rev=True):
    """Processes given integer and returns a linked list object of the digits

       Args:
           vals: int
           rev: boolean
               if True, the digits are reversed before a linked list is created
       Returns:
           LL: Linked List

    """

    LL = LinkedList()
    if rev:
        vals = reverse_vals(data)
    else:
        vals = vals_as_list(data)
    for i in vals:
        LL.insert_into_ll(i)
    return LL

def vals_as_list(data):
    """Returns a list composed of digits in an int
    """
    int_list = []
    data_as_str = str(data)
    for i in data_as_str:
        int_list.append(int(i))
    return int_list

def reverse_vals(data):
    """Returns a list of integers out of digits in given integer, in reverse order"

       Args:
           data: int
       Returns:
           int_list: list
    """           

    int_list = []
    data_as_str = str(data)
    length = len(data_as_str)
    count = length-1
    for i in range(0,length):
        int_list.append(int(data_as_str[count]))
        count-=1

    return int_list

def sum_lists(vals1=None, vals2=None, ll1=None, ll2=None, rev=True):
    """Prompt: Write a function that adds two numbers and returns the sum as a linked list

       Further details: Two numbers represented as a linked list (alternate: provide values 
       are turned into a linked list), where each node contains a single digit. 

       Args:
           vals1, vals2: integer
           ll1, ll2: LinkedList
           rev: boolen
               if revered is True, then the values or linked lists provided are assumed 
               to be in reverse order of the digits of the integer. The returned Linked List 
               Nodes will also be in reverse order of the sum
    """


    if vals1 and vals2:
        LL1 = process_vals(vals1, rev=rev)
        LL2 = process_vals(vals2, rev=rev)
        LL_val = add_lists(LL1,LL2,rev=rev)
    elif ll1 and ll2:
        LL_val = add_lists(ll1,ll2,rev=rev)
    else:
        print("Give things")
        
    LL_sum = process_vals(LL_val,rev=rev)

    LL_sum.print_ll()
