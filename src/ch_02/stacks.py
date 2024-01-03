"""
A stack is a linear data structure to store a one-dimensional list. It can store items either in a
Last-In, First-Out (LIFO) or First-In, Last-Out (FILO) manner. The defining characteristic of a
stack is the way elements are added to and removed from it. A new element is added at one end
and an element is removed from that end only.

The following are the operations related to stacks:
• isEmpty: Returns true if the stack is empty
• push: Adds a new element
• pop: Returns the element added most recently and removes it
"""

class Stack:

    def __init__(self):
        self.items: list = []

    def isEmpty(self) -> bool:
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def representation(self):
        return self.items


if __name__ == '__main__':
    stack = Stack()
    stack.push('Red')
    stack.push('Green')
    stack.push("Blue")
    stack.push("Yellow")
    print(stack.representation())
    stack.pop()
    print(stack.isEmpty())
    print(stack.representation())
