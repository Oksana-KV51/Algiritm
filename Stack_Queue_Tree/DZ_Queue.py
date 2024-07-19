# Реализация очереди (FIFO - First In, First Out)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Попытка извлечения элемента из пустой очереди")
        return self.items.pop(0)

    def size(self):
        return len(self.items)

# Пример использования очереди
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue()) # Output: 1
print(queue.size())    # Output: 2