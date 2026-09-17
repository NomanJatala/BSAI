# Array Operations: Insertion, Deletion, Traversal

arr = []

n = int(input("Enter number of elements: "))

print(f"Enter {n} elements:")
for i in range(n):
    arr.append(int(input()))

while True:
    print("\n--- Array Operations Menu ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        pos = int(input("Enter position (0-based): "))
        value = int(input("Enter value: "))

        if pos < 0 or pos > len(arr):
            print("Invalid position.")
        else:
            arr.insert(pos, value)
            print(f"Inserted {value} at position {pos}.")

    elif choice == 2:
        pos = int(input("Enter position (0-based) to delete: "))

        if pos < 0 or pos >= len(arr):
            print("Invalid position.")
        else:
            del arr[pos]
            print(f"Deleted element at position {pos}.")

    elif choice == 3:
        print("Array elements:", end=" ")
        for item in arr:
            print(item, end=" ")
        print()

    elif choice == 4:
        print("Exiting array operations.")
        break

    else:
        print("Invalid choice. Try again.")