# Binary Search (requires sorted input)
# Time Complexity: O(log n)
# Returns index (0-based) if found, or reports not found.

n = int(input("Enter number of elements (sorted order): "))

arr = []
print("Enter sorted elements:")
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter value to search: "))

low = 0
high = n - 1

while low <= high:
    mid = low + (high - low) // 2  # avoids overflow

    if arr[mid] == key:
        print(f"Element found at index {mid} (0-based).")
        break
    elif key < arr[mid]:
        high = mid - 1  # search left half
    else:
        low = mid + 1   # search right half
else:
    print("Element not found.")# Binary Search (requires sorted input)
# Time Complexity: O(log n)
# Returns index (0-based) if found, or reports not found.

n = int(input("Enter number of elements (sorted order): "))

arr = []
print("Enter sorted elements:")
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter value to search: "))

low = 0
high = n - 1

while low <= high:
    mid = low + (high - low) // 2  # avoids overflow

    if arr[mid] == key:
        print(f"Element found at index {mid} (0-based).")
        break
    elif key < arr[mid]:
        high = mid - 1  # search left half
    else:
        low = mid + 1   # search right half
else:
    print("Element not found.")