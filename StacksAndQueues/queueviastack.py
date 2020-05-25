class QueueAsStacks:
    #catch the things
    """Prompt: Make a queue using two stacks."""

    def __init__(self):
        self.pop_stack = []
        self.push_stack = []

    def push(self, item):
        """Add item to top of stack"""
        self.push_stack.append(item)

    def _flip(self):
        while self.push_stack:
            item = self.push_stack.pop()
            self.pop_stack.append(item)

    def pop(self):
        if not self.pop_stack:
            self._flip()
        return self.items.pop()

    def peek(self):
        if not self.pop_stack:
            self._flip()
        return self.pop_stack[-1]
