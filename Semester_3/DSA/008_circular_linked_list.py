# Circular Linked List
# Demonstrates:
# insertion at end/start, deletion by value, and display


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


# Insert at end
def insert_at_end(head, value):
    new_node = Node(value)

    if head is None:
        head = new_node
        new_node.next = head
        return head

    temp = head

    while temp.next != head:
        temp = temp.next

    temp.next = new_node
    new_node.next = head

    return head


# Insert at start
def insert_at_start(head, value):
    new_node = Node(value)

    if head is None:
        head = new_node
        new_node.next = head
        return head

    temp = head

    while temp.next != head:
        temp = temp.next

    temp.next = new_node
    new_node.next = head
    head = new_node

    return head


# Delete first occurrence of value
def delete_node(head, value):

    if head is None:
        print("List is empty.")
        return head

    # Single node
    if head.data == value and head.next == head:
        head = None
        return head

    # Deleting head
    if head.data == value:
        last = head

        while last.next != head:
            last = last.next

        head = head.next
        last.next = head

        return head

    # Deleting a node other than head
    prev = head
    cur = head.next

    while cur != head and cur.data != value:
        prev = cur
        cur = cur.next

    # Value not found
    if cur == head:
        print("Value not found.")
        return head

    prev.next = cur.next

    return head


# Display circular linked list
def display(head):

    if head is None:
        print("List is empty.")
        return

    temp = head

    print("Circular Linked List:", end=" ")

    while True:
        print(temp.data, end=" ")
        temp = temp.next

        if temp == head:
            break

    print()


# Main program
head = None

n = int(input("Enter number of nodes to insert: "))

for i in range(n):
    v = int(input("Enter value: "))
    head = insert_at_end(head, v)

print("List after insertion:", end=" ")
display(head)

print("Insert 999 at start.")
head = insert_at_start(head, 999)

print("List after inserting at start:", end=" ")
display(head)

v = int(input("Enter value to delete: "))
head = delete_node(head, v)

print("After deletion:", end=" ")
display(head)