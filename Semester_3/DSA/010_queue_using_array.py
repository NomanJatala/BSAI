MAX = 100


class Queue:

    def __init__(self):
        self.arr = [0] * MAX
        self.front = 0
        self.rear = -1

    def is_empty(self):
        return self.rear < self.front

    def is_full(self):
        return self.rear == MAX - 1

    def enqueue(self, x):
        if self.is_full():
            print("Queue Overflow")
            return

        self.rear += 1
        self.arr[self.rear] = x

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return

        self.front += 1

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return -1

        return self.arr[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return

        for i in range(self.front, self.rear + 1):
            print(self.arr[i], end=" ")

        print()


# Main program
q = Queue()

n = int(input("Enter number of elements to enqueue: "))

for i in range(n):
    val = int(input("Enter value: "))
    q.enqueue(val)

print("Queue (front to rear):", end=" ")
q.display()

print("Front element:", q.peek())

print("Dequeue one element")
q.dequeue()

print("Queue now:", end=" ")
q.display()