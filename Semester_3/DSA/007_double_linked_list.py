# Doubly Linked List
# Demonstrates:
# insert at end, insert at start, delete by value, display forward


class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None


# Insert at end
def insert_at_end(head, value):
    new_node = Node(value)

    if head is None:
        return new_node

    temp = head

    while temp.next is not None:
        temp = temp.next

    temp.next = new_node
    new_node.prev = temp

    return head


# Insert at start
def insert_at_start(head, value):
    new_node = Node(value)

    if head is not None:
        head.prev = new_node

    new_node.next = head
    head = new_node

    return head


# Delete first occurrence of value
def delete_node(head, value):
    temp = head

    # Find the node
    while temp is not None and temp.data != value:
        temp = temp.next

    # Value not found
    if temp is None:
        return head

    # If deleting a node that has a previous node
    if temp.prev is not None:
        temp.prev.next = temp.next
    else:
        # Deleting the head
        head = temp.next

    # If there is a next node
    if temp.next is not None:
        temp.next.prev = temp.prev

    return head


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

print("Doubly Linked List after insertion:", end=" ")
display(head)

print("Insert 100 at start.")
head = insert_at_start(head, 100)

print("After inserting 100 at start:", end=" ")
display(head)

val = int(input("Enter value to delete: "))
head = delete_node(head, val)

print("After deletion:", end=" ")
display(head)