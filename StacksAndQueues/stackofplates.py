class SetofStacks:
    """Prompt: when a stack exceeded a value, create a new stack."""

    def __init__(self):
        self.items_collection = []
        self.items = []

    def pop(self):
        return self.items.pop(0)

    def push(self, item):
        if self.is_full():
            self.items =[]
            return self.push(item)
        if self.is_empty:
            self.items_collection.insert(0,self.items)

        self.items.insert(0,item)

    def peek(self):
        return self.items[0]

    def is_empty(self):
        return self.items == []

    def is_full(self):
        return len(self.items) == 10

    def popAt(self, index):
        return self.items_collection[index].pop(0)
