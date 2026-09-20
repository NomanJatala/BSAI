# Singly Linked List
# Demonstrates:
# insert at end, insert at start, delete by value,
# search, and display


# Node class
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


# Insert value at the end
def insert_at_end(head, value):
    new_node = Node(value)

    if head is None:
        return new_node

    temp = head

    while temp.next is not None:
        temp = temp.next

    temp.next = new_node
    return head


# Insert value at the start
def insert_at_start(head, value):
    new_node = Node(value)

    new_node.next = head
    head = new_node

    return head


# Delete first occurrence of value
def delete_node(head, value):

    if head is None:
        return head

    # If first node contains the value
    if head.data == value:
        head = head.next
        return head

    prev = head
    cur = head.next

    while cur is not None and cur.data != value:
        prev = cur
        cur = cur.next

    # Value not found
    if cur is None:
        return head

    prev.next = cur.next

    return head


# Search for a value
def search(head, key):
    temp = head

    while temp is not None:
        if temp.data == key:
            return True

        temp = temp.next

    return False


# Display list
def display(head):
    temp = head

    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next

    print()


# Main program
head = None

n = int(input("Enter number of nodes to insert: "))

for i in range(n):
    val = int(input("Enter value: "))
    head = insert_at_end(head, val)

print("List after insertion at end:", end=" ")
display(head)

print("Insert at start value 5")
head = insert_at_start(head, 5)

print("List after inserting 5 at start:", end=" ")
display(head)

val = int(input("Enter value to delete: "))
head = delete_node(head, val)

print("List after deletion:", end=" ")
display(head)

val = int(input("Enter value to search: "))

if search(head, val):
    print("Found")
else:
    print("Not Found")