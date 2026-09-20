# Bubble Sort
# Repeatedly compare adjacent elements and swap if out of order.
# Time Complexity: O(n^2)
# Stable sort

n = int(input("Enter number of elements: "))

arr = []
print("Enter elements:")
for i in range(n):
    arr.append(int(input()))

for i in range(n - 1):
    # Last i elements are already in place
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            # Swap arr[j] and arr[j + 1]
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted Array:", end=" ")
for num in arr:
    print(num, end=" ")