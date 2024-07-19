#Очередь (Queue) — это структура данных, работающая по принципу "первый пришел — первый ушел" (First In, First Out).

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

queue = Queue()
print(queue.is_empty())

queue.enqueue("действие 1")
queue.enqueue("действие 2")
queue.enqueue("действие 3")
queue.enqueue("действие 4")

# ["действие 4", "действие 3", "действие 2", "действие 1"]
print(queue.is_empty())#очередь на пустоту
print(queue.size())#Узнаем размер списка (количество элементов очереди)
print(queue.dequeue())#Удалим из очереди один элемент (действие 1)
print(queue.size())