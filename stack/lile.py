class Stack:

  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    if not self.is_empty():
      return self.items.pop()
    raise IndexError("Помилка: стек порожній")

  def peek(self):
    if not self.is_empty():
      return self.items[-1]
    raise IndexError("Помилка: стек порожній")

  def is_empty(self):
    return len(self.items) == 0


# Приклад використання стека:
my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

print("Верхній елемент (peek):", my_stack.peek()) 
print("Видалено елемент (pop):", my_stack.pop()) 
print("Верхній елемент після pop:", my_stack.peek()) 
