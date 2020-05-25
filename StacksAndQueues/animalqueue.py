class Node: 
    def __init__(self, age, next_animal=None):
        self.animal = animal
        self.next_animal = next_animal

class AnimalList:
    """Prompt: Create a queue which is strictly FIFO for animal adoption

       Additional requirements: People can choose between a cat or dog
    """
    def __init__(self):
        self.head = None

    def enqueue(self, animal):
        new_node = Node(animal)

        if self.head:
            cur = self.head
            while cur:
                cur = cur.next_animal
            cur.next_animal = new_node
        else:
            self.head = new_node

    def dequeue(self, animal=None):
        cur = self.head
        if animal:
            active = cur.next_animal
            while not active.animal == animal:
                cur = active
                active = active.next_animal
                
            cur.next_animal = active.next_animal
        else:
            self.head = cur.next_animal

        print(f"Here's your new {cur.animal}!")
