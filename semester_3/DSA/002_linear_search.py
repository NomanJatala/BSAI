# Linear Search (sequential search)
# Time Complexity: O(n)
# Returns first index where key matches (0-based)

n = int(input("Enter number of elements: "))

arr = []
print("Enter elements:")
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter value to search: "))

# Linear scan through array
for i in range(n):
    if arr[i] == key:
        print(f"Element found at index {i} (0-based).")
        break
else:
    print("Element not found.")