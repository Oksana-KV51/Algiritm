# Реализация стека (LIFO - Last In, First Out)

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Попытка извлечения элемента из пустого стека")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Попытка просмотра элемента в пустом стеке")
        return self.items[-1]

    def size(self):
        return len(self.items)

# Пример использования стека
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Output: 3
print(stack.peek()) # Output: 2
print(stack.size()) # Output: 2