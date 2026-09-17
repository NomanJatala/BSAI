MAX = 100
# Simple stack implementation using fixed-size list
class Stack:

    def __init__(self):
        self.top = -1
        self.arr = [0] * MAX

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == MAX - 1

    def push(self, x):
        if self.is_full():
            print("Stack Overflow")
            return

        self.top += 1
        self.arr[self.top] = x

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return

        self.top -= 1

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return -1

        return self.arr[self.top]

    def display(self):
        for i in range(self.top, -1, -1):
            print(self.arr[i], end=" ")

        print()


# Main program
s = Stack()

n = int(input("Enter number of elements to push: "))

for i in range(n):
    val = int(input("Enter value: "))
    s.push(val)

print("Stack (top to bottom):", end=" ")
s.display()

print("Peek top:", s.peek())

print("Pop one element")
s.pop()

print("Stack now:", end=" ")
s.display()