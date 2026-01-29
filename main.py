class Stack:
    def __init__(self):
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        if not self._items:
            return None
        return self._items.pop()

    def is_empty(self):
        return len(self._items) == 0


def main():
    data = [1, 2, 3, 4, 5]

    stack = Stack()

    for value in data:
        stack.push(value)

    while not stack.is_empty():
        print(stack.pop())


if __name__ == "__main__":
    main()
