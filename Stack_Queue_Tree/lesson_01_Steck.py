#Стек (Stack) — это структура данных, работающая по принципу "последний пришел, первый ушел" (Last In, First Out, LIFO).

class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):#проверка, пуст ли стек.
        return self.items == []

    def push(self, item): #добавление элемента в стек,
        self.items.append(item)

    def pop(self):#удаление верхнего элемента,
        return self.items.pop()

    def peek(self):#получение верхнего элемента без удаления,
        return self.items[-1]

stack = Stack()
print(stack.is_empty())

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.is_empty())

print(stack.peek())